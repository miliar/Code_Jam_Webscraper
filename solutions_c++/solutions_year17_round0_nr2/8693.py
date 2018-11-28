#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <climits>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <list>
#include <queue>
#include <set>
#include <map>
#include <unordered_map>
#include <functional>
#include <bitset>
using namespace std;

typedef long long ll;
ll f(ll n) {
    if (n<=9) return n;
    ll rhs=n%10, t=rhs, idx=1;
    while (n/10) {
        n/=10;
        idx*=10;
        int lhs=n%10;
        if (lhs>rhs) t=lhs*idx-1;
        else t+=lhs*idx;
        rhs=t/idx;
    }
    return t;
}
int main() {
    int ntc;
    cin>>ntc;
    for (int tc=1; tc<=ntc; ++tc) {
        ll t;
        cin>>t;
        cout<<"Case #"<<tc<<": "<<f(t)<<'\n';
    }
    return 0;
}