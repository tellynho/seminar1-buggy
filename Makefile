objects = hello.o

all: hello

hello: $(objects)
	g++ -o hello $(objects)