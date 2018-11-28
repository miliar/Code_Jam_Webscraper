#include <bits/stdc++.h>
using namespace std;

#define int long long
#define ll long long
#define vi vector<int>
#define REP(i, n) for (int i = 0; (i) < (int)(n); ++i)
#define FOR(i, a, b) for (int i = (int)a, _b = b; i <= _b; ++i)
#define FORD(i, a, b) for (int i = (int)a ,_b = b; i >= _b; --i)

#define MAX(a, b) (a > b ? a : b)
#define MIN(a, b) (a < b ? a : b)

#define DEBUG(X) { cerr << #X << " = " << (X) << endl; }

#define MAXN 7100

int GI(int &a){return scanf("%I64d", &a);}

int n, i, j, k, tmp, m, x, b, t;

vi v1, v2, v3;
int a[20];
int numDigit(int x){
    int r = 0;
    while (x > 0){
        ++r;
        x /= 10;
    }
    return r;
}

int32_t main(){
    freopen("blarge.in", "rt", stdin);
    freopen("blarge.out", "wt", stdout);
    ios_base::sync_with_stdio(false);

    string s;
    cin >> t;
	REP(z, t){
        cin >> n;
        int dig = numDigit(n);
        int pos = dig - 1;
        while (n > 0){
            a[pos--] = n % 10;
            n /= 10;
        }
        while (1){
            int ok = 1;
            REP(i, dig - 1)
                if (a[i] > a[i + 1]){
                    ok = 0;
                    a[i]--;
                    FOR(j, i + 1, dig - 1)
                        a[j] = 9;
                    break;
                }
            if (ok)
                break;
        }

        cout << "Case #" << z + 1 << ": ";
        pos = 0;
        while (a[pos] == 0)
            ++pos;
        while (pos < dig)
            cout << a[pos++];
        cout << "\n";
	}
}
