#include <bits/stdc++.h>
using namespace std;
char s[1100];
int main(){
//freopen("test","r",stdin);
int i,j,k,n,m,T,K;
scanf("%d",&T);
for(int cas=1;cas<=T;cas++){
scanf("%s",s);
m=strlen(s);
for(i=m-1;i>0;i--)
if(s[i]<s[i-1]){
for(j=i;j<m;j++)
s[j]='9';
for(j=i-1;j>=0;j--)
if(s[j]!='0'){
s[j]--;
break;
}
else
s[j]='9';
}
printf("Case #%d: ",cas);
for(i=0;i<m;i++)
if(s[i]!='0')break;
while(i<m)
putchar(s[i++]);
putchar('\n');
}
return 0;
}
