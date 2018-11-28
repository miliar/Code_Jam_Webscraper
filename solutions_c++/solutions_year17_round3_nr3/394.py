
#include <iostream>
#include <algorithm>
#include <cstdio>
#include <queue>
const double  eps = 1e-12;
const double PI=acos(-1.0);
using namespace std;
priority_queue<double, vector<double>, greater<double> >ans;
struct node {
    double r,h;
    double cs,ds,s;
}a[1111];
bool cmp(node a,node b)
{
    return a.cs >b.cs;
}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int M;
    int tes = 0;
    cin >> M;
    while (M--)
    {
    int N,K;
    cin >> N >> K;
    double t ;
    cin >> t;
    for (int i = 1; i<=N; i++)
    {
        double x;
        cin >> x;
        ans.push(x);
    }

    while (t>eps*100)
    {
        double to = ans.top();
        if (to>=1-eps) break;
        ans.pop();
        to+=(double)0.0001;
        t-=(double)0.0001;
        ans.push(to);
    }
    double res = 1;
    while (!ans.empty())
    {
        res*=ans.top();
        ans.pop();
    }
    printf("Case #%d: %.12f\n",++tes,res>=1?1.0000000:res);
}
}
