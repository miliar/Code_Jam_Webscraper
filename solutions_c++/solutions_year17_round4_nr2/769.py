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
const int maxn = 1000 + 10;
int cnt[maxn][maxn], sm[maxn], tot[maxn];
void pros(){
    int n, c, m;
    cin >> n >> c >> m;
    memset(cnt, 0, sizeof cnt);
    memset(sm, 0, sizeof sm);
    memset(tot, 0, sizeof tot);
    int mx = 0;
    for(int i=0; i<m; i++){
        int p, id;
        cin >> p >> id;
        p--, id--;
        cnt[p][id]++;
        sm[id]++;
        mx = max(mx, sm[id]);
        tot[p]++;
    }
    int lo = 0, hi = m;
    int num = 0;
    while(hi - lo > 1){
        int mid = hi + lo >> 1;
        int cur = 0;
        bool can = 1;
        int ted = 0;
        if(mid < mx) can = 0;
        else{
            for(int i=n-1; i>=0; i--){
                int x = tot[i] + cur;
                if(x <= mid){
                    ted += cur;
                    cur = 0;
                }
                else
                    cur = x - mid;
            }
            if(cur) can = 0;
        }
        if(can)
            hi = mid, num = ted;
        else
            lo = mid;
    }
    cout << hi << " " << num << endl;
}
int main(){
    IOS;
    freopen("BS.in", "r", stdin);
    freopen("BS.txt", "w", stdout);
    int T;
    cin >> T;
    for(int i=1; i<=T; i++){
        cout << "Case #" << i << ": ";
        pros();
    }

}
