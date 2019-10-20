#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  tp2.py
#  
#  Copyright 2019 sandro <sandro@PERSONAL>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


print("Hola mundo")
print("Que es Git: Git es un software de control de versiones diseñado por Linus Torvalds, pensando en la eficiencia y la confiabilidad del mantenimiento de versiones de aplicaciones cuando éstas tienen un gran número de archivos de código fuente.")
print("-------------")
print("GitHub es una forja para alojar proyectos utilizando el sistema de control de versiones Git. Se utiliza principalmente para la creación de código fuente de programas de computadora. El software que opera GitHub fue escrito en Ruby on Rails. Desde enero de 2010, GitHub opera bajo el nombre de GitHub, Inc")
print("-------------")
print("Gitlab es un servicio web de control de versiones y desarrollo de software colaborativo basado en Git. Además de gestor de repositorios, el servicio ofrece también alojamiento de wikis y un sistema de seguimiento de errores, todo ello publicado bajo una Licencia de código abierto")
print("-------------")
print("Diferencia : Desde hace pocas fechas la versión gratuita de GitHub permite crear repositorios privados y gratuitos. Esto es algo que ya ofrecía GitLab. Sin embargo existen diferencias entre ambos servicios. No son muy grandes, pero sí puede hacer que algunos usuarios se decanten por una u otra, según lo que necesiten.Esta diferencia reside en el número máximo de colaboradores por repositorio. GitHub permite crear repositorios privados de manera ilimitada, pero con un máximo de 3 colaboradores. Por su parte GitLab permite también crear repositorios privados ilimitados y gratuitos, pero en esta ocasión no hay límite de colaboradores.")
print("-------------")
print("""  Funcionalidades de GitLab; 
GitLab  se puede usar en un servidor propio,  incluye varias herramientas casi imprescindibles para cualquier proyecto como gestión de peticiones para recoger las historias, wiki como documentación e información y pages para generar pequeños sitios web además de los repositorios de Git o el servidor de integración y entrega continua. Que GitLab incluya por defecto todas estas herramientas hace innecesario recurrir en la mayoría de los casos a varias herramientas especializadas que cubran estas necesidades como JIRA, Jenkins, MediaWiki o un servidor web para los sitios web.""")
print("-------------")
print("""Quienes pueden usar sus datos : Usuarios

Los usuarios en Gitlab son las cuentas que abre la gente. Las cuentas de usuario no tienen ninguna complicación: viene a ser una colección de información personal unida a la información de login. Cada cuenta tiene un espacio de nombres (namespace) que es una agrupación lógica de los proyectos que pertenecen al usuario. De este modo, si el usuario jane tiene un proyecto llamado project, la URL de ese proyecto sería http://server/jane/project.
Para trabajar en un proyecto GitLab lo más simple es tener acceso de escritura (push) sobre el repositorio git. Puedes añadir usuarios al proyecto en la sección “Members” de los ajustes del mismo, y asociar el usuario con un nivel de acceso (los niveles los hemos visto en Grupos). Cualquier nivel de acceso tipo “Developer” o superior, permite al usuario enviar commits y ramas sin ninguna limitación.""")

print("-------------")
print("""Que proyectos colocarias en github y cuales en gitlab?¿Porque?

con GitLab es que podemos montarnos una réplica de un producto on premise, es decir, en nuestra instalación. 
Si formamos parte de una estructura empresarial que es celosa de albergar su código fuente en un tercero, por problemas o necesidades varias,
 podemos montarnos en nuestra instalación este mismo servicio tal cual y es  gratuito.
con GitHub : Los repositorios públicos quedan igual: gratis y con colaboradores ilimitados. 
Bajo el nombre GitHub Enterprise se unirán el antiguo Enterprise Cloud y Enterprise Server, y al precio de uno solo.
pero solo te permite repositorios privados bajo suscripción""")


print("-------------")



print(""" Principales Comandos : 
git help

Muestra una lista con los comandos más utilizados en GIT.

git init

Podemos ejecutar ese comando para crear localmente un repositorio con GIT y así utilizar todo el funcionamiento que GIT ofrece.  Basta con estar ubicados dentro de la carpeta donde tenemos nuestro proyecto y ejecutar el comando.  Cuando agreguemos archivos y un commit, se va a crear el branch master por defecto.

git add + path

Agrega al repositorio los archivos que indiquemos.

git add -A

Agrega al repositorio TODOS los archivos y carpetas que estén en nuestro proyecto, los cuales GIT no está siguiendo.

git commit -m "mensaje" + archivos

Hace commit a los archivos que indiquemos, de esta manera quedan guardados nuestras modificaciones.

git commit -am "mensaje"

Hace commit de los archivos que han sido modificados y GIT los está siguiendo.

git checkout -b NombreDeBranch

Crea un nuevo branch y automaticamente GIT se cambia al branch creado, clonando el branch desde donde ejecutamos el comando.

git branch

Nos muestra una lista de los branches que existen en nuestro repositorio.

git checkout NombreDeBranch

Sirve para moverse entre branches, en este caso vamos al branch que indicamos en el comando.

git merge NombreDeBranch

Hace un merge entre dos branches, en este caso la dirección del merge sería entre el branch que indiquemos en el comando, y el branch donde estémos ubicados.

git status

Nos indica el estado del repositorio, por ejemplo cuales están modificados, cuales no están siendo seguidos por GIT, entre otras características.

git clone URL/name.git NombreProyecto

Clona un proyecto de git en la carpeta NombreProyecto.

git push origin NombreDeBranch

Luego de que hicimos un git commit, si estamos trabajando remotamente, este comando va a subir los archivos al repositorio remoto, específicamente al branch que indiquemos.

git pull origin NombreDeBranch

Hace una actualización en nuestro branch local, desde un branch remoto que indicamos en el comando.""")

print("-------------")


