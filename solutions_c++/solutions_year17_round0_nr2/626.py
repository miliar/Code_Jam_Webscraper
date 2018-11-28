#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <sstream>
#include <vector>
#include <list>
#include <deque>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <utility>
#include <algorithm>
#include <limits>
#include <iomanip>
#include <bitset>

#define INF 1000000000
#define Inf 1000000000000000000
#define mp make_pair
#define pb push_back
#define EPS 1e-9

using namespace std;

typedef long long ll;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<vii> vvii;

int t;
string n;
int main() {
    // freopen("in","r",stdin);
    // freopen("out","w",stdout);

    cin >> t;
    for(int cas = 1; cas <= t; ++cas) {
        cin >> n;
        for(int i = n.size() - 2; i >= 0; --i) {
            if (n[i] > n[i + 1]) {
                --n[i];
                for(int j = i + 1; j < n.size(); ++j) n[j] = '9';
            }
        }
        if (n[0] == '0') cout << "Case #" << cas << ": " << n.substr(1, n.size() - 1) << endl;
        else cout << "Case #" << cas << ": " << n << endl;
    }
    return 0;
}
