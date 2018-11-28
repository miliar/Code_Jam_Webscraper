#include<stdio.h>
#include<string.h>
#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    ifstream input;
    input.open("B-large.in");
    ofstream output;
    output.open("codejam1.txt");
    int t,z=0;
    input>>t;
    while(t--)
  {
      z++;
    int n,p=0,i;
    char a[20],b[20];
    input>>a;
    p=strlen(a);
   // printf("%d\n",p);
    for(n=p-1;n>0;n--)
    {
        if(a[n]<a[n-1])
        {
           a[n-1]=a[n-1]-1;
           for(i=n;i<p;i++)
            a[i]='9';
        }
    }
    if(a[0]=='0')
    {
        for(i=0;i<p-1;i++)
        b[i]=a[i+1];
        b[p-1]='\0';
    }
    else
    {
        for(i=0;i<p;i++)
        b[i]=a[i];
        b[p]='\0';
    }
    output<<"Case #"<<z<<": "<<b<<endl;
  }
}
