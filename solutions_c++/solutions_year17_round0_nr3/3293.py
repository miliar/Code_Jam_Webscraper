#include <iostream>
#include <map>
#include <utility>

using namespace std;

pair<long, long> split_stall(long n) {
    if (n & 0x01) {
        return make_pair(n >> 1, n >> 1);
    } else {
        return make_pair((n >> 1) - 1, n >> 1);
    }
};


int main() {

    int t;
    long k, n;
    map<long, long> stk;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        cin >> n >> k;
        stk.clear();
        stk[n] = 1;
        pair<long, long> par;
        long cnt = 0;
        while (cnt < k) {
            auto p = stk.end();
            --p;
            par = split_stall(p->first);

            stk[par.first] += p->second;
            stk[par.second] += p->second;

            cnt += p->second;
            stk.erase(p);
        }


        cout << "Case #" << i << ": " << par.second << " " << par.first << endl;
    }


    return 0;
}