#include <iostream>
#include <vector>
#include "unordered_map"
#include <cmath>
#include <climits>
#include "queue"
#include "tuple"
#include <algorithm>

using ll=long long;
using ull=unsigned long long;
using namespace std;

int main() {
    freopen("../input.txt","r",stdin);
    freopen("../output.txt","w",stdout);
    int n;
    cin >> n;
    for(int i = 1; i <= n; ++i) {
        ull ln;
        cin >> ln;
        string ns = to_string(ln);
        int nsCount = ns.size();
        for(int j = nsCount - 1; j > 0; --j) {
            int cn = ns[j] - '0';
            int pn = ns[j - 1] - '0';
            if(cn < pn) {
                int li = j;
                while(li < nsCount && ns[li] != '9') {
                    ns[li] = '9';
                    ++li;
                }
                char pnc = '0' + pn - 1;
                ns[j - 1] = pnc;
            }
        }
        cout << "Case #" << i << ": " << stoull(ns) << endl;
    }
}
