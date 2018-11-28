//
//  main.cpp
//  codejam
//
//  Created by Noura Ahmed on 4/8/17.
//  Copyright © 2017 Nura Ahmed. All rights reserved.
//
#include <fstream>
#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <vector>
#include<string>

using namespace std;  // since cin and cout are both in namespace std, this saves some text


void findCount(int i, int testCase){
    int lst = i;
    int flag = 0;
    vector<int> digits;
    while(lst)
    {
        digits.push_back(lst%10);
        lst /= 10;
        if (digits.back() < lst%10) {
            flag = 1;
            break;
        }
    }
    if (flag != 1) {
        cout << "Case #" << testCase << ": " << i << endl;
        
    }
    else{
        digits.clear();
        findCount(--i, testCase);
    }
}
int main(int argc, char* argv[]) {
    int t, n;
 
    //std::map <int, int> number_list;
    std::ifstream initfile(argv[1]);
    string outputString;
    std::string inputString;
    

    std::getline(initfile, inputString);
    t = std::stoi(inputString);
    for (int i = 1; i <= t; ++i) {
        std::getline(initfile, inputString);
        n = std::stoi(inputString);
        findCount(n, i);
        // cout knows that n + m and n * m are ints, and prints them accordingly.
        // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
    }

    
    return 0;
}
