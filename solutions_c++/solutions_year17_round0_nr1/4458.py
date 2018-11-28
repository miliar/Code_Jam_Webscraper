//
//  main.cpp
//  test
//
//  Created by pzmrzy on 08/04/2017.
//  Copyright © 2017 pzmrzy. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int main(int argc, const char * argv[]) {
    ifstream fin;
    ofstream fout;
    fin.open("/Users/pzmrzy/Desktop/test/test/A-large.in");
    fout.open("/Users/pzmrzy/Desktop/test/test/A_output.txt");
    int T, K;
    string s;
    fin >> T;
    for (int t=0; t<T; t++){
        fin >> s >> K;
        int res = 0;
        for (int i =0; i<s.length()-K+1; i++){
            if (s[i] == '+'){
                continue;
            }else{
                res += 1;
                for (int j=i; j<i+K; j++){
                    if (s[j] == '+'){
                        s[j] = '-';
                    }else{
                        s[j] = '+';
                    }
                }
            }
        }
        bool flag = true;
        for (int i=0; i<s.length(); i++){
            if (s[i] == '-'){
                flag = false;
                break;
            }
        }
        if (flag){
            fout << "Case #" << t + 1 << ": " << res << endl;
        }else{
            fout << "Case #" << t + 1 << ": " << "IMPOSSIBLE" << endl;
        }
        
    }
    fout.close();
    fin.close();
    
    return 0;
}
