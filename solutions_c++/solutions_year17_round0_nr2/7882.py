#include <bits/stdc++.h>
using namespace std;
int main(){
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    string n;
    cin>>t;
    for(int i=1;i<=t;++i){
        cin>>n;
        if(n.length()>1){
            for(int i=0;i<n.length()-1;++i){
                if(n[i]>n[i+1]){
                    for(int j=i+1;j<n.length();++j){
                        n[j]='9';
                    }
                    (int)n[i]--;i=-1;
                }
            }
        }
        cout<<"Case #"<<i<<": ";
        bool aux=true;
        for(int i=0;i<n.length();++i){
            if(n[i]=='0' && aux){aux=false;}
            else{cout<<n[i];}
        }
        cout<<endl;
    }
    return 0;
}
