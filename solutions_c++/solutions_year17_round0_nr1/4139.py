#include <iostream>
#include <string>
#include <cstring>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <sstream>
using namespace std;

int main(){

    freopen("A-large.in","r",stdin);
    freopen("d.out","w",stdout);

    int t;
    string s;
    int k;
    cin>>t;
    int j,num;
    bool flag;
    for(int i = 1; i <= t; i++){
        cin>>s>>k;
        j =0;
        num =0;
        while(j <= s.length() - k){
            if(s[j] == '-'){
                num++;
                for(int l = 0; l < k; l++){
                    if(s[j+l] == '-')
                        s[j+l] = '+';
                    else
                        s[j+l] = '-';
                }
            }
            j++;
        }
        flag = true;
        while(j < s.length()){
            if(s[j] == '-')
                flag = false;
            j++;
        }
        if(flag){
            cout<<"Case #"<<i<<": "<<num<<endl;
        }
        else{
            cout<<"Case #"<<i<<": "<<"IMPOSSIBLE"<<endl;
        }
    }
    return 0;
}
