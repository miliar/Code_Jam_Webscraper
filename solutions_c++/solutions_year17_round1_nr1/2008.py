#include <bits/stdc++.h>
#define ll long long int
#define pii pair<int,int>
#define d0(x) outp<<x<<" "
#define d1(x) outp<<x<<"\n"
#define d2(x,y) outp<<x<<" "<<y<<"\n"
#define d3(x,y,z) outp<<x<<" "<<y<<" "<<z<<"\n"
const ll mod=1e9+7;
using namespace std;
int main()
{
    ios_base::sync_with_stdio ( false );
	ifstream inp("input.txt");
	ofstream outp("output.txt");
	int t;inp>>t;//t=5;
    for(int test=1;test<=t;test++)
    {
           int R,C;inp>>R>>C;char a[R][C];int cnt[C];
           for(int i=0;i<C;i++)
           {
               cnt[i]=0;
           }
           for(int i=0;i<R;i++)
           {
               for(int j=0;j<C;j++)
               {
                   inp>>a[i][j];
                   if(a[i][j]!='?'){cnt[j]++;}
               }
           }
           for(int j=0;j<C;j++)
           {
                if(cnt[j]==0)
                {
                       continue;
                }
                for(int i=0;i<R;i++)
                {
                    if(a[i][j]=='?')
                    {
                          continue;
                    }
                    for(int k=i+1;k<R;k++)
                    {
                        if(a[k][j]!='?'){break;}
                        a[k][j]=a[i][j];cnt[j]++;
                    }
                    for(int k=i-1;k>=0;k--)
                    {
                        if(a[k][j]!='?'){break;}
                        a[k][j]=a[i][j];cnt[j]++;
                    }
                }
           }
           for(int j=0;j<C;j++)
           {
               //cout<<cnt[j];
           }
           //cout<<"\n";
           int cunt=0;
           for(int j=C-1;j>=0;j--)
           {
               if(cnt[j]!=R){continue;}
               //cout<<j<<" "<<cnt[j]<<"\n";
               for(int k=j-1;k>=0;k--)
               {
                   if(cnt[k]==R){break;}
                   //cout<<k<<"\n";
                   for(int i=0;i<R;i++)
                   {
                       a[i][k]=a[i][j];cnt[k]++;
                   }
               }
               for(int k=j+1;k<C;k++)
               {
                   if(cnt[k]==R){break;}
                   //cout<<k<<"\n";
                   for(int i=0;i<R;i++)
                   {
                       a[i][k]=a[i][j];cnt[k]++;
                   }
               }
           }
           outp<<"Case #"<<test<<":\n";
           //d3("Case #",test,":");
           for(int i=0;i<R;i++)
           {
               for(int j=0;j<C;j++)
               {
                   outp<<a[i][j];
                   if(a[i][j]=='?')
                   {
                       cout<<test<<" "<<cunt<<"\n";
                   }
               }
               outp<<"\n";
           }
    }
}
