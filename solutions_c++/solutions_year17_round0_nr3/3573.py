#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pi;

#define F first
#define S second
#define PB push_back
#define MP make_pair
#define REP(i,a,b) for(int i = a; i <= b ;i++)

int main()
{
    //freopen("in.txt", "r", stdin);
    //freopen("out.txt", "w", stdout);

    ios_base::sync_with_stdio(false);cin.tie(NULL);

    int n,ac = 0;
    cin >> n;
    while(n--){
        ll p, k, ans = 0, Mx, Mn;
        map <ll, ll> Mp;
        cin >> p >> k;
        cout << "Case #" << ++ac << ": ";
        Mp[p + 1]++;
        while(ans < k) {
            ll r = Mp.rbegin()->F;
            ll f = Mp[r];
            Mp.erase(r);
            ans += f;
            Mp[r >> 1] += f;
            Mp[r + 1 >> 1] += f;
            Mx = r + 1 >> 1;
            Mn = r >> 1;

        }
        cout << Mx-1 << " " << Mn-1 << endl;
        }
    return 0;
}
