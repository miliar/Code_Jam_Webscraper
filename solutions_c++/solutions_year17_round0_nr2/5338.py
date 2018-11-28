#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<cstring>
using namespace std;

int i,j,k,f[20],l,t,flag,e,r;
string n[110];

int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    cin>>r;
    for(e=0;e<r;e++)
        cin>>n[e];
    for(e=0;e<r;e++){
        for(i=0;i<20;i++)f[i]=0;
        for(i=0;i<n[e].length();i++)f[i]=n[e][n[e].length()-1-i]-'0';
        
    while(true){
        l=n[e].length();
        while(f[l]==0){
            l--;
        }
        l++;
        
        
        flag=0;
        for(i=1;i<l;i++){
            if(f[i-1]<f[i]){flag=1;break;}
        }
        if (flag==0){cout<<"Case #"<<e+1<<": ";for(i=0;i<l;i++)cout<<f[l-1-i];cout<<endl;break;}
        f[i]=f[i]-1;
        for(j=0;j<i;j++)f[j]=9;
}}
     
    return 0;
}
