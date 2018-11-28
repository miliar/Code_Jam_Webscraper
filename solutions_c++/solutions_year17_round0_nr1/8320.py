#include<stdio.h>
#include<string.h>
#include<iostream>
#include<fstream>
using namespace std;
int main()
{
 ifstream input;
 input.open("A-small-attempt0.in");
 ofstream output;
 output.open("codejam3.txt");
 int t,z=0;
 input>>t;
 while(t--)
 {
     z++;
     int k,i,j,c=0,d=0,p;
     char s[1000];
     input>>s;
     input>>k;
     p=strlen(s);
     for(i=0;i<p;i++)
     {
        if(s[i]=='-')
      {
        for(j=i;j<i+k;j++)
        {
            if((i+k)>p)
                {
                    d++;
                    break;
                }
            else if(s[j]=='-')
                s[j]='+';
            else if(s[j]=='+')
                s[j]='-';
        }
        c++;
      }
      //cout<<c <<s<<endl;
     }
     if(d==0)
        output<<"case #"<<z<<": "<<c<<endl;
     else
        output<<"case #"<<z<<": IMPOSSIBLE"<<endl;
 }
}
