//
//  main.cpp
//  test
//
//  Created by Shuying Sun on 2/28/17.
//  Copyright © 2017 Shuying Sun. All rights reserved.
//

#include <iostream>
using std::cout; using std::endl; using std::cin;
using std::string;
using std::ostream;
#include <fstream>
using std::ofstream;
using std::ifstream;

string last_tidy_number(string num){
    int index = 1;
    while (index < num.size() && num[index-1] <= num[index]) ++index;
    if (index == num.size()) return num;
    string res{};
    if (num[0] == '1' && num[0] == num[index-1]){
        res += string(num.size()-1,'9');
        return res;
    }
    int start_equal = 0;
    while (start_equal < index){
        if (num[start_equal] != num[index-1]){
            res += num[start_equal++];
        }
        else break;
    }
    res += num[start_equal]-1;
    res += string(num.size()-res.size(),'9');
    return res;
    
}

int main(int argc, const char * argv[]) {
    int T = 0;
    ifstream file;
    file.open("/Users/shuyingsun/Downloads/B-large.in.txt");
    file >> T;
    ofstream output;
    output.open("/Users/shuyingsun/Desktop/output.txt");
    for (int i = 1; i <= T; ++i){
        string num{};
        file >> num;
        output << "Case #" << i<<": " << last_tidy_number(num) << "\n";
    }
    file.close();
    output.close();
    return 0;
    
}
