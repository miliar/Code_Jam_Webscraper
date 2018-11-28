#include <iostream>
#include <cstdio>
#include <string>
#include <cmath>
#include <iomanip>
#include <vector>
#include <algorithm>
#include <cstring>


using namespace std;

int n,k;
vector<pair<double,double> > p(1010);
double dp[1010][1010];

double pi=3.1415926535897932;

double solve(int pancake, int stak)
{
    if (stak==k || pancake==n) return 0;
    if(dp[pancake][stak]!=-1)
    {
        return dp[pancake][stak];
    }
    double s = p[pancake].second;
    if(stak>0) s-=p[pancake].first*p[pancake].first*pi;
    dp[pancake][stak]=max(solve(pancake+1,stak),s+solve(pancake+1,stak+1));
    return dp[pancake][stak];
}

int main()
{

    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);

    int t;
    cin >> t;

    for(int tc=0;tc<t;tc++)
    {
        p.clear();
        cin >> n >> k;
        for(int i=0;i<n;i++)
        {
            double r,h;
            cin >>r>>h;
            p.push_back(make_pair(r,pi*r*r+2*r*h*pi));
        }
        sort(p.rbegin(),p.rend());
        for(int i=0;i<1010;i++)
            for(int j=0;j<1010;j++) dp[i][j]=-1;
        double s = solve(0,0);
        cout <<"Case #"<<tc+1<<": "<<fixed << setprecision(9) <<s;
        if(tc<t-1) cout << endl;
    }
    return 0;
}

