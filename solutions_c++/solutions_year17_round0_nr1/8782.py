#include<iostream>
#include<stdio.h>
#include<string.h>

using namespace std;

int main(){

freopen("A-large.in","r",stdin);
freopen("outpp.txt","w",stdout);
char s[1001];
int k;
int test;
cin>>test;

for(int p=1;p<=test;p++){
    cin>>s>>k;
    int co = 0;
    bool possible = true;
    for(int i=0;i<strlen(s)-k+1;i++){
        if(s[i]=='-'){
            for(int j=0;j<k;j++) s[i+j]=(s[i+j]=='+')?'-':'+';
            co++;
            }
        }
    for(int j=strlen(s)-1;j>strlen(s)-k;j--)
        if(s[j]=='-') possible=false;
    cout<<"Case #"<<p<<": ";
    if(possible) cout<<co<<"\n";
    else cout<<"IMPOSSIBLE\n";
    }
}
