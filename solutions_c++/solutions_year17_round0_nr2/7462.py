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
int count1 = 0;
int k;

ifstream fin("B-large.in");
ofstream fout("output.txt");

int main() {
    fin>>k;
    for(int x = 0; x<k; x++){
        fin>>s;
        count1++;
        for(int z = 0; z<s.size(); z++){
            for(int x = 0; x+1<s.size(); x++){
                int a = (int)(s[x]-'0');
                int b = (int)(s[x+1]-'0');
                if(a>b){
                    a--;
                    char temp = (char)(a+'0');
                    s[x] = temp;
                    for(int y = x+1; y<s.size(); y++){
                        s[y] = '9';
                    }
                }
            }
        }
        ans = "";
        check = false;
        for(int k = 0; k<s.size(); k++){
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
