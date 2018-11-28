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
string input="";
ifstream it;
ofstream ot;
it.open("input.in");
ot.open("output.out");
long int j,t,i,k,n,p,temp;
string str;
bool flag;
it>>t;
for(k=1;k<=t;k++)
{
    it>>str;
    flag=true;
    n=str.length();
    for(i=n-1;i>=1;i--)
    {
        while(str[i]<str[i-1] || str[i]=='0')
        {
            str[i]=str[i]-1;
            if(str[i]<='0')
            {
                for(p=i;p<n;p++)
                    str[p]='9';
                if(i-1>=0)
                    str[i-1]=str[i-1]-1;
            }    
        }//while
    }
    ot<<"Case #"<<k<<": ";
    for(i=0;i<str.length();i++)
        if(!(i==0 && str[i]=='0'))
            ot<<str[i];
    ot<<"\n";
}// tst case
it.close();
ot.close();
return 0;
}
