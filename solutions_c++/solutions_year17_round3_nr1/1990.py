#include<bits/stdc++.h>
using namespace  std;
vector<pair<long long int,long long int> >a;
vector<pair<long long int,long long int> >b;
bool cmp(pair<long long int,long long int> p, pair<long long int,long long int> q)
{
    return(p.first*p.second<q.first*q.second);
}
bool cmp1(pair<long long int,long long int> p, pair<long long int,long long int> q)
{
    return(p.first<q.first);
}
int main()
{
    //freopen("i.in","r",stdin);
	//freopen("o1.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++)
    {
        int n,k;
        scanf("%d %d",&n,&k);
        int p,q;
        for(int j=0;j<n;j++)
        {
            scanf("%d %d",&p,&q);
            a.push_back(make_pair(p,q));
            b.push_back(make_pair(p,q));
        }

        sort(a.begin(),a.end(),cmp);
        sort(b.begin(),b.end(),cmp1);

        long long int max1=0;
        for(int j=n-1,o=0;o<k;o++,j--)
        {
            max1=max(max1,a[j].first);
        }
        //long long int check;
        double ans;
        ans=(double)max1*max1*M_PI;
        //ans=ans/7;
        //check=max1*max1;
        for(int j=n-1,o=0;o<k;j--,o++)
        {
            ans+=((double)2*a[j].first*a[j].second*M_PI);
          //  check+=2*a[j].first*a[j].second;
        }
        double ans2;
        //long long int check2;
        max1=b[n-1].first;
        //check2=max1*max1;
        ans2=(double)max1*max1*M_PI;
       // printf("*");
        int r=0;
        for(int j=n-1,o=0;o<k-1;j--)
        {
            if(a[j].first==b[n-1].first&&a[j].second==b[n-1].second&&r==0)
            {
                r=1;
                continue;
            }
            ans2+=((double)2*a[j].first*a[j].second*M_PI);
            o++;
          //  check2+=2*b[j].first*b[j].second;
        }
        ans2+=(double)2*b[n-1].first*b[n-1].second*M_PI;
       // printf("%lf %lf %lld %lld\n",ans,ans2,check,check2);
        if(ans2<ans)
        printf("Case #%d: %.9lf\n",i,ans);
        else
             printf("Case #%d: %.9lf\n",i,ans2);
        a.clear();
        b.clear();
    }
    return 0;
}
