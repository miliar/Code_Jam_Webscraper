//
//  main.cpp
//  CodeJam Qual 2
//
//  Created by Jeong Yang on 4/8/17.
//  Copyright © 2017 Jonathan Yang. All rights reserved.
//

#include <iostream>
#include <fstream>
using namespace std;
string s, ans = "";
bool check;
long long count1 = 0;
long long k;

ifstream fin("B-large.in");
ofstream fout("output.txt");

int main() {
    fin>>k;
    for(long long x = 0; x<k; x++){
        fin>>s;
        count1++;
        for(long long z = 0; z<s.size(); z++){
            for(long long x = 0; x+1<s.size(); x++){
                long long a = (long long)(s[x]-'0');
                long long b = (long long)(s[x+1]-'0');
                if(a>b){
                    a--;
                    char temp = (char)(a+'0');
                    s[x] = temp;
                    for(long long y = x+1; y<s.size(); y++){
                        s[y] = '9';
                    }
                }
            }
        }
        ans = "";
        check = false;
        for(long long k = 0; k<s.size(); k++){
            if(s[k] != '0'){
                check = true;
            }
            if(check){
                ans+=s[k];
            }
        }
        if(!check){
            ans="0";
        }
        fout<<"Case #"<<count1<<": "<<ans<<endl;
    }
}
