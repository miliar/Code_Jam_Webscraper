#include <bits/stdc++.h>
#define ll long long
#define ull unsigned long long
#define pi acos(-1.0)
#define rf freopen("in.txt", "r", stdin);
#define ld long double
#define all(v) v.begin(),v.end()
#define pb push_back
#define ff first
#define ss second
#define sz size()
#define ln length()
#define REP(i,a) for(int i=0;i<a;++i)
#define REPP(i,a,b) for(int i=a;i<b;++i)
#define s(n) scanf("%d",&n);
#define sl(n) scanf("%lld",&n);
#define sld(n) scanf("%lf", &n);

using namespace std;

long long tonum(string s) { stringstream ss; long long n; ss << s; ss >> n; return n; }

bool check(string p) {
    for (int i = 1; i < p.length(); i++) {
        if (p[i - 1] > p[i]) {
            return false;
        }
    }
    return true;
}

int main() { //rf
                //freopen("out.txt", "w", stdout);
    int t;
    s(t);
    for (int x = 1; x <= t; x++) {
        string s; cin >> s;
        ll res = 0;
        while (not check(s)) {
            for (int i = 1; i < s.length(); i++) {
                if (s[i] < s[i - 1]) {
                    s[i - 1]--;
                    int j = i;
                    while (i < s.length()) {
                        s[i] = '9';
                        i++;
                    }
                    break;
                }
            }
        }

        ll answer = tonum(s);
        cout << "Case #" << x << ": " << answer << endl;
    }
    return 0;
}
