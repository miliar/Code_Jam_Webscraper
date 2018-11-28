#include <bits/stdc++.h>
using namespace std;

#define maxn 1010

int a[maxn][maxn];

int dp[maxn][maxn];

int rsum[maxn], colsum[maxn], tsum[maxn];
multiset <int> s; 

int ans;

bool check (int lim, int n){
    s.clear();
    ans= 0;
    if (colsum[1]>lim) return 0;
    for (int i=1; i<=n; i++) tsum[i]= colsum[i];

    s.insert(tsum[1]);
    for (int i=2; i<=n; i++){
        if (tsum[i]>lim){
            while (tsum[i]!=lim){
                int t= *s.begin();
                if (t==lim) return 0;
                s.erase(s.find(t));
                tsum[i]--;
                ans++;
                s.insert(t+1);
            }
        }
        s.insert(colsum[i]);
    } 
    return 1;   

}

void solve(int ind){
    for (int i=0; i<maxn; i++){
        for (int j=0; j<maxn; j++) {
            a[i][j]= 0;
            dp[i][j]= 0;
        }
    }
    int n, c, m;
    cin>>n>>c>>m;
    s.clear();
    for (int i=1; i<=m; i++){
        int x, y;
        cin>>x>>y;
        a[y][x]++;
    }
    int maxr= 0, maxc= 0;
    for (int i=1; i<=c; i++){
        int t= 0;
        for (int j=1; j<=n; j++){
            t+=a[i][j];
        }
        rsum[i]= t;
        maxr= max(maxr, t);
    }
    for (int j=1; j<=n; j++){
        int t= 0;
        for (int i=1; i<=c; i++){
            t+=a[i][j];
        }
        colsum[j]= t;
        maxc= max(maxc, t);
    }
    if (maxc<=maxr){
        cout<<"Case #"<<ind<<": "<<maxr<<" "<<0<<endl;
        return;
    }
    int s=0;
   int res= 0;
    int cur= max(n, c);
    for (int i=20; i>=0; i--){
        int tmp= cur-(1<<i);
        if (tmp<maxr) continue;
        if (check(tmp, n)) cur= tmp;
    }
    check(cur, n);

    cout<<"Case #"<<ind<<": "<<cur<<" "<<ans<<endl;
}




int main(){
    int t;
    cin>>t;
    for (int i=1; i<=t; i++) solve(i);
}