/// In the name of God
#include <bits/stdc++.h>
//#define int long long
using namespace std;
typedef pair<int,int> pii;
typedef long long ll;
typedef long double ld;
typedef vector<int> vi;

#define y1 def1
#define X first
#define Y second
#define endl '\n'
#define all(o) o.begin(), o.end()
#define IOS ios::sync_with_stdio(0), cin.tie(0)
int cnt[5], mod;
int dp[4][100][100];
int Dp[4][100][100][100];
bool bad = 0;
bool gg(int x,int y){
    if(x == 0) return 1;
    return 0;
}
int pros(){
    int n, p;
    cin >> n >> p;
    memset(cnt, 0, sizeof cnt);
    int sm = 0;
    for(int i=0; i<n; i++){
        int x;
        cin >> x;
        cnt[x % p]++;
        sm = (sm + x) % p;
    }
    mod = p;
    if(cnt[0] == n) return n;
    if(p == 2){
        if(cnt[1] % 2 == 0)
            return cnt[0] + cnt[1]/2;
        return cnt[0] + cnt[1]/2 + 1;
    }
    if(p == 3)
    {
        memset(dp, -63, sizeof dp);
        dp[0][0][0] = 0;
        for(int i=0; i<=cnt[1]; i++)
            for(int j=0; j<=cnt[2]; j++)
                for(int r=0; r<3; r++){
                    if(i + j + 1 == n) bad = 1;
                    dp[(r+1)%mod][i + 1][j] = max(dp[(r+1)%mod][i + 1][j], dp[r][i][j] + gg(r, 1));
                    dp[(r+2)%mod][i][j + 1] = max(dp[(r+2)%mod][i][j + 1], dp[r][i][j] + gg(r, 2));
                    if(i + j + 1 == n) bad = 0;
                }
        //cout << cnt[1] << " " << cnt[2] << endl;
        return dp[sm][cnt[1]][cnt[2]] + cnt[0];
    }
    memset(Dp, -63, sizeof dp);
    Dp[0][0][0][0] = 0;
    for(int i=0; i<=cnt[1]; i++)
            for(int j=0; j<=cnt[2]; j++)
                for(int k=0; k<=cnt[3]; k++){
                    for(int r=0; r<4; r++){
                        if(i + j + k + 1 == n) bad = 1;
                        Dp[(r+1)%mod][i + 1][j][k] = max(Dp[(r+1)%mod][i + 1][j][k], Dp[r][i][j][k] + gg(r, 1));
                        Dp[(r+2)%mod][i][j + 1][k] = max(Dp[(r+2)%mod][i][j + 1][k], Dp[r][i][j][k] + gg(r, 2));
                        Dp[(r+3)%mod][i][j][k + 1] = max(Dp[(r+3)%mod][i][j][k + 1], Dp[r][i][j][k] + gg(r, 3));
                        if(i + j + k + 1 == n) bad = 0;
                    }
            }
    return Dp[sm][cnt[1]][cnt[2]][cnt[3]] + cnt[0];
}
int main(){
    IOS;
     freopen("AL.in", "r", stdin);
     freopen("AL.txt", "w", stdout);
    int T;
    cin >> T;
    for(int i=1; i<=T; i++){
        cout << "Case #" << i << ": ";
        cout << pros() << endl;
    }
}
