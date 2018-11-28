#include<bits/stdc++.h>
using namespace std;
int a[1500];
char b[1500];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out1.out","w",stdout);
    int Q,num = 1,o = 0;
    scanf("%d",&Q);
    while(Q--)
    {
        o = 0;
        int k;
        scanf(" %s %d",b,&k);
        int n = strlen(b);
        for(int i=0; i<n; i++)
        {
            if(b[i] == '+')
                a[i] = 1;
            else
                a[i] = 0;
        }
        for(int i=0; i<n; i++)
        {
            if(!a[i])
            {
                o++;
                if(i+k-1<n)
                for(int j = i; j<i+k && j< n; j++)
                    a[j] = !a[j];
            }
        }
        int ch = 0;
        for(int i=0; i<n; i++){
            if(!a[i])
            {
                ch = 1;
                break;
            }
        }
        if(ch)
            printf("Case #%d: IMPOSSIBLE\n",num);
        else
            printf("Case #%d: %d\n",num,o);
        num++;
    }
    return 0;
}
