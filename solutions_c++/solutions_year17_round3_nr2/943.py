#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t,n,m,i;
    int cse=1;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d%d",&n,&m);
        pair<int,int> a[5];
        pair<int,int> b[5];
        for(i=0;i<n;i++)
        {
            scanf("%d%d",&a[i].first,&a[i].second);
        }
        for(i=0;i<m;i++)
        {
            scanf("%d%d",&b[i].first,&b[i].second);
        }
        if(n+m==1)
            printf("Case #%d: 2\n",cse);
        else
        {
            if(n==2)
            {
                sort(a,a+n);
                if(abs(a[0].first+1440-a[1].second)>=720||abs(a[0].second-a[1].first)>=720)
                {
                    printf("Case #%d: 2\n",cse);
                }
                else
                {
                    printf("Case #%d: 4\n",cse);
                }
            }
            else if(m==2)
            {
                sort(b,b+m);
                if(abs(b[0].first+1440-b[1].second)>=720||abs(b[0].second-b[1].first)>=720)
                {
                    printf("Case #%d: 2\n",cse);
                }
                else
                {
                    printf("Case #%d: 4\n",cse);
                }
            }
            else
            {
                if(a[0]<b[0])
                {
                if(abs(a[0].first+1440-b[0].first)>=720||abs(b[0].first-a[0].first)>=720)
                {
                    printf("Case #%d: 2\n",cse);
                }
                else
                {
                    printf("Case #%d: 4\n",cse);
                }
                }
                else
                {
                if(abs(b[0].first+1440-a[0].first)>=720||abs(a[0].first-b[0].first)>=720)
                {
                    printf("Case #%d: 2\n",cse);
                }
                else
                {
                    printf("Case #%d: 4\n",cse);
                }
                }
            }
        }
        cse++;
    }
    return 0;
}
