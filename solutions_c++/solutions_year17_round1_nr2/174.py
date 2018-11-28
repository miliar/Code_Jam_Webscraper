#include<iostream>
#include<cmath>
#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;

int t;
int n,p;

int r[111];
int g[111][111];

int ii[111];
int ans;

int ff[111][111];
int tt[111][111];


int main()
{
    int i,j,k,times;
    freopen("B-large.in","r",stdin);
    freopen("ans.out","w",stdout);
    
    cin>>t;
    for(times=1;times<=t;times++)
    {
         cin>>n>>p;
         for(i=1;i<=n;i++)
         {
             cin>>r[i];
         }
         
         for(i=1;i<=n;i++)
         {
             for(j=1;j<=p;j++)
             {
                 cin>>g[i][j];
             }
             sort(g[i]+1,g[i]+p+1);
         }
         /*
         for(i=1;i<=n;i++)
         {
             for(j=1;j<=p;j++)
             {
                 cout<<g[i][j]<<' ';
             }
             cout<<endl;
         }
         */
         for(i=1;i<=n;i++)
         {
              for(j=1;j<=p;j++)
              {
                  
                  double tmp=g[i][j];
                  tmp=tmp/0.9*1.0;
                  int d=(int)floor(tmp+1e-9);
                  tt[i][j]=d;
                  
                  tmp=g[i][j];
                  tmp=tmp/1.1*1.0;
                  d=(int)ceil(tmp-1e-9);
                  ff[i][j]=d;
                  
                  d=ff[i][j]/r[i];
                  if(ff[i][j]%r[i]!=0)
                  {
                      d++;
                  }
                  ff[i][j]=d;
                  
                  
                  d=tt[i][j]/r[i];
                  tt[i][j]=d;
                  
                  //cout<<ff[i][j]<<' '<<tt[i][j]<<"    ";
              }
              //cout<<endl;
         }
         
         /*
         for(i=1;i<=n;i++)
         {
             for(j=1;j<=p;j++)
             {
                 cout<<ff[i][j]<<' '<<tt[i][j]<<"    ";
             }
             cout<<endl;
         }
         */
         
         for(i=1;i<=n;i++)
         {
             ii[i]=1;
         }
         ans=0;
         
         while(1)
         {
              int from,to;
              from=ff[1][ii[1]];
              to=tt[1][ii[1]];
              for(i=1;i<=n;i++)
              {
                  from=max(from,ff[i][ii[i]]);
                  to=min(to,tt[i][ii[i]]);
              }
              
              if(from<=to)
              {
                  ans++;
                  for(i=1;i<=n;i++)
                  {
                      ii[i]++;
                  }
              }
              else
              {
                  int mm=1;
                  for(i=1;i<=n;i++)
                  {
                      if(tt[i][ii[i]]<tt[mm][ii[mm]])
                      {
                          mm=i;
                      }
                  }
                  
                  ii[mm]++;
              }
              
              for(i=1;i<=n;i++)
              {
                  if(ii[i]>p)break;
              }
              if(i<=n)break;
         }
         cout<<"Case #"<<times<<": "<<ans<<endl;
    }
    
    
    
    return 0;
}
