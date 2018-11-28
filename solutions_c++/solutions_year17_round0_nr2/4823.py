#include<bits/stdc++.h>
int main()
{
    int t,i,arr[20],m,l;
    scanf("%d",&t);
    for(m=1;m<=t;m++)
    {
        char str[20];
        int x=0;
        scanf("%s",str);
        int len=strlen(str);
        for(i=len-1;i>=0;i--)
        {
            arr[x]=str[i]-48;
            x++;
        }
        for(i=1;i<x;i++)
        {
            if(arr[i]>arr[i-1])
            {
                arr[i]--;
                for(l=i-1;l>=0;l--)
                    arr[l]=9;
            }
        }
        printf("Case #%d: ",m);
        if(arr[x-1]!=0)
            printf("%d",arr[x-1]);
        for(i=x-2;i>=0;i--)
        {
            printf("%d",arr[i]);
        }
        printf("\n");
    }

    return 0;
}
