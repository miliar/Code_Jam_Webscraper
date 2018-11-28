#include <bits/stdc++.h>
using namespace std;
 
int main(){
int t;
cin>>t;
for(int a=1; a<=t; a++){
    string str;
    int k;
    int count = 0;
    bool flag = false;
    cin>>str;
    cin>>k;
    for(int i=0; i<str.length(); i++)
    {
        if(str[i] == '-'){
            if((i+k) <= str.length()){
                count++;
 
                for(int j=i ; j<i+k; j++){
                    if(str[j] == '+') str[j] = '-';
                    else str[j] = '+';
                }
            }
            else{
                flag = true;
                break;
            }
        }
    }
 
    if(flag)
        cout<<"Case #"<<a<<": IMPOSSIBLE"<<endl;
    else
        cout<<"Case #"<<a<<": "<<count<<endl;
}
 
}