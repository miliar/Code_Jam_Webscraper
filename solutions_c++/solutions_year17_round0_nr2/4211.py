#include <bits/stdc++.h>
using namespace std;
int T,nine;
string S;
int num[30];


int f(int i){
  if(i<0) return 0;
  if(num[i+1]<num[i]){
      num[i]--;
      nine=i+1;
    }
  f(i-1);
}

int main(){
   freopen("B-large.in","r",stdin);
   freopen("output.txt","w",stdout);
   cin>>T;
   for(int t=1;t<=T;t++){
     memset(num,0,sizeof num);
     nine=999;
     cin>>S;
     for(int i=0;i<S.length();i++)
       num[i]=(int)(S[i]-'0');
     f(S.length()-2);



     bool primo=true;
     printf("Case #%d: ",t);
     for(int i=0;i<S.length();i++)
       if((!primo && num[i]==0) || num[i]!=0 || i>=nine)
       {
         primo=false;
         if(i<nine)
           printf("%d",num[i]);
         else printf("%d",9);
        }

     printf("\n");
   }
   return 0;
}
