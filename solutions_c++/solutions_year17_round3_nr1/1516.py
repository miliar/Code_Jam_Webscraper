#include<bits/stdc++.h>
using namespace std;

double pi = 3.14159265358979;

vector<pair<double,double> >v;
double dp[1002][1002];
bool visited[1002][1002];

int n;
double solve(int pos,int remaining)
{
    if(remaining==1)
    {
        double r = v[pos].first,h = v[pos].second;
        return 2*pi*r*h + pi*r*r;
    }
    if(pos==n-1)
        return -1000000;
    if(visited[pos][remaining])
        return dp[pos][remaining];
    visited[pos][remaining] = true;
    double r = v[pos].first,h = v[pos].second;
    double mn = -1000000;
    for(int i=pos+1;i<n;i++)
    {
        double d = solve(i,remaining-1);
        if(d>=0)
        {
            double area = 2*pi*r*h + pi*r*r - pi*v[i].first*v[i].first;
            mn = max(mn,area+d);
        }
    }
    return dp[pos][remaining] = mn;
}

int main()
{
    int T,k;
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    cin>>T;

    for(int t=1;t<=T;t++)
    {
        cin>>n>>k;
        v.clear();
        for(int i=0;i<n;i++)
        {
            double r,h;
            cin>>r>>h;
            v.push_back(make_pair(r,h));
        }
        sort(v.begin(),v.end());
        reverse(v.begin(),v.end());
        double d = 0;
        memset(visited,false,sizeof(visited));
        for(int i=0;i<n;i++)
        {
            double area = solve(i,k);
            d = max(d,area);
        }
        cout<<"Case #"<<t<<": ";
        std::cout << std::fixed;
        std::cout << std::setprecision(9);
        cout<<d<<endl;
    }

}
