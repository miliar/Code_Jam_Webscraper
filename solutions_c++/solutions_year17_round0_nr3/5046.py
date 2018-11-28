#include <iostream>
#include <cstdio>
#include <map>
#include <vector>
#include <algorithm>
#include <set>
#include <queue>
#include <cmath>
using namespace std;

void insertar (map<int, int>& s, int elem) {
    if (elem == 0)
        return;
    s[elem]++;
}

int main () {
    freopen("c.in", "r", stdin);
    freopen("c.out", "w", stdout);

    int t, res1, res2;
    cin >> t;
    
    long long int n, k;
    for (int tc = 1; tc <= t; tc++) {
        cin >> n >> k;
        
        cout << "Case #" << tc << ": ";
        
        map<int, int> s;
        s[n] = 1;
        for (int i = 0; i < k && !s.empty(); i++) {
            int tmp = s.rbegin()->first; // get max value
            s[tmp]--;
            
            if (s[tmp] == 0)
                s.erase(tmp);
            
            if (tmp % 2 == 0) {
                insertar(s, tmp / 2);
                insertar(s, tmp / 2 - 1);
                res1 = tmp / 2;
                res2 = tmp / 2 - 1;
            }
            else {
                insertar(s, tmp / 2);
                insertar(s, tmp / 2);
                res1 = tmp / 2;
                res2 = tmp / 2;
            }
        }
        
        if (s.empty()) {
            cout << 0 << " " << 0 << endl;
        }
        else {
            cout << res1 << " " << res2 << endl;
        }
    }
}

