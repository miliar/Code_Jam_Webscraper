#include <iostream>
#include <sstream>
#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <cstring>
#include <cmath>
using namespace std;

#define Rep(i,n) for(int i=0;i<(n);++i)
#define For(i,a,b) for(int i=(a);i<=(b);++i)
#define Ford(i,a,b) for(int i=(a);i>=(b);--i)
#define fi first
#define se second
#define pb push_back
#define MP make_pair

typedef pair<int,int> PII;
typedef vector<int> VI;

bool a[1010];

int main() {
    int nt;
    cin >> nt;
    Rep(t,nt) {
        string s;
        int k;
        cin >> s >> k;
        int n = s.length();
        Rep(i, n) a[i] = (s[i] == '+');
        int count = 0;
        Rep(i, n) if (a[i] == false && i + k <= n) {
            ++count;
            Rep(j, k) a[i + j] = !a[i + j];
        }
        bool ok = true;
        Rep(i, n) if (!a[i]) ok = false;
        cout << "Case #" << (t + 1) << ": ";
        if (ok) cout << count;
        else cout << "IMPOSSIBLE";
        cout << endl;
    }
    return 0;
}
