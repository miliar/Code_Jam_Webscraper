#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<cstring>
using namespace std;

int i,j,k[110],flag,result=0,f[1010],r,e;
string s[110];
int main(){
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    cin>>r;
    for (e=0;e<r;e++)
        cin>>s[e]>>k[e];
    for (e=0;e<r;e++){
    flag=0;
    result=0;
    for(j=0;j<1001;j++){
        f[j]=0;
    }
    for(j=0;j<s[e].length();j++){
        if(s[e][j]=='-')f[j]=0;
        else f[j]=1;
    }
    i=0;
    while(i<=s[e].length()-k[e]){
        if(f[i]==0){
            for(j=0;j<k[e];j++){
                if(f[j+i]==0)f[j+i]=1;
                else f[j+i]=0;
            }
            result++;
        }
        i++;
    }
    for(j=0;j<s[e].length();j++){
        if(f[j]==0){flag=1;break;}
    }
    if(flag==1)cout<<"Case #"<<e+1<<": "<<"IMPOSSIBLE"<<endl;
    else cout<<"Case #"<<e+1<<": "<<result<<endl;
    }
   
    return 0;
} 
