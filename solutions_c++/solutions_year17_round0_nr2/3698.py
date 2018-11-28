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
	bool c;
	cin >> t;
	t0 = t;
	string s;
	int out;
	while(t-->0) {
        cin >> s;
        n = s.size();
        do {
            c = 0;
            for(int i = n-1; i >= 1; i--) {
                if(s[i] < s[i-1]) {
                    rep(j, i, n) s[j] = '9';
                    s[i-1]--;
                    c = 1;
                }
            }
        } while(c);
        if(s[0] == '0') s.erase(s.begin());
        cout << "Case #" << t0-t << ": ";
        cout << s << endl;
	}
	return 0;
}
