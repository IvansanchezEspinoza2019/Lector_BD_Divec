CREATE TABLE carrera(
id INT PRIMARY KEY AUTO_INCREMENT,
nombre VARCHAR(50) NOT NULL
);

CREATE TABLE profesor(
id INT PRIMARY KEY AUTO_INCREMENT,
nombre VARCHAR(60) NOT NULL
);

CREATE TABLE dia(
id INT PRIMARY KEY AUTO_INCREMENT,
dia VARCHAR(60) NOT NULL
);

CREATE TABLE hora(
id INT PRIMARY KEY AUTO_INCREMENT,
hora VARCHAR(40) NOT NULL
);

CREATE TABLE aula(
id INT PRIMARY KEY AUTO_INCREMENT,
numero VARCHAR(40) NOT NULL
);

CREATE TABLE edificio(
id INT PRIMARY KEY AUTO_INCREMENT,
edificio VARCHAR(40) NOT NULL
);

CREATE TABLE periodo(
id INT PRIMARY KEY AUTO_INCREMENT,
periodo VARCHAR(30) NOT NULL
);

CREATE TABLE detalle_materia(
id INT PRIMARY KEY AUTO_INCREMENT,
clave VARCHAR(10) NOT NULL,
nombre VARCHAR(95) NOT NULL,
creditos VARCHAR(3) NOT NULL,
id_periodo INT,
FOREIGN KEY (id_periodo)
REFERENCES periodo(id)
);

CREATE TABLE materia(
id INT PRIMARY KEY AUTO_INCREMENT,
nrc VARCHAR(15) NOT NULL,
cupos VARCHAR(5) NOT NULL,
disponibles VARCHAR(5) NOT NULL,
id_profesor INT,
id_dia INT,
id_hora INT,
id_aula INT,
id_edificio INT,
id_detalle_materia INT,
FOREIGN KEY (id_profesor)
REFERENCES profesor(id),
FOREIGN KEY (id_dia)
REFERENCES dia(id),
FOREIGN KEY (id_hora)
REFERENCES hora(id),
FOREIGN KEY (id_aula)
REFERENCES aula(id),
FOREIGN KEY (id_edificio)
REFERENCES edificio(id),
FOREIGN KEY (id_detalle_materia)
REFERENCES detalle_materia(id)
);

CREATE TABLE carrera_materia(
id_detalle_materia INT,
id_carrera INT,
FOREIGN KEY (id_detalle_materia)
REFERENCES detalle_materia(id),
FOREIGN KEY (id_carrera)
REFERENCES carrera(id)
);

