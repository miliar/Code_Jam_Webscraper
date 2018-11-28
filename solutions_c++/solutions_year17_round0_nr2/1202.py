#include <bits/stdc++.h>

#define PI 3.14159265358979323846
#define EPS 1e-6
#define INF 1000000000

#define _ ios_base::sync_with_stdio(0), cin.tie(0), cin.tie(0), cout.tie(0), cout.precision(15);
#define FOR(i, a, b) for(int i=int(a); i<int(b); i++)
#define RFOR(i, a, b) for(int i=int(a)-1; i>=int(b); i--)
#define FORC(cont, it) for(decltype((cont).begin()) it = (cont).begin(); it != (cont).end(); it++)
#define RFORC(cont, it) for(decltype((cont).rbegin()) it = (cont).rbegin(); it != (cont).rend(); it++)
#define pb push_back

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;

#define MAXN 10
#define MOD 1000000007

string solve(string s) {
    bool b = true;

    while(s.find("0") == 0) {
        s = s.substr(1);
    }

    while (b) {
        b = false;
        for (int i = 0, j = 1; j < s.length(); i ++, j ++) {
            if (s[i] > s[j]) {
                b = true;
                s[i] --;
                for(; j < s.length(); i ++, j ++) {
                    s[j] = '9';
                }
            }
        }

        while(s.find("0") == 0) {
            s = s.substr(1);
        }
    }

    return s;
}


int main() { _
    int T;
    string n;

    freopen("b.in", "r", stdin);
    freopen("b.out", "w", stdout);

    cin >> T;
    FOR (t, 1, T + 1) {
        cin >> n;

        cout << "Case #" << t << ": " << solve(n) << endl;
    }



    return 0;
}

