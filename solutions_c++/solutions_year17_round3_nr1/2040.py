using namespace std;

#include<bits/stdc++.h>

#define ll long long
#define INF -1e18
#define pi 3.14159265359

ll N, K;
vector<pair<double, double>> v;

double Func(ll i, ll s)
{
    if(i<0){
        if(s==K) return 0;
        else return INF;
    }
    if(s==K) return 0;

    double area = 2*pi*v[i].first*v[i].second;
    if(s==0) area += pi*v[i].first*v[i].first;

    return max(area+Func(i-1,s+1), Func(i-1,s));
}

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    freopen("A.in", "r", stdin);
    FILE *fp;
    fp = fopen ("A.out","w");
    ///freopen("A.out", "w", stdout);

    ll T, N, D;
    cin>>T;

    for(int iter=1; iter<=T; iter++){
        ios::sync_with_stdio(false);
        cin.tie(NULL);

        cin>>N>>K;
        double r, h;

        for(ll i=0; i<N; i++){
            cin>>r>>h;
            v.push_back(make_pair(r,h));
        }

        sort(v.begin(),v.end());
        double ans = Func(N-1, 0);
        fprintf (fp, "Case #%d: %.10f\n",iter,ans);

        v.clear();
    }

return 0;
}
