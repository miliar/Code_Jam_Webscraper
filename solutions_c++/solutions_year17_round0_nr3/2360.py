#include <bits/stdc++.h>
using namespace std;
#define forsn(i, s, n) for (int i = s; i < n; i++)
#define forn(i, n) forsn(i, 0, n)
#define dforsn(i, s, n) for (int i = n - 1; i >= s; i--)
#define dforn(i, n) dforsn(i, 0, n)
#define pb push_back
#define fst first
#define snd second
#define tint long long
#define uint unsigned tint
#define debug(v) cerr << #v << " = " << v << '\n';

int main() {
    tint t;

    cin >> t;

    forn(tt,t) {
        cout << "Case #" << tt+1 << ": ";

        uint n, k;

        cin >> n >> k;

        map<uint,uint> q;
        q.emplace(n,1);

        uint ocup = 0;
        uint lastNum = n;

        while(ocup < k) {
            auto it = q.rbegin();
            uint num = it->first;
            uint cnt = it->second;

            q.erase(num);

            q[num/2] += cnt;
            q[(num-1)/2] += cnt;

            lastNum = num;
            ocup += cnt;
        }

        cout << lastNum/2 << " " << (lastNum-1)/2 << endl;
    }

    return 0;
}
