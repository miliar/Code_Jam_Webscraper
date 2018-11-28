#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <deque>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>
using namespace std;

#ifdef OLYMP_HXLOCAL
	#define P(expr) (cerr << "[line " << __LINE__ << "] " << #expr << ": " << expr << '\n')
#else
	#define P(expr)
#endif

#define len(arr) ((int)(arr).size())

typedef long long ll;

int main() {
#ifndef OLYMP_HXLOCAL
	cin.tie(0);
	ios_base::sync_with_stdio(false);
#endif

	int T;
    cin >> T;
    for (int no = 1; no <= T; no++) {
        string s;
        cin >> s;

        s = '0' + s;
        int j;
        for (j = 0; j < len(s) - 1; j++)
            if (s[j] > s[j + 1])
                break;
        if (j < len(s) - 1) {
            while (s[j] == s[j - 1])
                j--;
            s[j]--;
            for (int k = j + 1; k < len(s); k++)
                s[k] = '9';
        }

        while (s[0] == '0')
            s = s.substr(1);
        cout << "Case #" << no << ": " << s << '\n';
    }
	return 0;
}
