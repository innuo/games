#!/usr/bin/ python
# -*- coding: utf-8 -*-

"TEST to better understand the DanceCV code by Esteban Pardo Sanchez"

import cv2
import cv2.cv as cv
import numpy
import pygame
import sys

ACTIVE_THRESHOLD = 200
CAPTURE_REGION = 100
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
 
##############
class Image():
    def __init__(self, debug = False):
        
        self.capture = cv2.VideoCapture(0)
        if self.capture.isOpened():         # Checks the stream
            self.frameSize = (int(self.capture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)),
                               int(self.capture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)))        
        SCREEN_HEIGHT = self.frameSize[0]
        SCREEN_WIDTH = self.frameSize[1]
        result, self.currentFrame = self.capture.read()        
        self.currentFrame = cv2.flip(self.currentFrame, 1)

    def getCurrentFrameAsImage(self):
        im = numpy.array(self.currentFrame)
        im = cv.fromarray(im)
        cv.CvtColor(im, im, cv.CV_BGR2RGB)
        pgImg = pygame.image.frombuffer(im.tostring(), cv.GetSize(im), "RGB")
        return pgImg
    
    def debug(self):
        print "in debug"
    
    def run(self):
        result, self.currentFrame = self.capture.read()        
        #self.currentFrame = cv2.flip(self.currentFrame, 1)
        cv2.waitKey(1)
    

##############
class Scene():
    def __init__(self, screen, image):
        self.sceneClock = pygame.time.Clock()
        self.screen = screen
        self.image = image
        
    def render(self):
        frame = self.image.getCurrentFrameAsImage()
        self.screen.blit(frame, (0,0))

    def run(self):
        self.screenDelay = self.sceneClock.tick()
        self.render()
        pygame.display.flip()

##############
class TestGame():
    def __init__(self):
        self.image = Image()
        pygame.init()

        self.clock = pygame.time.Clock()
        pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("TEST")
        screen = pygame.display.get_surface()
        self.scene = Scene(screen, self.image)

    def run(self):
        while True:
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    sys.exit(0)
            self.image.run()
            self.scene.run()
            pygame.display.update()
            self.clock.tick(30)

if __name__ == '__main__':
    game =  TestGame()
    game.run()
