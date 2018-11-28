#include <bits/stdc++.h>
using namespace std;
int T;

int main(){
   freopen("C-small-2-attempt0.in","r",stdin);
   freopen("output.txt","w",stdout);
   cin>>T;
   for(int t=1;t<=T;t++){
      int N,K;
      cin>>N>>K;
      priority_queue <int> q;
      q.push(N);
      for(int i=0;i<K-1;i++){
         int siz=q.top();
         q.pop();
         if(siz%2==1){
           q.push(siz/2);
           q.push(siz/2);
         }
         else{
           q.push(siz/2);
           q.push((siz/2)-1);
         }
      }
      int sol=q.top();
      if(sol%2==1){
           printf("Case #%d: %d %d\n",t,sol/2,sol/2);
         }
         else{
           printf("Case #%d: %d %d\n",t,sol/2,(sol/2)-1);
         }
    }
   return 0;
}
