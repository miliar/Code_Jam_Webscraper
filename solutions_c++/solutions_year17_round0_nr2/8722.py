#include <iostream>
#include <string>
#include<fstream>
using namespace std;

int main()
{
    ifstream fin;
    ofstream fout;
    fin.open("smallin.txt");
    fout.open("smallout.txt");
    int t,x=1;

    fin>>t;
    while(x<=t)
    {
       string n,s;
       fin>>n;
       int i,len,digit1,digit2,flag=0;
       len=n.length();
       for(i=0;i<len-1;i++)
       {
           digit1=n[i]-48;
           digit2=n[i+1]-48;
           if(digit1<=digit2)
                s=s+n[i];
           else
           {
               flag=1;
               if(digit1 != 1)
               {
                   --digit1;char di=digit1+48;
                   s=s+di;int j;
                   int k=i;int fl=0;
                   for(j=i;j>=1;j--)
                   {
                       if(s[j]<s[j-1])
                       {
                           fl=1;
                           di=s[j-1];--di;
                           s[j-1]=di;
                       }
                    }
                   //cout<<s<<endl;
                   if(fl==1 )
                    s[k]='9';

                   for(j=i+1;j<len;j++)
                   {s=s+'9';}
                   break;
               }
               else if(digit1 == 1)
               {
                   s.clear();int j;
                   for(j=0;j<len-1;j++)
                   {s=s+'9';}
                   break;
               }
           }
       }
       if(flag==0)
        s=s+n[len-1];

       if(x !=t)
       {fout<<"Case #"<<x<<": "<<s<<endl;}
       else
        {fout<<"Case #"<<x<<": "<<s;}

       ++x;
    }
    return 0;
}
