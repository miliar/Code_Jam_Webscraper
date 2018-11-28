#include <bits/stdc++.h>
using namespace std;
int main(){
    ofstream out;
    out.open("output");
    int t;
    cin>>t;
    for(int z=1;z<=t;z++){
        int cont=0;
        string s;
        int n;
        cin>>s>>n;
        int l=int(s.length());
        for(int i=0;i<=l-n;i++){
            if(s[i]=='+'){
                continue;
            }else{
                cont++;
                for(int j=i;j<i+n;j++){
                    if(s[j]=='+'){
                        s[j]='-';
                    }else{
                        s[j]='+';
                    }
                }
            }
        }
        int f=0;
        for(int i=l-n+1;i<l;i++){
            if(s[i]=='-'){
                f=1;
                break;
            }
        }
        out<<"Case #"<<z<<": ";
        if(f==0){
            out<<cont<<endl;
        }else{
            out<<"IMPOSSIBLE"<<endl;
        }
    }
    out.close();
    return 0;
}