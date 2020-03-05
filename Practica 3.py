class Estudiante:
  # Indicamos los atributos para la clase
  Edad = 0
  carrera = "Desconocida"
  universidad = "Desconocida"
  genero = "Fenemino"
  
  # Definimos funciones
  def festejar(self) : 
    print("Festejando")
  
  def estudiar(self, materia) :
    print("Estudiando" + materia)
    
  def llorar() : 
    print("Llorar")
  
  def dormir(self) : 
    print("Durmiendo")
  
  # Ajustamos la edad
  def cambiarEdad(self, edadAlumno) :
    self.edad = edadAlumno
    print("Nueva edad ", edadAlumno)
    
# Generamos un nuevo estudiante
miguel = Estudiante()
miguel.estudiar(" logica para la programacion")

#imprimimos atributos de objeto
miguel.cambiarEdad(21)
print(miguel.edad)