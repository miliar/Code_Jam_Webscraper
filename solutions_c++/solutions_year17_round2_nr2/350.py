#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

typedef long long LL;
#define rep(it,s) for(__typeof((s).begin()) it=(s).begin();it!=(s).end();it++)

int n;
int v[6], w[6];
int c[1010];
char col[] = {'R', 'O', 'Y', 'G', 'B', 'V'};

int main() {

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int tt;
    cin>>tt;
    for (int cas=1; cas<=tt; cas++) {
        cin>>n;
        for (int j=0; j<6; j++) cin>>v[j];
        for (int i=0; i<6; i++) w[i] = v[i];

        int last = -1;
        bool bad = false;
        for (int i=0; i<n-8; i++) {

            int best = 0;
            int sel = -1;
            for (int j=0; j<6; j++) {
                if (j != last && v[j] > best) {
                    sel = j;
                    best = v[j];
                }
            }

            if (sel == -1) {
                bad = true;
            }
            else {
                c[i] = sel;
                v[sel]--;
                last = sel;
            }
        }

        int m = min(8, n);
        vector<int> all;
        for (int i=0; i<6; i++) {
            for (int j=0; j<v[i]; j++) all.push_back(i);
        }

        sort(all.begin(), all.end());
        bool finish = false;
        do {

            bool good = true;
            for (int i=0; i<all.size()-1; i++) {
                if (all[i] == all[i+1]) good = false;
            }

            if (m != n) {
                if (all[0] == c[n-9]) good = false;
                if (all[m-1] == c[0]) good = false;
            }
            else {
                if (all[0] == all[m-1]) good = false;
            }

            if (good) {
                finish = true;
                int k = 0;
                for (int i=n-m; i<n; i++) c[i] = all[k++];
            }

        } while (next_permutation(all.begin(), all.end()) && !finish);

        if (!finish) {
            printf("Case #%d: IMPOSSIBLE\n", cas);
        }
        else {
            printf("Case #%d: ", cas);
            for (int i=0; i<n; i++) cout<<col[c[i]];
            cout<<endl;
        }

    }

    return 0;

}
