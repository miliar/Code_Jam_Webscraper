#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <cmath>
#include <climits>
#include <algorithm>
#include <cstring>
#include <bitset>
#include <functional>
#include <map>

using namespace std;

typedef pair<int, int> pii;
typedef pair<pair<int, int>, pair<int, int>> piii;
typedef long long ll;
#define ff first.first
#define fs first.second
#define sf second.first
#define ss second.second

int t;
int n, k;
vector <pair <double, double>> vt;
double phi = 3.14159265359;
double ans;

void func(int a, int b, double c)
{
    if(b == k)
    {
        ans = max(ans, c);
        return;
    }

    for(int i=a+1;i<n;i++)
    {
        double temp = 2.0*vt[i].first*vt[i].second*phi;
        func(i, b+1, c+temp);
    }
    return;
}

int main(void)
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("output-A.txt", "w", stdout);
    scanf("%d", &t);
    for(int o=1;o<=t;o++)
    {
        ans = 0.0;
        vt.clear();
        scanf("%d %d", &n, &k);
        vt.resize(n);
        for(int i=0;i<n;i++)
        {
            scanf("%lf %lf", &vt[i].first, &vt[i].second);
        }
        sort(vt.begin(), vt.end(), greater<pair<double, double>>());
        for(int i=0;i<n;i++)
        {
            double temp = vt[i].first*vt[i].first*phi+2.0*vt[i].first*vt[i].second*phi;
            func(i, 1, temp);
        }
        printf("Case #%d: %.7lf\n", o, ans);
    }
}
