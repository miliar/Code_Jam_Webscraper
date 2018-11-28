#include<stdio.h>
#define MAX 1010

int S[MAX];
long K[MAX];

int main()
{
int t,d=0,n,i,j;
long D;
double ans,time,temp;
scanf("%d",&t);
while(t--)
{
time=0.0;
scanf("%ld %d",&D,&n);
for(i=0;i<n;i++)scanf("%ld %d",&K[i],&S[i]);
time=1.0*(D-K[0])/S[0];
i=1;
while(i<n)
{
temp=1.0*(D-K[i])/S[i];
if(temp>time)time=temp;
i++;
}
printf("Case #%d: %lf\n",d+1,1.0*D/time,time);
d++;
}
return 0;
}