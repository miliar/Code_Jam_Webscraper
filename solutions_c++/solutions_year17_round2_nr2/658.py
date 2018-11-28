#include <iostream>
#include <cstdio>
#include <string>
#include <algorithm>
#include <unordered_set>
#include <cmath>
#include <set>
#include <unordered_map>
#include <map>
#include <functional>
#include <iomanip>
#include <vector>
#include <utility>

using namespace std;

typedef long long ll;
typedef long double ld;

const bool debug = false;

string solve (){

    int N, R, Or, Y, G, B, V;
    cin >> N >> R >> Or >> Y >> G >> B >> V;
    vector<pair<int, char>> q = {{R, 'R'}, {Y, 'Y'}, {B, 'B'}};
    sort(q.begin(), q.end());
    if(q[0].first + q[1].first < q[2].first) {
        return "IMPOSSIBLE";
    }
    else {
        int n = R + Y + B;
        string str(n, '0');
        int i = 0;
        int rem = (q[1].first + q[0].first) % q[2].first;
        if(q[0].first == q[2].first) {
            rem = q[0].first;
        }
        while(i < n) {
            str[i] = q[2].second;
            i++;
            if(q[1].first > 0) {
                str[i] = q[1].second;
                q[1].first--;
                i++;
                if(rem > 0) {
                   str[i] = q[0].second;
                   i++;
                   rem--;
                }
            }
            else  {
                str[i] = q[0].second;
                i++;
            }
        }
        return str;
    }


}

int main() {
   ios_base::sync_with_stdio(false);
   if(!debug) {
        freopen("small.in", "r", stdin);
        freopen("small.out", "w", stdout);
    }
    int t;
    cin >> t;
    int i;
    for(i = 1; i <= t; i++) {
        cout << "Case #" << i << ": " << solve() << '\n';


        cerr << "Case " << i << '\n';
    }
    return 0;
}
