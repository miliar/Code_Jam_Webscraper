/// In the name of God
#include <bits/stdc++.h>
#define int long long
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
map<int,int> cnt;
inline int most(){
    int t;
    for(auto it : cnt)
        t = it.X;
    return t;
}
int gg(int n,int k){
    cnt.clear();
    cnt[n] = 1;
    while(1){
        int x = most();
        if(cnt[x] >= k)
            return x;
        k -= cnt[x];
        cnt[(x - 1)/2] += cnt[x];
        cnt[x/2] += cnt[x];
        cnt[x] = 0;
        cnt.erase(x);
    }
}
main(){
    IOS;
    freopen("CL.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;
    cin >> T;
    for(int it=0; it<T; it++){
        int n, k;
        cin >> n >> k;
        int x = gg(n, k);
        cout << "Case #" << it+1 << ": " << x/2 << " " << (x-1)/2 << endl;
    }
}
