#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <fstream>
#define lli long long int
#define MAX 100
#define li long int
using namespace std;

int main ()
{
    ifstream input;
    input.open("input.in");
    ofstream output;
    output.open("output.txt");

     int t;
    input>>t;
    for(int tttt=1;tttt<=t;tttt++)
    {
        string s;
        input>>s;
        int k;
        input>>k;
        int count=0;
        int flag2=0;
        for(int i=0;i<=s.length()-k;i++)
        {
          if(s[i]=='-')
          {

              for(int j=i;j<=k+i-1;j++)
              {
                  if(s[j]=='-')
                s[j]='+';
                else if(s[j]=='+')
                    s[j]='-';
              }
              count++;

          }
        }
        int flag1=0;
        for(int i=0;i<s.length();i++)
        {
            if(s[i]=='-')
            {
                output<<"Case #" <<tttt<< ": "<<"IMPOSSIBLE"<<endl;
                flag1=1;

            break;
            }
            else continue;
        }
        if(flag1==0)
           output<<"Case #" <<tttt<< ": "<<count<<endl;

    }
    return 0;
}
