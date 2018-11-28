#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <queue>
#include <cassert>
#include <unordered_map>
#include <fstream>
#define ll long long
#define F first
#define S second
#define MOD 1000000007
#define MAX 200001
#define BUGGY 0
using namespace std;
pair<ll, ll> solve(ll n, ll k, ll done = 1) {
    if (k == 1) {
        return {(n - 1) / 2 + (n - 1) % 2, (n - 1) / 2};
    }
    ll large = (n - 1) / 2 + (n - 1) % 2, small = (n - 1) / 2, lCount = 1, sCount = 1;
    k -= 1;
    done = 2;
    while(k > 0) {
        if (k <= lCount) {
            return {max(0ll, (large - 1) / 2 + (large - 1) % 2), (large - 1) / 2};
        } else if (k <= done){
            return {max(0ll, (small - 1) / 2 + (small - 1) % 2), (small - 1) / 2};
        }
        ll tl = 0, ts = 0;
        if (large % 2 == 1) {
            tl += lCount * 2;
        } else {
            tl += lCount;
            ts += lCount;
        }
        if (small % 2 == 1) {
            ts += sCount * 2;
        } else {
            tl += sCount;
            ts += sCount;
        }
        lCount = tl, sCount = ts;
        large = (large - 1) / 2 + (large - 1) % 2;
        small = (small - 1) / 2;
        k -= done;
        done *= 2;
        assert((lCount + sCount) == done);
    }
    return {0, 0};
}
int main(){
    ifstream cin("/Users/shikhar.s/Downloads/C-large.in");
    //ifstream cin("/Users/shikhar.s/Desktop/Competitive/Competitive/a.txt");
    ofstream cout("/Users/shikhar.s/Desktop/Competitive/Competitive/b.txt");
    int t;
    cin >> t;
    int T = 1;
    while (t--) {
        ll n, k;
        cin >> n >> k;
        pair<ll, ll> ans = solve(n, k);
        cout << "Case #" << T++ << ": " << ans.F << " " << ans.S << "\n";
    }
    printf("Done!");
    return 0;
}

