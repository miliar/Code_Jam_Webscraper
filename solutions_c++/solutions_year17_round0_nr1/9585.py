#include<stdio.h>
#include<string.h>
int main()
{
freopen("A-large.in","r",stdin);
freopen("output1.txt","w",stdout);
int t,i,j,count=0,n,k,l;
char arr[1003];
scanf("%d",&t);
i=0;
while(t--)
{
    int flag=1;
scanf("%s",arr);
scanf("%d",&k);
n=strlen(arr);
count=0;
for(j=0;j<n;j++)
{
if(arr[j]=='+')
{continue;}
else
{
for(l=j;l<j+k;l++)
{
    if(j+k>n)
    {
        flag=0;
        break;
    }
    if(arr[l]=='+')
    {arr[l]='-';}
else
{arr[l]='+';}
}
count++;
}
}
if(flag)
    printf("case #%d: %d\n",++i,count);
else
    printf("case #%d: IMPOSSIBLE\n",++i);
}
}
