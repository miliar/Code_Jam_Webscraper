#include <bits/stdc++.h>
#include<string.h>
#define MOD 1000000003
#define MAXA 10000000000000ll
#define PI 3.14159265358979323846264338327950
#define INF 0x3f3f3f3f
typedef long long int ll;
using namespace std;
const  int maxn=5e5+5;
const int N=1e6+5;
vector<pair<pair<int,int> ,int> > v,v1;
bool cmp(pair<pair<int,int>,int> p1,pair<pair<int,int>,int> p2)
{
    ll temp1=p1.first.first*1LL*p1.first.first+p1.first.first*2LL*p1.first.second;
    ll temp2=p2.first.first*1LL*p2.first.first+p2.first.first*2LL*p2.first.second;
    if(temp1!=temp2)
    return temp1<temp2;
    return p1.first.first<p2.first.first;
}
bool cmp1(pair<pair<int,int>,int> p1,pair<pair<int,int>,int> p2)
{
    ll temp1=p1.first.first*1LL*p1.first.second;
    ll temp2=p2.first.first*1LL*p2.first.second;
    if(temp1!=temp2)
    return temp1<temp2;
    return p1.first.first<p2.first.first;
}
int main()
{
    freopen("A4.in","r+",stdin);
    freopen("ou.txt","w+",stdout);
    int t,n,k,i,r,h,t1=1,j;
    cin>>t;
    while(t--)
    {
        cin>>n>>k;
        v.clear();
        v1.clear();
        for(i=0;i<n;i++)
        {
            cin>>r>>h;
            v.push_back(make_pair(make_pair(r,h),i));
            v1.push_back(make_pair(make_pair(r,h),i));
        }
        sort(v.begin(),v.end(),cmp);
        sort(v1.begin(),v1.end(),cmp1);
        double maxa=0;
        for(i=v.size()-1;i>=0;i--)
        {
            pair<pair<int,int>,int> p =v[i];
            int c=0;
            double ans1=p.first.first*1LL*p.first.first+p.first.first*2LL*p.first.second;
            for(j=v1.size()-1;j>=0;j--)
            {
                if(v1[j].second!=v[i].second)
                {
                    if(c==k-1)
                        break;
                    ans1+=v1[j].first.first*2LL*v1[j].first.second;
                    c++;
                }
            }
            if(ans1>maxa)
                maxa=ans1;
        }
        maxa=maxa*PI;
        printf("Case #%d: %0.9lf\n",t1,maxa);
        t1++;
    }
    return 0;
}
