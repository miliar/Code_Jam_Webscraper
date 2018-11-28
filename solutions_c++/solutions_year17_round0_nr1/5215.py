//
//  main.cpp
//  codejam
//
//  Created by Twinkle Gupta on 4/7/17.
//  Copyright © 2017 Twinkle Gupta. All rights reserved.
//

#include <iostream>
#include<bitset>
#include<string>
using namespace std;

void flip(string& a, int pos, int times){
    int n = a.length();
    if(pos + times > n) return ;
    for(int i = pos; i-pos < times && a[i] != '\0'; i++)
    {
        if(a[i] == '0') a[i] = '1';
        else a[i] = '0';
    }
}

bool allzero(string s){
  
    for(int i = 0; s[i] != '\0'; i++)
    {
        if(s[i] == '1') return false;
    }
    return true;
}
int main() {
    //freopen("A-small-attempt0.in","r",stdin);
    //freopen("A_small_out.txt","w",stdout);
    int t;
    cin>>t;
    for(int i = 1; i<= t; i++){
        string s;
        int k;
        cin>> s >> k;
        //cout<<s<<" "<<k;
        for(int j = 0; s[j] != '\0'; j++){
            if(s[j] == '+') s[j] = '0';
            else s[j] = '1';
        }
        
        int n = s.length();
        int count = 0;
        int j;
        for(j = 0; s[j] != '\0';j++){
            if(s[j] == '1'){
                flip(s,j,k);
                count++;

            }
            //cout<<"flipped : "<<s<<endl;
            if(allzero(s)) break;
        }
        if(allzero(s) == false) cout<<"Case #"<<i<<": IMPOSSIBLE\n";
        else cout<<"Case #"<<i<<": "<<count<<"\n";


     
    }
    
    return 0;
}
