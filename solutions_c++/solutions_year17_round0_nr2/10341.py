#include<bits/stdc++.h>
int main()
{
    freopen("input.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int reserve[1002]={0};
    for(int i=0;i<1000;i++)
    {
        int tem=i;
        int a=tem%10;
        int b=(tem/10)%10;
        int c=(tem/100)%10;
        if(c<=b && b<=a)
            reserve[i]=1;
    }
    reserve[1000]=0;
    int n,i,data;
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
        scanf("%d",&data);
        for(int j=data;;j--)
        {
            if(reserve[j]==1)
            {
                printf("Case #%d: %d\n",i+1,j);
                break;
            }
        }
    }
    return 0;
}
