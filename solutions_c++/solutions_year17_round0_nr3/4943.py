//Pranet Verma
#include <bits/stdc++.h>
using namespace std;
typedef map<long long, long long, greater<long long> > myMap;
long long recurse(int level, long long people, myMap cnt, long long k) {
    assert(cnt.size() <= 2);
    if (people >= k) {
        long long alreadyDone = (1LL << (level - 1)) - 1;
        for (auto x : cnt) {
            long long len = x.first;
            long long val = x.second;
            if (alreadyDone + val >= k) {
                return len;
            }
            else {
                alreadyDone += val;
            }
        }
        assert (false);
    }
    else {
        myMap ncnt;
        for (auto x : cnt) {
            long long len = x.first;
            long long val = x.second;
            if (len % 2 == 0) {
                ncnt[len / 2] += val;
                ncnt[len / 2 - 1] += val;
            }
            else {
                ncnt[len / 2] += 2 * val;
            }
        }
        return recurse(level + 1, people + (1LL << level), ncnt, k);
    }
}

int main() {
    std::ios::sync_with_stdio(false);
    cin.tie(0);
    int t, tt = 0;
    cin >> t;
    while (t--) {
        cout << "Case #"<< ++tt << ": ";
        long long n, k;
        cin >> n >> k;
        myMap cnt;
        cnt[n] = 1;
        long long activeLength = recurse(1, 1, cnt, k);
        if (activeLength % 2 == 0) {
            cout << activeLength / 2 << " " << activeLength / 2 - 1 << endl;
        }
        else {
            cout << activeLength / 2 << " " << activeLength / 2 << endl;
        } 
    } 
}