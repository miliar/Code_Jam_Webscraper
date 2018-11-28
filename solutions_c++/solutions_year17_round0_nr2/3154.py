#include <bits/stdc++.h>
using namespace std;
int main(){
    ofstream out;
    out.open("output");
    int t;
    cin>>t;
    for(int z=1;z<=t;z++){
        out<<"Case #"<<z<<": ";
        string n;
        cin>>n;
        reverse(n.begin(),n.end());
        int l=(int)(n.length());
        for(int i=1;i<l;i++){
            if(n[i]<=n[i-1]){
                continue;
            }else{
                for(int j=0;j<i;j++){
                    n[j]='9';
                }
                n[i]=(char)(n[i]-1);
            }
        }
        reverse(n.begin(),n.end());
        out<<stoll(n)<<endl;
    }
    out.close();
    return 0;
}