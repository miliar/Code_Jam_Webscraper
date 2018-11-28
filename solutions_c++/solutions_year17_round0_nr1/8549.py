#include<iostream>
#include<fstream>
#include<string.h>
using namespace std;
int main()
{ int t;
 ifstream input;
    input.open("A-small-attempt0.in");
    ofstream output;
    output.open("codejam2.txt");


input>>t;int m=0;
while(t--)
{
    m++;
char s[1000];
input>>s;
int k,d=0;
input>>k;
int l,g=0,i,p=0;
l=strlen(s);
for(i=0;i<=l-k;i++)
{
if(s[i]=='-')
{int o=k,p=i;
while(o--)
{if(s[p]=='+')
s[p]='-';
else
    s[p]='+';
p++;}
g++;

}

}
for(i=0;i<l;i++)
{
    if(s[i]=='-')
        { output<<"Case #"<<m<<": IMPOSSIBLE"<<endl;break;}
    else
        d++;
}
if(d==l)
    output<<"Case #"<<m<<": "<<g<<endl;

}

}
