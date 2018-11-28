#include <sstream>
#include <fstream>
#include <string>

#include <algorithm>
#include <iostream>
#include <map>
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


    int64_t N = 0;
    int64_t k = 0;

    while (std::getline(infile, line))  // this does the checking!
    {
        std::map<int64_t, int64_t> intervalList;
        std::map<int64_t, int64_t>::iterator max;

        std::istringstream iss(line);
        iss >> N;
        iss >> k;

        intervalList[N] = 1;
        while( k > 0 ){
           
            #ifdef DEBUG_OUTPUT
            std::cout << "Current k= " << k << "  List: " ;
            for(auto i: intervalList) std::cout << "(" << i.first << ',' << i.second << "), ";
            std::cout << std::endl;
            int asdf;
            std::cin >> asdf;
            #endif

            max = std::max_element(intervalList.begin(), intervalList.end(), 
                                   [](std::pair<int64_t,int64_t> a, std::pair<int64_t,int64_t> b){
                                   return a.first < b.first;});

            #ifdef DEBUG_OUTPUT
            std::cout << "max first " << max->first << " sec " << max->second << std::endl;
            #endif

            if( k - max->second <= 0){
                break;   
            }
            if(max->first%2==1){
                // check init !!
                intervalList[max->first/2] += 2*max->second;
            }
            else{
                intervalList[max->first/2-1] += max->second;
                intervalList[max->first/2]   += max->second;
            }
            k -= max->second;
            intervalList.erase(max);
        } 

        #ifdef DEBUG_OUTPUT
        std::cout << "final max first " << max->first << " sec " << max->second << std::endl;
        #endif

        std::cout << "Case #" << ++case_ <<  ": ";
        std::cout << (max->first)/ 2 << " " << (max->first-1) / 2 << std::endl;
    }
    return 0;
}
