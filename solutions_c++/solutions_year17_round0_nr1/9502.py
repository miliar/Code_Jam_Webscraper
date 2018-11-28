#include <iostream>
#include <stdio.h>

using namespace std;

int main(){
    int t,res;
    cin >> t;
    for(int ti=1; ti<=t; ti++){
        string s;
        cin >> s;
        int n = s.size();
        int k;
        res=0;
        cin >> k;
        for(int i=0; i<=n-k; i++){
            if(s[i]=='-'){
                for(int j=i; j<i+k; j++){
                    if(s[j]=='+')s[j]='-';
                    else s[j]='+';
                }
                res++;
            }
        }
        bool imp=0;
        for(int i=0; i<n; i++){
            if(s[i]=='-'){imp=1;break;}
        }
        if(imp){
            cout << "Case #"<<ti<<": IMPOSSIBLE"<<endl;
        } else {
            cout << "Case #"<<ti<<": " << res<<endl;
        }
    }
    return 0;
}
