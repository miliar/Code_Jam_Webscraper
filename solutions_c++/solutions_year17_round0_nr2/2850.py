//
//  main.cpp
//  codejam02
//
//  Created by hyspace on 4/8/17.
//  Copyright © 2017 hyspace. All rights reserved.
//

#include <iostream>
#include <string>
#include <sstream>

using namespace std;

typedef unsigned long long num;

num cal(num input_num){
    string input = to_string(input_num);
    char max = '0';
    string pre;
    for(int i = 0; i < input.size(); ++i){
        char c = input[i];
        if(c >= max){
            pre.push_back(c);
            max = c;
        }else{
            num pre_num = cal(stoull(pre) - 1);
            for(int j = i; j < input.size(); ++j){
                pre_num *= 10;
                pre_num += 9;
            }
            return pre_num;
        }
    }
    return input_num;
}

int main(int argc, const char * argv[]) {
    int num_cases;
    cin >> num_cases;
    for(int i = 0; i < num_cases; ++i){
        num data;
        cin >> data;
        
        
        cout << "case #" << i + 1 << ": ";
        
        num res = cal(data);
        cout << res << endl;
    }
    return 0;
}
