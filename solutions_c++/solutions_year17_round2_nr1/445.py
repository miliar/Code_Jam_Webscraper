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

int main(){
    IOS;
    freopen("AL.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;
    cin >> T;
    for(int it=0; it<T; it++){
        int D, n;
        cin >> D >> n;
        ld mn = 1e15;
        for(int i=0; i<n; i++){
            ld fir, sor;
            cin >> fir >> sor;
            ld zrb = ld(D) / ld(D - fir);
            mn = min(mn, sor * zrb);
        }
        cout << "Case #" << it + 1 << ": " << setprecision(12) << mn << endl;
    }
}
