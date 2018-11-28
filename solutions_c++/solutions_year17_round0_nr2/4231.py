//
//  main.cpp
//  Oversized Pancake Flipper
//
//  Created by Bill Zeng on 2017-04-08.
//  Copyright © 2017 Bill Zeng. All rights reserved.
//

#include <iostream>
#include <cmath>
#include <cstring>
#include <vector>
#include <map>
#include <algorithm>
#include <queue>
#include <stack>
#include <iostream>
#include <fstream>
using namespace std;
int t;

int main(int argc, const char * argv[]) {
    // insert code here...
    ifstream fin("B-large.in");
    ofstream fout("output.txt");
    fin >> t;
    for(int q = 1; q <= t; q++){
        string s;
        fin >> s;
        reverse(s.begin(), s.end());
        while(true){
            for(int i = 0; i < s.length()-1; i++){
                if(s[i] < s[i+1]){
                    for(int j = 0; j <= i; j++)
                        s[j] = '9';
                    for(int j = i+1; j < s.length(); j++){
                        if(j == s.length()-1 && s[j] == '1'){
                            s.erase(s.length()-1);
                            break;
                        }
                        else if(s[j] == 0)
                            s[j] = '9';
                        else {
                            s[j]--;
                            break;
                        }
                    }
                    break;
                }
            }
//            cout << s << "\n";
            bool done = true;
            for(int i = 0; i < s.length()-1; i++){
                if(s[i] < s[i+1]){
                    done = false;
                    break;
                }
            }
            if(done)
                break;
        }
        reverse(s.begin(), s.end());
        fout << "Case #" << q << ": " << s << "\n";
    }
    return 0;
}
