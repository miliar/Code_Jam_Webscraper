//
//  main.cpp
//  Tidy Numbers
//
//  Created by Gellért Peresztegi- Nagy on 2017. 04. 08..
//  Copyright © 2017. Gellért Peresztegi- Nagy. All rights reserved.
//

#include <iostream>
#include <string>
using namespace std;

char max(char a, char b){
    return a > b ? a : b;
}

int main(int argc, const char * argv[]) {
    int n;
    cin>>n;
    string s;
    
    
    int l;
    for(int t = 1; t <= n; t++){
        cin>>s;
        l = s.length();
        for(int i = l-1; i > 0; i--){
            if(s[i] < s[i-1]){
                s[i-1]--;
                s[i] = '9';
                for(int j = i; j < l; j++){
                    s[j] = '9';
                }
                
                //cout<<s<<"\n";
            }
        }
        if(s[0] == '0' && l != 1) s = s.substr(1,l);
        cout<<"Case #"<<t<<": "<<s<<"\n";
    }
    return 0;
}


/*
4
132
1000
7
111111111111111110

*/
