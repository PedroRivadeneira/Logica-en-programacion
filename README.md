
25/06/2025

LINK DEL VIDEO DE PRESENTACION: https://drive.google.com/file/d/1leK__g0Idaiig2t2V6Qzx0V9WkMyKVKw/view?usp=sharing

Programa “Adivina el número”**


Objetivo del programa:

El propósito del programa es que la computadora adivine un número entre 1 y 100 que el usuario ha pensado. Para lograrlo, se utiliza una estrategia de búsqueda binaria, preguntando al usuario si el número pensado es mayor, menor o igual al número propuesto por el programa. El programa continúa ajustando su rango de búsqueda hasta adivinar correctamente.



 Funcionalidades principales del código:

1. Mensaje inicial y pausa:

   * El programa comienza pidiéndole al usuario que piense en un número del 1 al 100.
   * Espera que el usuario presione Enter para continuar.

2. Inicialización de variables:

   * `bajo = 1`: límite inferior del rango.
   * `alto = 100`: límite superior del rango.
   * `intentos = 0`: cuenta cuántos intentos ha hecho el programa.

3. Bucle de adivinanza:

   * El programa calcula un número a mitad del rango (`(bajo + alto) // 2`).
   * Pregunta al usuario si su número es mayor, menor o igual al propuesto.
   * Según la respuesta:

     * Si es “correcto”: muestra un mensaje de éxito y termina.
     * Si es “mayor”: ajusta el límite inferior (`bajo = intento + 1`).
     * Si es “menor”: ajusta el límite superior (`alto = intento - 1`).
     * Si la respuesta no es válida: muestra un mensaje de error.

4. Terminación:

   * El programa finaliza cuando el usuario confirma que el número propuesto es correcto.


