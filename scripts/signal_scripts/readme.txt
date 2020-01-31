===============================
 Descripción de los archivos:
===============================

- "massListGenerator.py": Genera la lista de las masas mx y my (massList.txt)

- "mgScript.py":- Modifica la semilla en la run_card
                - Iniciliza los valores de los acoples en la param_card
                - Ejecuta el generate_event para cada par (mx, my) en el archivo massList.txt

===============================
	      Notas
===============================

En el archivo mgScript se deben configurar algunos parámetros, los cuales están al
inicio del archivo, antes de ejecuar el script:

   - Las rutas de los archivos "run_card.dat", "param_card.dat" y de la carpeta "./bin"
   - El valor de los acoples

Durante la ejecución del primer evento, se deben seleccionar de forma manual la ejecución 
de pythia y delphes, luego de esto la ejecución se realizará de forma automática (entre 
evento y evento se deberían esperar 60 segundos, pero no considero que esto sea muy grave
en estos momentos jajaja).


