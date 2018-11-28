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

int d, n;
int k[1010], s[1010];
double t[1010];

int main() {

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int tt;
    cin>>tt;
    for (int cas=1; cas<=tt; cas++) {

        cin>>d>>n;
        for (int i=0; i<n; i++) {
            cin>>k[i]>>s[i];
        }

        double t = 0.0;
        for (int i=0; i<n; i++) {
            t = max(t, 1.0*(d-k[i])/s[i]);
        }

        double res = d / t;

        printf("Case #%d: %.12f\n", cas, res);
    }

    return 0;

}
