#include <string>
#include <sstream>
#include <vector>
#include <iterator>
#include <set>
#include <iostream>

template<typename Out>
void split(const std::string &s, char delim, Out result) {
    std::stringstream ss;
    ss.str(s);
    std::string item;
    while (std::getline(ss, item, delim)) {
        *(result++) = item;
    }
}


std::vector<std::string> split(const std::string &s, char delim) {
    std::vector<std::string> elems;
    split(s, delim, std::back_inserter(elems));
    return elems;
}

void flip(std::string &s, int start, int num){
    for(int i = start; i < start + num; i++){
        s[i] = s[i] == '-' ? '+' : '-';
    }
}

int main(){ 
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::string temp;
    std::getline(std::cin, temp);
    const int T = std::stoi(temp);

    for (int i = 1; i <= T; i++){ //Iterate through test cases
        std::cout << "Case #" << i << ": ";
        
        std::getline(std::cin, temp);
        auto vals = split(temp, ' ');

        auto pancakes = vals[0];
        auto size = std::stoi(vals[1]);

        int changes = 0;
        int len = pancakes.length();
        for(int i = 0; i < len; i++){
            if(pancakes[i] == '-'){
                if (i + size > len){
                    std::cout << "IMPOSSIBLE" << "\n";
                    break;
                }
                flip(pancakes, i, size);
                changes++;
            }
            if (i == len - 1){
                std::cout << changes << "\n";
            }
        }
    } 
}
