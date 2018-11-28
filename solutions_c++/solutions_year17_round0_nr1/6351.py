#include<iostream>
#include<algorithm>
#include<fstream>
#include<vector>
#include<sstream>
#include<string>
#include<algorithm>
using namespace std;


int main()
{
bool flag;
string input="";
ifstream it;
ofstream ot;
it.open("input.in");
ot.open("output.out");
long int j,t,i,k,n,min,count,len;
string str;
it>>t;
for(k=1;k<=t;k++)
{
    it>>str>>n;
    count=0;
    len=str.length();
    for(i=0;i<len-n+1;i++)
    {
        if(str[i]=='-')
        {
            for(j=i;j<i+n;j++)
                str[j]=(str[j]=='+'?'-':'+');
            count++;
        }
    }
    for(i=len-n;i<len;i++)
        if(str[i]=='-')
            {count=-1;break;}
    
   // cout<<str<<"\n";
    if(count==-1)
        ot<<"Case #"<<k<<": "<<"IMPOSSIBLE"<<"\n";        
    else
        ot<<"Case #"<<k<<": "<<count<<"\n";
}// tst case
it.close();
ot.close();
return 0;
}
