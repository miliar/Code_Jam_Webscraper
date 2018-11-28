#include<iostream>
#include<cstring>
using namespace std;
int main()
{
    int T,N,K,i,j,flag1=1,x=0,y;
    char S[1001];
    cin>>T;
    while(T--)
    {
              x++;
              y=0;
              flag1=1;
              cin>>S; 
              cin>>K;
              N=strlen(S);
              for(i=0;i<=(N-K);i++)
              {
                              if(S[i]=='-')
                              {
                                           y++;
                                           for(j=i;j<(i+K);j++)
                                           {
                                                               if(S[j]=='+') S[j]='-';
                                                               else S[j]='+';
                                           } 
                              }
              }
              for(i=0;i<N;i++)
              { 
                              if(S[i]=='-')
                              {flag1=0;break;}
              }
              if(flag1==0)
              cout<<"Case #"<<x<<": "<<"IMPOSSIBLE"<<endl;
              else cout<<"Case #"<<x<<": "<<y<<endl;
    }
    return 0;
}
