//#include<iostream>
#include<bits/stdc++.h>

using namespace std ;
char S[2000];
void revert(int x,int K)
{ K--;
  while(K--)
   if(S[x]=='+')
      S[x++]='-';
   else
      S[x++]='+';
}
int main()
{ 
  int T,K,x,flag=0,z,m;
  cin>>T;
  for(m=1;m<T+1;m++)
  {  z=0;
     flag=0;
    cin>>S;
     cin>>K;
     
     for(x=0;S[x]!='\0';x++)
     { if(S[x]!='+')
          if(S[x+K-1]=='\0')
           { z=5;
             cout<<"Case #"<<m<<": "<<"IMPOSSIBLE\n";
             break;
           }
          else
            { S[x]='+';
             revert(x+1,K);
            // cout<<"   "<<S<<"  ";
             flag++;
            }
     }
     if(z!=5)
	 cout<<"Case #"<<m<<": "<<flag<<"\n";
  }
}
