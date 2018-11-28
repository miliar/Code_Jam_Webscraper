#include <iostream>
#include <queue>
#include <cstdlib>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <stack>
#include <iomanip>

#define FOR(i,x,y) for(int i =(int)(x); i<(int)(y); i++)
#define REP(i, N) FOR(i, 0, N)
#define SZ(x) (int)x.size()

using namespace std;

typedef vector<int> vin;
typedef pair<int, int> pii;
typedef vector<pair<int, int> > vpii;
typedef vector<vector<int> > vvin;

typedef long long LL;
typedef unsigned long long ULL;

void set_nines(string &num, int start) {
    for (int i = start; i < int(num.size()); ++i) {
        num[i] = '9';
    }
}

int main ()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int T; cin >> T;
    for (int t = 1; t <= T; ++t) {
        string num; cin >> num;
        int max_dig = num[num.size() - 1] - '0';    // Max dig to right
        for (int i = int(num.size()) - 2; i >= 0; --i) {
            int cur_dig = int(num[i] - '0');
            if (cur_dig > max_dig) {
                max_dig = cur_dig - 1;
                num[i] = num[i] - 1;
                set_nines(num, i + 1);
            }
            max_dig = min(cur_dig, max_dig);
        }

        // Trim leading 0s
        int i = 0;
        for (i = 0; i < int(num.size()); ++i) {
            if (num[i] != '0')
                break;
        }

        cout << "Case #" << t << ": ";
        for (int j = i; j < int(num.size()); ++j)
            cout << num[j];
        cout << endl;
    }

    return 0;
}
