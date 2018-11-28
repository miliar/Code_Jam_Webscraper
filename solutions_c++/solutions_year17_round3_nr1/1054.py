#include<bits/stdc++.h>
#define MX 1005
using namespace std;
typedef long long ll;
const double PI=acos(-1);
const double inf=1e19;

pair< int, int > ara[MX];

int n, k;
double dp[MX][MX][3];
bool vis[MX][MX][3];

double func(int pos, int cnt, bool flag){
     if(cnt>=k) return 0;
     if(pos<0 && cnt<k) return -inf;
     if(vis[pos][cnt][flag]) return dp[pos][cnt][flag];
     vis[pos][cnt][flag]=1;
     double r, tmp;
     r=func(pos-1, cnt, flag);
     tmp=2.*PI*ara[pos].first*ara[pos].second;
     if(flag){
          r=max(r, tmp+func(pos-1, cnt+1, 1));
     }
     else{
          tmp=tmp+PI*ara[pos].first*ara[pos].first;
          r=max(r, tmp+func(pos-1, cnt+1, 1));
     }
     return dp[pos][cnt][flag]=r;
}

int main(){
     freopen("in1.txt", "r", stdin);
     freopen("out1.txt", "w", stdout);
     int i, j;
     int t, T;
     cin >> T;
     for(t=1; t<=T; ++t){
          cin >> n >> k;
          memset(vis, 0, sizeof vis);
          for(i=0; i<n; ++i) cin >> ara[i].first >> ara[i].second;
          sort(ara, ara+n);
          printf("Case #%d: %0.8lf\n", t, func(n-1, 0, 0));
     }
     return 0;
}
