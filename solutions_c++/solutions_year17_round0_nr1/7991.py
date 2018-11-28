#include <iostream>
#include <fstream>
#include <string.h>
#include <stdio.h>
using namespace std;
string s;
long int i,k,l,j,counter;
int flag,t,p;
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
        counter=0;
        flag=0;
        for(i=0;i<=(l-k);i++)
        {
            if(s.at(i)=='-')
            {
                counter++;
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
            flag=1;
      }
      if(flag==1)
        cout<<"Case #"<<p-t<<": IMPOSSIBLE"<<endl;
      else if(counter==0)
        cout<<"Case #"<<p-t<<": 0"<<endl;
      else if(counter>0)
        cout<<"Case #"<<p-t<<": "<<counter<<endl;
    }
    return 0;
}
