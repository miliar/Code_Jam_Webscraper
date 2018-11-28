#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <sstream>
#include <string>
using namespace std;

typedef pair<long long, long long> pr;

int main () {
    int cases;
    cin >> cases;

    for (int cc = 1; cc <= cases; ++cc) {
        long long n, k;
        cin >> n >> k;
        map<long long, long long> mp;
        mp[n] = 1;
        long long solSpace = 0;
        long long remain = k;
        while (true) {
            pr cur = *mp.rbegin();
            //cerr << cur.first << ' ' << cur.second << ' ' << remain << endl;
            if (cur.second >= remain) {
                solSpace = cur.first - 1;
                break;
            } else {
                remain -= cur.second;
                int space = cur.first;
                mp.erase(space);
                --space;
                long long cnt1 = (mp.find(space / 2) == mp.end() ? 0 : mp[space / 2]) + cur.second;
                mp[space/2] = cnt1;
                long long cnt2 = (mp.find(space - space / 2) == mp.end() ? 0 : mp[space - space / 2]) + cur.second;
                mp[space - (space/2)] = cnt2;
            }
        }
        cout << "Case #" << cc << ": " << (solSpace - solSpace / 2) << ' ' << (solSpace / 2) << endl;
    }
}
