//
// Created by gopia on 08/04/2017.
//

#include <iostream>
#include <queue>
#include <unordered_map>
#include <fstream>
#include <bitset>

int check_increasing(long long *arr, int len) {
    int next_non_zero = 0;
    for(int i = 0; i<len-1; i++) {
            //std::cout << arr[i] << " > " << arr[i+1] << std::endl;
        if(arr[i] > arr[i+1]) return (arr[i] == 0 ? next_non_zero : i);
        if(arr[i] != 0) next_non_zero = i;
    }
    return -1;

}

std::string find_neat_number(std::string s) {
    long long arr [s.length()];

    // initialize the array
    for(int i = 0; i<s.length(); i++) {
        arr[i] = s[i] - '0';
        //std::cout << arr[i] << ", ";
    }
    //std::cout << std::endl;

    while(1) {
        /*for(int i = 0; i<s.length(); i++) {
            std::cout << arr[i] << ", ";
        }

        std::cout << std::endl;*/
        std::string temp;

        for(int i = 0; i<s.length(); i++) {
                temp += ('0' + arr[i]);
        }

        //std::cout << "Temp: " << temp << std::endl;
        long  violating = check_increasing(arr, s.length());
        //std::cout << "Violating character: " << violating << std::endl;
        if(violating == -1) break;
        // roll through the array until the first violating character is met

        // Then find the first element that can be decreased, decrease it, give value to next
        arr[violating]--;
        arr[violating+1]+=10;
        while(arr[violating+1]  > 9 ) {
            long long loss = arr[violating+1] - 9;
               arr[violating+1] -= loss;
            if(violating + 1 != s.length()) {
                violating++;
                arr[violating+1] += 10;
            }
        }
    }
    std::string result;
    int start  = 0;
    while(arr[start] == 0 && start < s.length()-1) start++;
    for(int i = start; i<s.length(); i++) {
        result += ('0' + arr[i]);
    }
    return result;

}



int main() {
    std::ifstream input_data = std::ifstream("input.txt", std::ifstream::in);
    std::ofstream output_data ("output.txt", std::ofstream::out);

    int T;
    input_data >> T;
    for(int i = 1; i<=T; i++) {
        std::string N;
        input_data >> N;
        output_data << "Case #" << i << ": " << find_neat_number(N) << std::endl;
    }


}




