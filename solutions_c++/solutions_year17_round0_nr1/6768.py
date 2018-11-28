#include <bits/stdc++.h>

#define INF (1 << 29)
#define rep2(i,m,n) for(int i=(int)(m);i<(int)(n);i++)
#define rep(i,n) rep2(i,0,n)
#define EPS 1e-10

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> P;

int dx[4] = {-1,0,1,0};
int dy[4] = {0,1,0,-1};

int func(string &str, int k) {
    vector<bool> memo(str.size());
    int sz = str.size();
    rep(i,str.size()) memo[i] = str[i]=='+';
    int ans = 0;
    rep(i,sz-k+1) if(!memo[i]) {
        ans++;
        rep(j,k) memo[i+j] = !memo[i+j];
    }
    rep2(i,sz-k,sz) if(!memo[i]){
        return -1;
    }
    return ans;
}

int main()
{
    int T;
    cin >> T;

    rep(cnum, T) {
        string str;
        int k;
        cin >> str >> k;
        int ans = func(str,k);
        if(ans<0) {
            cout << "Case #" << cnum+1 << ": IMPOSSIBLE" << endl;
        } else {
            cout << "Case #" << cnum+1 << ": " << ans << endl;
        }
    }
    return 0;
}
