#include <bits/stdc++.h>

using namespace std;
# define M_PI           3.14159265358979323846
typedef long long ll;
typedef pair<int,double>pid;
vector<pid>vpid;
bool op(pair<int,double>p1,pair<int,double>p2)
{
    if(p1.first>p2.first)return 1;
    if(p1.first==p2.first&&p1.second-p2.second>=1e-6)return 1;
    return 0;
}
int n,k;
double mem[1001][1001][2];
double rec(int i,int rem,bool anytaken)
{
    if(i==n||rem==0)return 0.0;
    double &ret=mem[i][rem][anytaken];
    if(ret+1>=1e-6)return ret;
    ret=0.0;
    double c1=rec(i+1,rem,anytaken);
    double c2=vpid[i].second;
    if(anytaken)c2-=M_PI*vpid[i].first*vpid[i].first;
    for(int j=i+1;j<n;j++)
    {
        c2=vpid[i].second;
        if(anytaken)c2-=M_PI*vpid[i].first*vpid[i].first;
        c2+=rec(j,rem-1,1);

        if(c2-c1>=1e-6)
        {
            if(c2-ret>=1e-6)ret=c2;
        }
        else
        {
            if(c1-ret>=1e-6)ret=c1;
        }

    }
    if(c2-c1>=1e-6)
        {
            if(c2-ret>=1e-6)ret=c2;
        }
        else
        {
            if(c1-ret>=1e-6)ret=c1;
        }
    return ret;
}
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T,q=0;
    cin>>T;
    int r,h;
    while(T--)
    {
        vpid.clear();
        cin>>n>>k;
        for(int i=0;i<n;i++)
        {
            cin>>r>>h;
            vpid.push_back(make_pair(r,M_PI*r*r*1.0+2*M_PI*r*h*1.0));
        }
        sort(vpid.begin(),vpid.end(),op);
        memset(mem,-1,sizeof mem);
        //for(int i=0;i<n;i++)cout<<vpid[i].first<<" "<<vpid[i].second<<endl;
        printf("Case #%d: ",++q);
        cout<<fixed<<setprecision(8);
        cout<<rec(0,k,0)<<endl;
    }
    return 0;
}
