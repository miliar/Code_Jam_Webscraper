#include <bits/stdc++.h>
using namespace std;
int T,D,N;
double sol;

int main(){
   freopen("A-large.in","r",stdin);
   freopen("output.txt","w",stdout);
   cin>>T;
   for(int t=0;t<T;t++){
      cin>>D>>N;
      double tMax=0,k,s;
      for(int i=0;i<N;i++){
        cin>>k>>s;
        tMax=max(tMax,((double)D-k)/s);
      }
      sol=(double)D/(double)tMax;
      printf("Case #%d: %.6f \n",t+1,sol);
   }
   return 0;
}
