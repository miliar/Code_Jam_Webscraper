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

bool p[1000010];
int n, k;

int get() {

    int mi = -1;
    int ma = -1;
    int l = 1000000;

    for (int i=1; i<=n; i++) if (!p[i]) {

        int ll = 0;
        int rr = 0;

        for (int j=i-1; j>=1; j--) {
            if (p[j]) break;
            else ll++;
        }
        for (int j=i+1; j<=n; j++) {
            if (p[j]) break;
            else rr++;
        }

        if (min(ll, rr) > mi) {
            mi = min(ll, rr);
            ma = max(ll, rr);
            l = i;
        }
        else if (min(ll, rr) == mi && max(ll, rr) > ma) {
            mi = min(ll, rr);
            ma = max(ll, rr);
            l = i;
        }
    }

    return l;
}

int main() {

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int t;
    cin>>t;
    for (int cas=1; cas<=t; cas++) {

        cin>>n>>k;
        /*
        n = cas;

        for (int i=0; i<n+2; i++) p[i] = 0;
        p[0] = p[n+1] = 1;

        cout<<n<<"-->"<<endl;

        for (int i=0; i<n; i++) {

            int x = get();

            p[x] = 1;

            cout<<x<<" ";

        }

        cout<<endl;
        */

        vector<int> all;
        priority_queue<pair<int, pair<int,int> > > v;
        v.push(make_pair(n, make_pair(-1, -n)));

        while (!v.empty() && all.size() < k) {
            pair<int,int> intv = v.top().second;
            intv.first = -intv.first;
            intv.second = -intv.second;
            v.pop();

             if (intv.first > intv.second) {
                continue;
             }

            int x = (intv.second + intv.first) / 2;

            all.push_back(x);

            //cout<<x<<endl;

            if (intv.first != intv.second) {
                v.push(make_pair(x-1-intv.first+1, make_pair(-intv.first, -x+1)));
                v.push(make_pair(intv.second-x-1+1, make_pair(-x-1, -intv.second)));
            }
        }

        //for (int i=0; i<all.size(); i++) cout<<all[i]<<" "; cout<<endl;

        //cout<<endl;

        int mi = 0;
        int ma = 0;
        int l = 0;
        int r = 0;
        for (int i=1; i<=n; i++) p[i] = 0;
        p[0] = p[n+1] = 1;
        for (int i=0; i<k-1; i++) p[all[i]] = 1;

        //for (int i=0; i<=n+1; i++) cout<<p[i]; cout<<endl;

        for (int j=all[k-1]+1; j<=n; j++) {
            if (p[j]) break;
            else r++;
        }
        for (int j=all[k-1]-1; j>=1; j--) {
            if (p[j]) break;
            else l++;
        }

        mi = min(l, r);
        ma = max(l, r);

        printf("Case #%d: %d %d\n", cas, ma, mi);

    }

    return 0;

}
