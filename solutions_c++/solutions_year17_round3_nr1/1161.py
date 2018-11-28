#include<bits/stdc++.h>

using namespace std;

vector<pair<long long,long long> >v;

const double pi = acos(-1);

long long dp[1005][1005];

int main(){

    freopen("gcj_in.txt","r",stdin);
    freopen("gcj_out.txt","w",stdout);
    int t;
    cin >> t;
    for(int it=1;it<=t;it++) {
        v.clear();
        long long n,k,i,j,idx=1,r,h,temp,k1,x,y;
        scanf("%lld%lld",&n,&k);
        for(i=0;i<=n;i++) {
            for(j=0;j<=k;j++) {
                dp[i][j] = 0;
            }
        }
        for(i=1;i<=n;i++) {
            scanf("%lld%lld",&x,&y);
            v.push_back(make_pair(x,y));
        }
        sort(v.begin(),v.end());
        dp[1][1] = v[0].first * v[0].first + 2 * v[0].first * v[0].second; idx = 2;
        for(i=1;i<n;i++) {
            r = v[i].first; h = v[i].second;
            for(j=1;j<=idx;j++) {
                if(j == 1) dp[idx][j] = r * r + 2 * r * h;
                else {
                    for(k1=i-1;k1>=0;k1--) {
                        temp = r * r - v[k1].first * v[k1].first;
                        dp[idx][j] = max(dp[idx][j],dp[k1 + 1][j - 1] + temp + 2 * r * h);
                    }
                }
             //   cout << dp[idx][j] << "\n";
            }
            idx = idx + 1;
        }
        double ans=0;
        temp = 0;
        for(i=0;i<n;i++) {
            temp = max(temp,dp[i + 1][k]);
        }
        ans = (double)temp * pi;

        cout << "Case #" << it << ": ";
        printf("%0.8f\n",ans);
    }
    return 0;


}
