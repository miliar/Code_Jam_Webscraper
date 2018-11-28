#include <bits/stdc++.h>
using namespace std;
int main(){
int N,D,i,j,K,t,T,S;
scanf("%d",&T);
for(t=1;t<=T;t++){
scanf("%d%d",&D,&N);
long double maxS=0;
long double d=1;
for(i=0;i<N;i++){
scanf("%d%d",&K,&S);
maxS=max(maxS,d*(D-K)/S);
}
printf("Case #%d: %Lf\n",t,D/maxS);
}
return 0;
}
