#include<bits/stdc++.h>
int main()
{
    int t,i,k,j,n,m;
    scanf("%d",&t);
    for(m=1;m<=t;m++)
    {
        char str[1001];
        int arr[1001],coun=0,flag=0,l=0;
        scanf("%s%d",str,&k);
        int len=strlen(str);
        for(n=0;n<len;n++)
        {
            if(str[n]=='+')
                {
                    arr[l]=1;
                    l++;
                }
            else
               {
                   arr[l]=-1;
                   l++;
               }
        }
        for(i=0;i<=l-k;i++)
        {
            if(arr[i]==-1)
            {
                for(j=i;j<i+k;j++)
                {
                    if(j==l)
                        break;
                    arr[j]*=-1;
                }

                coun++;
            }
        }
        for(n=0;n<l;n++)
            if(arr[n]==-1)
            flag=1;
        if(flag==1)
            printf("Case #%d: IMPOSSIBLE\n",m);
        else
            printf("Case #%d: %d\n",m,coun);
    }
    return 0;
}
