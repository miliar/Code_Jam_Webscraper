#include <bits/stdc++.h>
#define rep(a,b,c) for(int a = b; a < c; a++)
#define ll long long
#define s second
#define f first
#define pb push_back

using namespace std;

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	freopen("/afs/ms/u/m/mo08/Downloads/in.txt", "r", stdin);
	freopen("/afs/ms/u/m/mo08/Downloads/out.txt", "w", stdout);
	int t, t0, k, n;
	cin >> t;
	t0 = t;
	string s;
	int out;
	while(t-->0) {
        cin >> s >> k;
        n = s.size();
        out = 0;
        rep(i, 0, n-k+1) {
            if(s[i] == '-') {
                rep(j, 0, k) {
                    if(s[i+j] == '-') s[i+j] = '+';
                    else s[i+j] = '-';
                }
                out++;
            }
        }
        rep(i, n-k+1, n) {
            if(s[i] == '-') out = -1;
        }
        cout << "Case #" << t0-t << ": ";
        if(out < 0) cout << "IMPOSSIBLE" << endl;
        else cout << out << endl;
	}
	return 0;
}
