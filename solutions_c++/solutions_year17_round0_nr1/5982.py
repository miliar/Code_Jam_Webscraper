#include<stdio.h>
#include<string.h>

int main()
{
long long ans;
int t,d=1,k,l,i,j;
char S[1010];
scanf("%d",&t);
while(t--)
{
scanf("%s %d",S,&k);
l=strlen(S);
int flag=0;
for(i=0;i<l;i++)
{
if(S[i]=='-')
{flag=1;
break;
}
}
if(flag==0)printf("Case #%d: 0\n",d);
else
{
ans=0;
i=0;
while(i<l-k)
{
if(S[i]=='-')
{
ans++;
for(j=0;j<k;j++){
if(S[i+j]=='+')S[i+j]='-';
else S[i+j]='+';
}
}
i++;
}
char c=S[l-k];
flag=0;
for(i=l-k;i<l;i++)
{
if(S[i]!=c){flag=1;break;}
}

if(c=='-')ans++;
if(flag==1)printf("Case #%d: IMPOSSIBLE\n",d);
else printf("Case #%d: %lld\n",d,ans);
}
d++;
}
return 0;
}