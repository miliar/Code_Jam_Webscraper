#include<stdio.h>
int main()
{
long long int n;
int t,g=1,c=0,j[20],count=0,i,a,q,temp,k=0,flag=0,w=1,m=0,prev=-1;
scanf("%d",&t);
while(t)
{
    scanf("%lld",&n);
    c=0;w=0;q=0;flag=0;k=0;m=0;count=0;
    for(i=0;i<20;i++)
        j[i]=0;
    if(n>=0&&n<=9)
    printf("case #%d: %lld\n",g++,n);
    else
{
    while(n!=0)
    {
        a=n%10;
        n=n/10;
        j[c++]=a;
    }
    for(i=0;i<c/2;i++)
    {
        temp=j[i];
        j[i]=j[c-i-1];
        j[c-i-1]=temp;
    }
    prev=j[0];
    count++;
    for(int i=1;i<c;i++)
           if(j[i]==prev)
            count++;
    if(count==c)
    {
        printf("Case #%d: ",g);
        g++;
        for(i=0;i<c;i++)
        printf("%d",j[i]);
        printf("\n");
    }
    else
        {
for(i=0;i<c-1;i++)
       {
           if(j[i]<j[i+1])
            continue;
           else if((j[i]>j[i+1]&&j[i]!=j[i-1])||(j[i]>j[i+1]&&i==0))
                {
                    flag=i;
                    w++;
                    break;
                }
            else if(j[i]>j[i+1]&&j[i]==j[i-1])
                {
                    k=i;
                    m=1;
                    break;
                }
    }
if(w>0)
    {
        if(flag!=c-1)
            {
        j[flag]=j[flag]-1;
        for(i=flag+1;i<c;i++)
            j[i]=9;
            }
    }
else if(m==1)
        {
           q=k-1;
           if(q>=0)
               while(j[k]==j[q]&&k>0)
                    k=k-1;

                j[k]=j[k]-1;
                for(i=k+1;i<c;i++)
                    j[i]=9;
        }
printf("Case #%d: ",g);
g++;
for(i=0;i<c;i++)
{
  if(j[i]==0&&i==0)
    continue;
  else
    printf("%d",j[i]);
}
printf("\n");
}}
    t--;
}
return 0;
}
