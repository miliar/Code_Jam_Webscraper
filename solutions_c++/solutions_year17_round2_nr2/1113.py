// A C program to implement Ukkonen's Suffix Tree Construction
// Here we build generalized suffix tree for two strings
// And then we find longest common substring of the two input strings
#include <stdio.h>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <iostream>
#include <string.h>
#include <string>
#include <stdlib.h>
#include <vector>
#include <cmath>
using namespace std;

typedef long long ll;
#define MAXN 105

ll t;

double n, d;
double eps = 1e-7;

string s = "ROYGBV";

ll cnt[7];

char res[1005];

int main()
{
    cin >> t;
    for (int cse = 1; cse <= t; cse++){
        memset(cnt, 0, sizeof(cnt));
        memset(res, '.', sizeof(res));
        cin >> n;
        for (int i = 0; i < 6; i++){
            cin >> cnt[i];
        }
        bool good = true;
        bool first = true;
        ll ind = 0;
        for (int i = 0; i < 6; i++){
            ll mxind = max_element(cnt, cnt+6) - cnt;
            while (cnt[mxind]){
                res[ind] = s[mxind];
                cnt[mxind]--;
                if (first){
                    ind+=2;
                    if (ind >= n){
                        first = false;
                        ind = 1;
                    }
                }
                else {
                    if (res[ind] == res[ind-1] ||
                        (ind < n-1 && res[ind] == res[ind+1])){
                        good = false;
                        break;
                    }
                    ind+=2;
                }
            }
            if (good == false){
                break;
            }
        }
        if (n > 1 && res[0] == res[int(n-1)]) {
            good = false;
        }
        string out = "";
        if (good){
            for (int i = 0; i < n; i++){
                out += res[i];
            }
        }
        else out = "IMPOSSIBLE";
        cout << "Case #" << cse << ": " << out << endl;
    }
    return 0;
}

