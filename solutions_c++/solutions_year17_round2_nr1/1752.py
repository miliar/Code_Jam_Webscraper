#include<bits/stdc++.h>
using namespace std;

int main()
{
    int t,n,x,y,i;
    int test=1;
    scanf("%d",&t);
    while(t--)
    {
        double d;
        scanf("%lf%d",&d,&n);
        pair<int,int> p[n];
        for(i=0;i<n;i++)
        {
            scanf("%d%d",&x,&y);
            p[i].first=x;
            p[i].second=y;
        }
        //cout<<"haha";
        sort(p,p+n);
        double ans=0,k;
        for(i=n-1;i>=0;i--)
        {
            k=double(d-p[i].first)/(double)(p[i].second);
            //cout<<k<<endl;
            if(k>ans)
                ans=k;
        }
        printf("Case #%d: %lf\n",test,d/ans);
        test++;
    }
    return 0;
}

