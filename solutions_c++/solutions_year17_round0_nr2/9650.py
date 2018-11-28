#include<iostream>
#include<stdio.h>
#include<string.h>
#include<fstream>
#include<cmath>
using namespace std;
int main()
{
ifstream input;
input.open("a.in");
ofstream output;
output.open("codejam.txt");
    int t;
    input>>t;
    for(int q=1;q<=t;q++)
    {
      char a[19];int count =1;char b[19];
      input>>a;
      int p=strlen(a);
for(int k=0;count!=0;k++){
        count =0;
   for(int i=0;a[i]!='\0'&&i<p-1;i++)
         {
             if(a[i]>a[i+1])
            {
                count++;
            }
         }
            if(count>0)


            {



                  for(int i=0;a[i]!='\0'&&i<p-1;i++)
         {
             if(a[i]>a[i+1])
            {
                a[i]=a[i]-1;


                for(int j=i+1;a[j]!='\0'&&j<p;j++)
                {
                    a[j]='9';
                }

            }
         }
            }

    }

    if(a[0]=='0')
    {
                         for(int i=0;a[i]!='\0'&&i<p-1;i++)
                            b[i]=a[i+1];
                            b[p-1]='\0';
    }
    else{
                          for(int i=0;a[i]!='\0'&&i<p;i++)
                                                        b[i]=a[i];
                                                        b[p]='\0';
    }
    output<<"Case #"<<q<<": "<<b<<"\n";
    }

    return 0;
}


