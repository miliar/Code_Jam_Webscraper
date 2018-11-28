//
//  main.cpp
//  TidyNumbers
//
//  Created by Armaan Sethi on 4/7/17.
//  Copyright © 2017 Armaan Sethi. All rights reserved.
//

#include <iostream>
#include <vector>
using namespace std;
void findTidy(string s){
    int broken = -1;
    int i = 0;
    while(i < s.length()-1 && broken == -1){
        if((s[i]-'0') > (s[i+1] - '0')){
            while(i >= 0 && s[i-1] == s[i]){
                i--;
            }
            broken = i;
            s[i] = s[i] - 1;
        }
        i++;
    }
    if(broken != -1){
        for(int z = broken+1; z < s.length(); z++){
            s[z] = '9';
        }
    }
    for(int k = 0; k < s.size(); k++){
        if(s[k] != '0'){
            cout << s[k];
        }
    }cout << endl;

}

int main(int argc, const char * argv[]) {
    // insert code here...
    int T;
    std::string N;
    std::cin >> T;
//    std::cout << "T: " << T << std::endl;
    for(int i = 0; i < T; ++i){
        std::cin >> N;
//        std::cout << "N: " << N << std::endl;
        cout << "Case #" << i+1 << ": ";
        if(N == "0"){
            cout << N;
        }
        findTidy(N);
    }
    return 0;
}
