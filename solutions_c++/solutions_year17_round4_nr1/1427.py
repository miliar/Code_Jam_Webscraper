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


int solve () {
    int n;
    int p;
    cin >> n >> p;
    int ct = 0;
    vector<int> arr(n);
    int i;
    for(i = 0; i < n; i++) {
        cin >> arr[i];
    }
    if(p == 2) {
        int rem[2] = {0, 0};
        for(int x: arr) {
            rem[x % 2]++;
        }
        ct += rem[0];
        ct += rem[1] / 2;
        ct += rem[1] % 2;
    }
    else if(p == 3) {

        int rem[3] = {0, 0, 0};
        for(int x: arr) {
            rem[x % 3]++;
        }
        ct += rem[0];
        if(rem[1] <= rem[2]) {
            ct += rem[1];
            rem[2] -= rem[1];
            ct += rem[2] / 3;
            rem[2] %= 3;
            if(rem[2] != 0) {
                ct++;
            }
        }
        else {
            ct += rem[2];
            rem[1] -= rem[2];
            ct += rem[1] / 3;
            rem[1] %= 3;
            if(rem[1] != 0) {
                ct++;
            }

        }
    }
    else {
        int rem[4] = {0, 0, 0, 0};
        for(int x: arr) {
            rem[x % 4]++;
        }
        ct += rem[0];
        ct += rem[2] / 2;
        rem[2] %= 2;
        if(rem[1] <= rem[3]) {
            ct += rem[1];
            rem[3] -= rem[1];
            if(rem[2] > 0) {
                if(rem[3] >= 2) {
                    ct++;
                    rem[3] -= 2;
                    ct += rem[3] / 4;
                    if(rem[3] % 4 != 0) {
                        ct++;
                    }
                }
                else {
                    ct++;
                }
            }
            else {
                    ct += rem[3] / 4;
                    if(rem[3] % 4 != 0) {
                        ct++;
                    }
            }
        }
        else {

            ct += rem[3];
            rem[1] -= rem[3];
            if(rem[2] > 0) {
                if(rem[1] >= 2) {
                    ct++;
                    rem[1] -= 2;
                    ct += rem[1] / 4;
                    if(rem[1] % 4 != 0) {
                        ct++;
                    }

                }
                else {
                    ct++;
                }
            }
            else {
                ct += rem[1] / 4;
                if(rem[1] % 4 != 0) {
                    ct++;
                }
            }
        }

    }
    return ct;


}

int main() {
   ios_base::sync_with_stdio(false);
   if(!debug) {
        freopen("large.in", "r", stdin);
        freopen("large.out", "w", stdout);
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
