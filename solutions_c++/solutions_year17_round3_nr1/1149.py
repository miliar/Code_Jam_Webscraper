/*
#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <climits>
#include <algorithm>
#include <cstring>
#include <map>
#include <queue>
#include <cmath>
#define PI 3.14159265359
using namespace std;

vector<pair<pair<double, double>,double> > p;

bool cmp(pair<pair<double, double>,double> &u, pair<pair<double, double>,double> &v)
{
    if(u.first.first > v.first.first){
        return true;
    }else if(u.first.first == v.first.first){
        if(u.first.second > v.first.second){
            return true;
        }else if(u.first.second == v.first.second){
            if(u.second < v.second)
                return true;
        }
    }
    return false;
}

int main(void)
{

    freopen("A-small-attempt1.in", "r", stdin);
    freopen("ASoutput2.txt", "w", stdout);


    int t;
    cin >> t;

    int n, k;
    double r, h;
    for(int i=1;i<=t;i++){
        cin >> n >> k;
        p.clear();
        for(int j=0;j<n;j++){
            cin >> r >> h;
            p.push_back({{2*PI*r*h + PI *r *r, h}, r});
        }
        sort(p.begin(), p.end(), cmp);

        double maxR = 0;
        double ans = 0;

        for(int j=0;j<k;j++){
            ans += 2*PI*p[j].first.second*p[j].second;
            maxR = max(maxR, p[j].second);
        }
        ans += PI*maxR*maxR;

        printf("Case #%d: %0.9f\n",i, ans);
    }

    return 0;
}
*/

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

int ttt;
int n, k;
vector <pair <double, double>> vt;
vector <pair <double, double>> ht;
double phi = 3.14159265359;
double ans;

void func(double aaa, double bbb, double ccc)
{
    int cnt = 1;
    if(cnt == k)
    {
        ans = max(ans, ccc);
        return;
    }
    bool check = false;
    for(int i=0;i<n;i++)
    {
        if(ht[i].second <= aaa)
        {
            if(ht[i].second == aaa && ht[i].first == bbb && !check)
            {
                check = true;
                continue;
            }
            ccc += ht[i].first;
            cnt+=1;
        }
        if(cnt == k)
            break;
    }
    ans = max(ans, ccc);
    return;
}

int main(void)
{

    freopen("A-large (1).in", "r", stdin);
    freopen("output-AL.txt", "w", stdout);

    scanf("%d", &ttt);
    for(int ooo=1;ooo<=ttt;ooo++)
    {
        ans = 0.0;
        vt.clear();
        scanf("%d %d", &n, &k);
        vt.resize(n);
        ht.resize(n);
        for(int i=0;i<n;i++)
        {
            scanf("%lf %lf", &vt[i].first, &vt[i].second);
            ht[i].first = 2.0*vt[i].first*vt[i].second*phi;
            ht[i].second = vt[i].first;
        }
        sort(vt.begin(), vt.end(), greater<pair<double, double>>());
        sort(ht.begin(), ht.end(), greater<pair<double, double>>());
        for(int i=0;i<n-k+1;i++)
        {
            double temp = vt[i].first*vt[i].first*phi+2.0*vt[i].first*vt[i].second*phi;
            func(vt[i].first,2.0*vt[i].first*vt[i].second*phi, temp);
        }
        printf("Case #%d: %.7lf\n", ooo, ans);
    }
}
