#include<iostream>
#include<fstream>
#include<cmath>
#include<stdio.h>
#include<string.h>
using namespace std;
int main()
{
    ifstream input;
    input.open("A-large.in");
    ofstream output;
    output.open("codejam.txt");
    int t;
    input>>t;
    for(int q=1;q<=t;q++)
    {
      char a[1005]; int k;int count= 0,count1=0;
      input>>a>>k;
    int p =strlen(a);
      for(int i=0;i<=p-k;i++)
      {
          if(a[i]=='-')
          {
          	a[i]='+';
             for(int j=1;j<k;j++)
             {
             	if(a[i+j]=='+')
             	a[i+j]='-';
             	else
             	a[i+j]='+';
             }
             count++;

          }
          else
          {
              continue;
          }


      }
      for(int i=0;i<p;i++)
      {
      	if(a[i]=='-')
      	{
      		count1++;
      		break;
      	}
      }


if(count1>0)
output<<"Case #"<<q<<": "<<"IMPOSSIBLE\n";
else if(count>0)
output<<"Case #"<<q<<": "<<count<<endl;
else
output<<"Case #"<<q<<": "<<"0\n";
    }
    return 0;
}
