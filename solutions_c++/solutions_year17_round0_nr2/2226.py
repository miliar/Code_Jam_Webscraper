#include<bits/stdc++.h>
using namespace std;
char b[20];
int a[20];
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out1.out","w",stdout);
    int Q;
    scanf("%d",&Q);
    for(int q=1;q<=Q;q++)
    {
        scanf(" %s",b);
        int ch = 1;
        int n = strlen(b);
        for(int i=0;i<n;i++)
            a[i] = b[i] - '0';
        int i;
        while(ch)
        {
            for(i=0;i<n-1;i++)
            {
                if(a[i] > a[i+1])
                {
                    a[i]--;
                    for(int j=i+1;j<n;j++)
                        a[j] = 9;
                    break;
                }
            }
            if(i == n-1)
                ch = 0;
        }
        for(i=0;i<n;i++)
        {
            if(a[i]!=0)
                break;
        }
        printf("Case #%d: ",q);
        for(;i<n;i++)
            printf("%d",a[i]);
        printf("\n");
    }

    return 0;
}
