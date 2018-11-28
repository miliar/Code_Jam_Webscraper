#include <bits/stdc++.h>
#define INF 100000000000005
#define MAXN 2000
#define mod 1000000007
#pragma comment(lib, "user32")

using namespace std;

#define F first
#define S second
#define MP make_pair
#define all(x) (x).begin(), (x).end()

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;

int main() {
        freopen("B-large.in", "r", stdin);
        freopen("outc.txt", "w", stdout);
        int t; cin >> t;
        string s;

        for(int z = 0; z < t; ++z) {
            cin >> s;
            int maxn = s[0] - '0', index = s.size();
            int f = 0;
            for(int i = 1; i < s.size(); ++i) {
                if( (int)(s[i] - '0') < maxn ) {
                    f = i;
                    break;
                }
                else {
                    maxn = (int)(s[i] - '0');
                }
            }
            if(f == 0) {
                cout << "Case #" << z + 1 << ": " << s << endl;
                continue;
            }
            else {
                f = 0;
                for(int i = 0; i < s.size(); ++i) {
                    if(f == 0) {
                        if((int)(s[i]-'0') == maxn) {
                            s[i] -= 1;
                            f = 1;
                        }
                    }
                    else {
                        s[i] = '9';
                    }
                }
                while(true) {
                    if(s[0] == '0') {
                        s.erase(0, 1);
                    }
                    else break;
                }
                cout << "Case #" << z + 1 << ": " << s << endl;
            }

        }
}
