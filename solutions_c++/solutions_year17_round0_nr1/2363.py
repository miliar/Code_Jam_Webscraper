#include <sstream>
#include <fstream>
#include <string>

#include <algorithm>
#include <iostream>
#include <vector>

int main(int argc, char**argv){

    if(argc != 2){
        std::cout << "Pass the filename" << std::endl;
        return 0;
    }

    std::string line;
    std::ifstream infile(argv[1]);

    int case_ = 0;
    std::getline(infile,line); // discard number of cases


    long long k = 0;
    std::string pancakes;

    while (std::getline(infile, line))  // this does the checking!
    {
        std::istringstream iss(line);
        iss >> pancakes;
        iss >> k;
        int flips = 0;
        std::cerr << "Starting conf " << pancakes << std::endl;

        for(int n = 0; n <= pancakes.length() - k; ++n){
            if( pancakes[n] == '-'){
                ++flips;
                for(int i=0;i<k;++i){
                    if(pancakes[n+i] == '-') pancakes[n+i] = '+';
                    else if(pancakes[n+i] == '+') pancakes[n+i] = '-';
                    else{
                        std::cerr << "something went wrong flipping" << std::endl;
                    }
                }
            }
        }
        // verify that all are up
        bool allUp = true;
        for(int i=0; i<pancakes.length(); ++i){
            allUp &= (pancakes[i] == '+');
        }
        std::cerr << "Looks like this now: " << pancakes << std::endl;

        std::cout << "Case #" << ++case_ <<  ": ";
        if(!allUp) std::cout << "IMPOSSIBLE" << std::endl;
        else std::cout << flips << std::endl;

    }
    return 0;
}
