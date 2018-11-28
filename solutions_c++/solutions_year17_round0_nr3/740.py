#include <iostream>
#include <map>
#include <cassert>
#include <algorithm>
using namespace std;

void solve(const int &tc) {
    int64_t n,k;
    cin >> n >> k;
    
    if(n == k) {
        cout << "Case #" << tc << ": " << 0 << " " << 0 << endl;
        return;
    }

    map<int64_t,int64_t,greater<int64_t>> mp;
    mp[n] = 1LL;

    int64_t rem = k;
    int64_t dec = 1LL;

    while(rem > dec) {
        rem -= dec;
        map<int64_t,int64_t,greater<int64_t>> nmp;
        for(auto &pr:mp) {
            auto _x = pr.first, _y = pr.second;
            if(_x&1) nmp[_x>>1] += _y<<1;
            else {
                nmp[_x>>1] += _y;
                nmp[(_x>>1) - 1] += _y;
            }
            cerr << _x << ":" << _y << " ";
        }
        cerr << endl;
        mp = nmp;
        dec <<= 1;

        assert(nmp.size() <= 2);
    }

    int64_t x,y;
    auto ptr = mp.begin();
    if(rem > ptr->second) ptr++;
    assert(ptr != mp.end());

    /*
    if(rem == 0LL) {
        if(mp.size() == 1) {
            cout << "Case #" << tc << ": " << mp.begin()->first << " " << mp.begin()->first << endl;
        } else {
            cout << "Case #" << tc << ": " << mp.begin()->first << " " << (++mp.begin())->first << endl;
        }
        return;
    }*/

    auto val = ptr->first - 1;
    y = val >> 1;
    x = val - y;
    cout << "Case #" << tc << ": " << x << " " << y << endl;
}

int main() {
    int t; cin >> t;
    for(int i=1;i<=t;i++) solve(i);
}
