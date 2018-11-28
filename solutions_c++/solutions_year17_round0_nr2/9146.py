#include<bits/stdc++.h>
using namespace std;
int main()
{
long long int t,i,j,k,x;
int count=0;
char c[19];
cin>>t;
for(i=1;i<=t;i++)
  {  count=0;
      int m=0;
      cin>>c;
    cout<<"Case #"<<i<<": ";
    unsigned int d=strlen(c);
    unsigned int u=d-2;
    if(d==1)
       {cout<<c<<endl;count=1;m=1;}
    else if((c[1]=='0') && (c[0]=='1') )
           {
            for(k=1;k<=d-1;k++)
                cout<<"9";
             cout<<endl;m=1;
             count=1;
            }
    else if(c[1]=='0')
           { cout<<((c[0]-'0')-1);
             for(k=1;k<=d-1;k++)
                  cout<<"9";
             cout<<endl;m=1;
             count=1;
           }
    if(count!=1)
     {for(j=0;(j<=u) && (j>=0);j++)
      {
         if(c[j]>c[j+1])
           {
               c[j]=('0'+((c[j]-'0')-1));
             for(k=j+1;k<=d-1;k++)
                c[k]='0'+9;
               u=j;
               j=j-2;
           }
     }
     if(m!=1 && c[0]!='0')
        {cout<<c<<endl;}
      else if(m!=1 && c[0]=='0')
        { for(x=1;x<=d-1;x++)
             cout<<c[x];
             cout<<endl;
        }
     }
  }
  return 0;

}
