#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>
#include <fstream>
#include <stdint.h>
#include <vector>
#include <cstdlib>

using namespace std;  // since cin and cout are both in namespace std, this saves some text

bool is_tidy(uint64_t num){
    if(num <= 9ULL){
        return true;
    }
    std::string num_s = std::to_string(num);
    uint8_t digit = (uint8_t)(num_s[0] - '0');
//    printf("%s\n",num_s.c_str());

    for(uint8_t i = num_s.length()-1; i >= 1; i--){
        if((uint8_t)(num_s[i] - '0') < (uint8_t)(num_s[i-1] - '0')){
            return false;
        }
    }
    //printf("%llu\n",num);
    return true;
}


uint64_t brute_solve(uint64_t in){
    uint64_t d = 1;
    for(uint64_t i = in; i > 0; i=i-d){
        if(is_tidy(i)){
            //printf("%llu\n",i);
            return i;
        }
    }
    return false;

}


int main(){
    std::fstream out;
    std::fstream in;
    bool first = true;
    out.open("output", std::fstream::in | std::fstream::out | std::fstream::trunc);
    in.open("input", std::fstream::in | std::fstream::out | std::fstream::in);
    unsigned num_test_cases;
    in >> num_test_cases;
    uint64_t num;
    for(unsigned i = 1; i <= num_test_cases; i++){
        in >> num;
        out << "Case #" << i << ": ";
        printf("%llu -> %llu\n",num,brute_solve(num));
        out << brute_solve(num);
        out << endl;
    }


    int k;


    return 0;
}
