#include <bits/stdc++.h>
using namespace std;
int num[8];
char str[]={"ROYGBV"};
int main()
{
    freopen("B-small-attempt1.in","r",stdin);
    freopen("B-small-attempt1.out","w",stdout);
    int t,a,b,c,d,e,f,n;
    scanf("%d",&t);
    for (int test=1;test<=t;++test)
    {
        scanf("%d",&n);
        for (int i=0;i<6;++i)
            scanf("%d",&num[i]);
        printf("Case #%d: ",test);
        if (num[0]>n/2 || num[2]>n/2 || num[4]>n/2)
            printf("IMPOSSIBLE\n");
        else
        {
            int lst=-1;
            int first=-1;
            while(n--)
            {
                int idx=-1;
                for (int i=0;i<6;i+=2)
                    if (num[i] &&i!=lst && (idx==-1 || num[i]>num[idx] ||
                                   (num[i]==num[idx] && i==first)))
                            idx=i;
                printf("%c",str[idx]);
                --num[idx];
                lst=idx;
                if (first==-1)
                    first=idx;
            }
            printf("\n");
        }
    }
}
