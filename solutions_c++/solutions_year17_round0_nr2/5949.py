#include<stdio.h>
#include<string.h>
int main()
{
int i,l,t,d=1,A[20],flag;
char S[20];
scanf("%d",&t);
while(t--)
{
flag=-1;
scanf("%s",S);
l=strlen(S);
for(i=0;i<l;i++)A[i]=S[i]-'0';
for(i=0;i<l-1;i++){
if(A[i]>A[i+1])
{
flag=i;
break;
}
}
if(flag<0)printf("Case #%d: %s\n",d,S);
else
{
for(i=flag+1;i<l;i++)A[i]=9;
A[flag]--;
for(i=flag-1;i>=0;i--){
if(A[i]>A[i+1])
{
A[i]--;
A[i+1]=9;
}}
printf("Case #%d: ",d);
if(A[0]==0)for(i=1;i<l;i++)printf("9");
else for(i=0;i<l;i++)printf("%d",A[i]);
printf("\n");
}
d++;
}
return 0;
}