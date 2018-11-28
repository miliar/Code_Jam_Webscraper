/*Sat Apr  8 09:27:16 CDT 2017, autor: (ramon)*/
#include<iostream>
#include<fstream>
#include<cstring>

#define impossible -1
#define allFlipped -2
#define notAllFlipped -3

void FlipAll(std::string str, int flipSize);
void turnCake(char *cake);
int CheckSurface(char *surface,int fullSurfaceLengt);
int CheckAlreadyFlippedCakes(char *surface,int fullSurfaceLengt);
std::fstream outputFile;

int main(int argc, char *argv[]){
std::fstream file;
std::string str;
int flipsize = 0;
int counter = 0;

file.open(argv[1],std::fstream::in);
file >> str;
outputFile.open(argv[2],std::fstream::out);

while(file >> str >> flipsize){
    counter++;
    /*std::cout << str << ", " << flipSize;
    std::cout << " " << str.size() << std::endl;*/
    std::cout << "Case #"<< counter << ": ";
    outputFile << "Case #" << counter << ": ";
    FlipAll(str,flipsize);
    std::cout << std::endl;
    outputFile << std::endl;
}
file.close();
outputFile.close();
return 0;
}

void FlipAll(std::string str, int flipSize){
    static char *surface = 0;
    surface = new char(str.size());
    std::memcpy(surface,str.c_str(),str.size());
    static int maxLimit = 0;
    maxLimit = str.size()-flipSize;
    static int fullSurfaceLengt;
    fullSurfaceLengt = str.size();
    static int result;
    result = 0;
    static int beginning;
    beginning = -1;
    static int beginning_1;
    beginning_1 = 0;
    static int counter;
    counter = 0;

    if(flipSize > fullSurfaceLengt) {
        result = impossible;
        std::cout << "IMPOSSIBLE";
        outputFile << "IMPOSSIBLE";
    }
    else{
        if(CheckSurface(surface,fullSurfaceLengt) == allFlipped){
            std::cout << "0" ;
            outputFile << "0";
        }
        else{
            do{
                beginning_1 = beginning;
                beginning = CheckAlreadyFlippedCakes(surface,fullSurfaceLengt);
                if(beginning < beginning_1){
                    std::cout << "IMPOSSIBLE"; 
                    outputFile << "IMPOSSIBLE";
                    return;
                }
                if(beginning > maxLimit){
                    std::cout << "IMPOSSIBLE"; 
                    outputFile << "IMPOSSIBLE";
                    return;
                }
                for(int flipCount = 0; flipCount < flipSize; flipCount++){
                    turnCake(&surface[beginning+flipCount]);
                }         
                counter++;
                if(CheckSurface(surface,fullSurfaceLengt) == allFlipped)
                    beginning_1 = beginning;       
            }while(beginning_1 != beginning);
            std::cout << counter;
            outputFile << counter;
        }        
    }

    if(surface != 0)delete surface;
}

void turnCake(char *cake){
    if(*cake == '-'){
        *cake = '+';
    }else{
        *cake = '-';
    }
}

int CheckSurface(char *surface,int fullSurfaceLengt){
    static int noFlippedCounter;
    noFlippedCounter=0;
    for(int i = 0; i < fullSurfaceLengt; i++){
        if(surface[i]=='-'){
            noFlippedCounter++;
        }
    }
    if(noFlippedCounter == 0){
        return allFlipped;
    }else{
        return notAllFlipped;
    }
}

int CheckAlreadyFlippedCakes(char *surface,int fullSurfaceLengt){
    static int noFlippedCounter;
    noFlippedCounter=0;
    for(int i = 0; i < fullSurfaceLengt; i++){
        if(surface[i]=='-'){
            return i;
        }
    }
    return fullSurfaceLengt-1;
}