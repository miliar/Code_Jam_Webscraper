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


    std::string N;

    while (std::getline(infile, line))  // this does the checking!
    {
        std::istringstream iss(line);
        iss >> N;
        //std::cout << N << std::endl;


        int i=1, // checks up to which place number is non-descending ("tidy")
            j=0; // checks up to which place number is ascending
        while(i < N.length() && int(N[i-1]) <= int(N[i])){
            if( int(N[i-1] < int(N[i]))) j = i;
            ++i;
        }
        if( i < N.length()){
            N[j] = char( int(N[j]) - 1);
            while(j < N.length()){
                N[++j] = '9';
            }
        }


        i=0;
        while(N[i] == '0') ++i;
        std::cout << "Case #" << ++case_ <<  ": ";

        for( ; i < N.length(); ++i) std::cout << N[i];
        std::cout << std::endl;

    }
    return 0;
}
