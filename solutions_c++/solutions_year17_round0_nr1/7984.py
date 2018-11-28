#include <iostream>
#include <fstream>
#include <string.h>
#include <stdio.h>
using namespace std;
string s;
long int i,k,l,j,c;
int f,t,p;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.in","w",stdout);
    cin>>t;
    p=t;
    while(t--)
    {   cin>>s;
        scanf("%lu",&k);
        l=s.size();
        c=0;
        f=0;
        for(i=0;i<=(l-k);i++)
        {
            if(s.at(i)=='-')
            {
                c++;
                for(j=i+1;(j<i+k)&&(j<l);j++)
                {
                    if (s.at(j)=='-')
                        s.at(j)='+';
                    else
                        s.at(j)='-';
                }
            }
        }
      for(i=(l-k)+1;i<l;i++)
      {
          if(s.at(i)=='-')
            f=1;
      }
      if(f==1)
        cout<<"Case #"<<p-t<<": IMPOSSIBLE"<<endl;
      else if(c==0)
        cout<<"Case #"<<p-t<<": 0"<<endl;
      else if(c>0)
        cout<<"Case #"<<p-t<<": "<<c<<endl;
    }
    return 0;
}
