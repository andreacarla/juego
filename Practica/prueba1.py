import pygame, sys
from pygame.locals import *
#~ from random import randint
import pygame.sprite as sprite

pygame.init()
pygame.display.set_caption("Juego")

pantalla=pygame.display.set_mode((300,300))

class background(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.fondo = pygame.image.load("Imagenes/dibujo1.png")
		#~ self.tam_fondo = self.fondo.get_size()
		self.rect_fondo = self.fondo.get_rect()
		pantalla = pygame.display.set_mode((800,600))
	
	def dibujar (self):
		pantalla.blit(self.fondo,self.rect_fondo)

	def actualizar(self,pantalla,vx,vy):
		self.rect_fondo.move_ip(-vx,-vy)	
		pantalla.blit(self.fondo,self.rect_fondo)

class personaje(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.personaje1 = pygame.image.load("Imagenes/Circulo.png")
		self.rect = self.personaje1.get_rect()
		self.rect.centerx = 20
		self.rect.centery = 500
	def dibujar(self):
		pantalla.blit(self.personaje1, self.rect)
	def caminar (self):
		self.rect.centerx += 1
	def mover (self):
		tecla = pygame.key.get_pressed()
		dist = 5
		if tecla[pygame.K_DOWN]:
			self.rect.centery+=dist
		elif tecla[pygame.K_UP]:
			self.rect.centery-=dist
		if tecla[pygame.K_RIGHT]:
			self.rect.centerx+=dist 
		elif tecla[pygame.K_LEFT]:
			self.rect.centerx -=dist
	def ajustar(self):
		if event.key == pygame.K_UP:
			self.rect.centery += 3
		if event.key == pygame.K_DOWN:
			self.rect.centery -= 3
		
		
class perro(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.imagenPerrito = pygame.image.load("Imagenes/prueba1.png").convert_alpha()
		self.perrito2 = pygame.image.load("Imagenes/prueba2.png").convert_alpha()
		#~ self.perrito3 = pygame.image.load("Imagenes/perrito3.png")
		#~ self.perrito4 = pygame.image.load("Imagenes/perrito4.png")
		#~ self.perrito5 = pygame.image.load("Imagenes/perrito5.png")
		#~ 
		#~ self.images = [[self.perrito1,self.perrito2],[self.perrito3,self.perrito4]]
		
		self.listaImagenes = [self.imagenPerrito, self.perrito2]
		self.posImagen = 0
		
		self.Animacion = self.listaImagenes [self.posImagen]
		
		self.rect = self.Animacion.get_rect()
		self.rect.centerx = 400
		self.rect.centery = 500
		
		self.tiempoCambio = 1

	def animacion (self):
		
		if event.key == pygame.K_RIGHT:
			#~ if tiempo == self.tiempoCambio:
			self.posImagen += 1
			#~ self.tiempoCambio += 1

			if self.posImagen > len(self.listaImagenes)-1:
				self.posImagen = 0
		
		if event.key == pygame.K_UP:
			#~ if tiempo == self.tiempoCambio:
			self.posImagen += 1
			#~ self.tiempoCambio += 1

			if self.posImagen > len(self.listaImagenes)-1:
				self.posImagen = 0
				
		if event.key == pygame.K_DOWN:
			#~ if tiempo == self.tiempoCambio:
			self.posImagen += 1
			#~ self.tiempoCambio += 1

			if self.posImagen > len(self.listaImagenes)-1:
				self.posImagen = 0				
				
		if event.key == pygame.K_LEFT:
			#~ if tiempo == self.tiempoCambio:
			self.posImagen += 1
			#~ self.tiempoCambio += 1

			if self.posImagen > len(self.listaImagenes)-1:
				self.posImagen = 0
		
	def dibujar(self):
		tecla = pygame.key.get_pressed()
		self.Animacion = self.listaImagenes[self.posImagen]
		pantalla.blit(self.Animacion, self.rect)
		if tecla[pygame.K_LEFT]:
			self.Animacion = pygame.transform.flip(self.Animacion,True,False)
			self.posImagen += 1
			#~ self.tiempoCambio += 1

			if self.posImagen > len(self.listaImagenes)-1:
				self.posImagen = 0
			pantalla.blit(self.Animacion, self.rect)
		
	def caminar(self):
		tecla = pygame.key.get_pressed()
		
		dist = 2
		if tecla[pygame.K_DOWN]:
			self.rect.centery+=dist
		elif tecla[pygame.K_UP]:
			self.rect.centery-=dist
		if tecla[pygame.K_RIGHT]:
			self.rect.centerx+=dist 
		elif tecla[pygame.K_LEFT]:
			self.rect.centerx -=dist

	def saltar(self):
		
		while self.rect.centery > 400:
			self.rect.centery -= 1

	def pararse(self):
		while self.rect.centery < 500:
			self.rect.centery += 1
	
	def mover(self, personaje):
		if self.rect.colliderect(persona):
			persona.mover()
	#~ def limiteMov(self, dx, dy):
		#~ newX = self.x + dx
		#~ newY = self.y + dy
		#~ self.x = max(0, min(newX, w))
		#~ self.y = max(0, min(newY, w))
		
class enemigo(pygame.sprite.Sprite):
	def __init__ (self): 
		pygame.sprite.Sprite.__init__(self)
		self.enermigo = pygame.image.load("Imagenes/alien1.png")
		self.rect = self.enemigo.get_rect()
		
	
	
		
			

persona = personaje()
perrito = perro()
fondo01 = background()
reloj1= pygame.time.Clock()
vx =0
vy =0
velocidad = 7
while True:
	
	tiempo = pygame.time.get_ticks()/1000
	pantalla.fill((0,200,255))
	fondo01.dibujar()
	fondo01.update(vx,vy)
	persona.dibujar()
	persona.caminar()
	
	perrito.dibujar()
	perrito.mover(persona)
	
	

	
	for event in pygame.event.get():

		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_LEFT:
			perrito.caminar()
			perrito.animacion()
			vx=-velocidad
		if event.key == pygame.K_RIGHT:
			perrito.caminar()
			perrito.animacion()
			vx=velocidad
			
		if event.key== pygame.K_UP:
			perrito.caminar()
			perrito.animacion()
			#~ vy=-velocidad
			#~ nave.ajustar()
		if event.key == pygame.K_DOWN:
			perrito.caminar()
			perrito.animacion()
			#~ vy=velocidad
			#~ nave.ajustar()
		if event.key == pygame.K_SPACE:
			perrito.saltar()
			
	if event.type == pygame.KEYUP:
		if event.key == pygame.K_LEFT:
			vx=0

		if event.key == pygame.K_RIGHT:
			vx=0

		#~ if event.key== pygame.K_UP:
			#~ vy=0
		#~ if event.key == pygame.K_DOWN:
			#~ vy=0
		if event.key == pygame.K_SPACE:
			perrito.pararse()
			
	fondo01.dibujar()		
	fondo01.actualizar(pantalla,vx,vy)
	persona.dibujar()
	persona.caminar()
	#~ perrito.animacion()
	perrito.dibujar()
	perrito.mover(persona)
	reloj1.tick(10)
	pygame.display.flip()
	pygame.display.update()
