#include "bits/stdc++.h"
#define ll long long
using namespace std;
int test;
string d;
int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    scanf("%d",&test);
    for(int l=1;l<=test;l++){
        cin>>d;
        int idx=-1,temp,val;
        for(int i=0;i<d.length()-1;i++){
            if(d[i]>d[i+1]){
                idx=i,temp=d[idx]; break;
            }
        }
        cout<<"Case #"<<l<<": ";
        if(idx==-1){
            cout<<d<<'\n'; continue;
        }
        for(;d[idx]==temp&&idx>=0;idx--) d[idx]--;
        idx++;
        for(int i=idx+1;i<d.length();i++) d[i]='9';
        int i=0;
        while(d[i]=='0'&&i<d.length()) i++;
        for(;i<d.length();i++) cout<<(char)d[i];
        cout<<'\n';
    }
}
