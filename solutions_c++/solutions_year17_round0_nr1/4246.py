#include <bits/stdc++.h>
using namespace std;
int T,K,sol;
string S;
bool ok;
int turn[2000];

char f(char s,int temp){
  if(temp%2==0 && s=='-') return '-';
  if(temp%2==1 && s=='+') return '-';
  return '+';
}

int main(){
   freopen("A-large.in","r",stdin);
   freopen("output.txt","w",stdout);
   cin>>T;
   for(int t=1;t<=T;t++){
     memset(turn,0,sizeof turn);
     int temp=0;
     sol=0;
     ok=true;
     cin>>S>>K;

     for(int i=0;i<=S.length()-K;i++){
       temp+=turn[i];
       if(f(S[i],temp)=='-'){
         sol++;
         temp++;
         turn[i+K]--;
       }
     }
     for(int i=S.length()-K+1;i<S.length();i++){
       temp+=turn[i];
       if(f(S[i],temp)=='-'){ok=false;}
     }

     if(ok) printf("Case #%d: %d\n",t,sol);
     else printf("Case #%d: IMPOSSIBLE\n",t,sol);
   }
   return 0;
}
