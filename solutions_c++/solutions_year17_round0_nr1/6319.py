#include<iostream>
#include<stdlib.h>
#include<string.h>

using namespace std;
void change(char*s,int k)
{
for(int i=0;i<k;i++)
s[i]=s[i]=='-'?'+':'-';
}

int main()
{
int t;
cin>>t;
int k;
for(int i=0;i<t;i++)
{char *s=(char*)calloc(sizeof(char),1004);
int count=0;
cin>>s;
cin>>k;int x=strlen(s);int j=0;
for(;j<x-k+1;j++)
if(s[j]=='-'){change(s+j,k);count++;}
//if(strchr(s,'-')!=NULL){change(s+j-1,k);count++;}
int flag=0;
while(j<x)
{if(s[j]=='-')
flag=1;
j++;}
if(flag==1)cout<<"Case "<<"#"<<i+1<<": "<<"IMPOSSIBLE";
else cout<<"Case "<<"#"<<i+1<<": "<<count;
free(s);
}

}

