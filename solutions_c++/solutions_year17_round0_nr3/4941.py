#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <cmath>
#include <deque>
#include <queue>
#include <stack>
#include <cstdio>

#define pb push_back
#define mp make_pair

using namespace std;

typedef long long ll;
typedef long double ld;
typedef unsigned int ui;
typedef unsigned long long int ull;

typedef pair<int, int> int_pair;

const int INF = 2147483647;
const ll LLINF = 9223372036854775807;


int main(){
    freopen("C-small-2-attempt0.in", "r", stdin);
    freopen("main.out", "w", stdout);
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int n, k;
        cin >> n >> k;
        set<int_pair> q;
        q.insert(make_pair(-n, 0));
        for (int i = 0; i < k - 1; i++) {
            int_pair old = *q.begin();
            int c = -old.first;
            int_pair ll, rr;
            ll = make_pair(-(c - c / 2 - 1), old.second);
            rr = make_pair(-(c / 2), old.second + c - c/2);
            q.erase(old);
            // cout << ll.first << " " << rr.first << endl;
            if (ll.first < 0) q.insert(ll);
            if (rr.first < 0) q.insert(rr);
        }
        // cout << (*q.begin()).first << " " << (*q.begin()).second << endl;
        int ans = -(*q.begin()).first;
        int y = ans / 2;
        int z = ans - ans / 2 - 1;
        cout << "Case #" << t << ": " << y << " " << z << "\n";
    }
}
