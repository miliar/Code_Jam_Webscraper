#include <vector>
#include <cstdio>
#include <iostream>
#include <math.h>
#include <string>

using namespace std;

int main(){
    freopen("blah.txt","w",stdout);
    int t, k;
    string s;
    cin>>t;
    for(int q = 1; q<=t; q++){
        cin>>s;
        cin>>k;
        int p = 0;
        int i;
        for(i = 0; i<s.size()-k; i++){
            if(s[i] == '-'){
                p++;
                for(int j = i; j<i+k;j++){
                    if(s[j] == '-'){
                        s[j] = '+';
                    }
                    else{
                        s[j] = '-';
                    } 
                }
            }
        }
        bool u = 0;
        if(s[i] == '-'){
            p++;
            for(; i<s.size(); i++){
                if(s[i] == '+'){
                    u = 1;
                    break;
                }
            }
        }
        else{
            for(; i<s.size(); i++){
                if(s[i] == '-'){
                    u = 1;
                    break;
                }
            }
        }
        if(!u){
            cout<<"Case #"<<q<<": "<<p<<endl;
        }
        else{
            cout<<"Case #"<<q<<": IMPOSSIBLE"<<endl;
        }
    }
    return 0;
}