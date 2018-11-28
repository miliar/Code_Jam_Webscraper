#include <bits/stdc++.h>

using namespace std;

#define MAX 1000005
#define ll long long
#define PI acos(-1)

int main()
{
    //freopen("A-large.in", "r", stdin);
    //freopen("out.txt", "w", stdout);
    int cases;
    scanf("%d", &cases);
    int caseno = 0;
    while(cases--){
        ll n, k;
        scanf("%lld %lld", &n, &k);
        vector<pair<ll, ll> > V;
        ll used[MAX];
        memset(used, 0, sizeof used);
        for(int i=0; i<n; i++){
            ll r, h;
            scanf("%lld %lld", &r, &h);
            V.push_back(make_pair(2*r*h, r));
        }
        sort(V.begin(), V.end());
        reverse(V.begin(), V.end());
        ll ans = 0;
        for(int i=0; i<k; i++){
            ans += V[i].first;
        }
        ll temp = 0;
        for(int i=0; i<k; i++){
            temp = max(temp, V[i].second * V[i].second);
        }
        ll mins = V[k-1].first;
        for(int i=k; i<n; i++){
            temp = max(temp, V[i].second * V[i].second + V[i].first - mins);
        }
        ans += temp;
        double res = (double) (ans * 1.0) * PI;
        printf("Case #%d: %.9lf\n", ++caseno, res);
    }
}
