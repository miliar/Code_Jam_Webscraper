#include <bits/stdc++.h>
using namespace std;
char s[1100];
int main(){
//freopen("test","r",stdin);
int i,j,k,n,m,T,K;
scanf("%d",&T);
for(int cas=1;cas<=T;cas++){
scanf("%s%d",s,&K);
n=0;
m=strlen(s);
bool flg=false;
for(i=0;i<m;i++){
if(s[i]=='+')continue;
n++;
if(i+K<=m){
for(j=i;j<i+K;j++)
if(s[j]=='-')s[j]='+';
else s[j]='-';
}
else flg=true;
}
if(!flg)
for(i=0;i<m;i++)
if(s[i]=='-')flg=false;
if(flg)printf("Case #%d: IMPOSSIBLE\n",cas);
else printf("Case #%d: %d\n",cas,n);
}
return 0;
}
