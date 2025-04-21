--------------------MODELO DE SEGREGACIÓN DE SCHELLING---------------------------
- En la interfaz gráfica vienen los siguientes botones:
   * setup : sirve para crear el mundo usable para la primera versión del modelo
             donde hay agentes verdes y rojos con un porcentaje de similitud
             ajustable con el deslizador "%similitud-requerida"
   * setup3 : sirve para crear el mundo usable para la tercera versión del modelo
              donde hay 3 tipos de agentes, su porcentaje de similitud se controla
              con el mismo deslizador de "%similitud-requerida"
   * go : pone a andar la simulación tanto para el setup 1 como el setup 3
   * densidad : deslizador que controla la cantidad de agentes que hay en el mundo
                este deslizador funciona para todas las versiones del modelo
                setup, setup2, setup3
   * %similitud-requerida : es un deslizador que controla el parámetro de
                            similitud requerida del primer y tercer modelo (setup,
                            setup2)
   * setup2 : crea un mundo donde hay dos tipos de agentes pero cada agente define
              su propio parámetro de similitud dependiendo de lo que se ingrese
              con los deslizadores de similitud-individual y desviación
   * similitud-individual : parámetro de similitud que puede tener cada agente
                            individualmente
   * desviación : maneja las unidades de margen superior e inferior respecto a
                  la similitud individual

--------------------MODELO DE TERMITAS APILADORAS-------------------------------
- Este modelo lo hice en el lenguaje de programación Python, por lo que es
  necesario tener instalado Python para poderlo usar
- Es necesario tener instaladas las librerías matplotlib y numpy
  * pip install matplotlib
  * pip install numpy
- Para ejecutarlo abre una terminal en Linux o el símbolo del sistema en Windows
- Dirigirse a la carpeta que contiene el archivo termitas.py
- ejecutarlo con la instrucción > Python termitas.py o > Python3 termitas.py
- ingresar los parámetros que requieran.

  *sugerencia*
  para el tiempo poner un parámetro bastante grande como 4000

NOTAS:
- No pude hacer que se no se encimaran las astillas en el mismo sitio por eso se
ve que desaparecen pero en realidad las apilan en la misma cuadrícula.
- El modo de asignación de las astillas es por probabilidad de que estén o no
  estén en la cuadrícula, no pude hacer que sea como que de una densidad global.