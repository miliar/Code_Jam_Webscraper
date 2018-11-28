#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <cstring>
#include <stdlib.h>
#include <cmath>
#include <map>
#include <queue>
#include <set>
using namespace std;

int T;
typedef long long ll;
pair<ll,ll> pii[1010];
int main() {
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    cin >> T;
    ll D;
    int N;
    int C = 1;
    while (T --) {
        cin >> D >> N;
        for (int i = 0;i < N;i ++) {
            cin >> pii[i].first >> pii[i].second;
        }
        sort(pii,pii + N);
        int cur = 0;
        while(1) {
            if (cur + 1 < N && pii[cur].second > pii[cur + 1].second) {
                double t1 = (D - pii[cur + 1].first) * 1.0 / pii[cur + 1].second;
                double t2 = (pii[cur + 1].first - pii[cur].first) * 1.0 / (pii[cur].second - pii[cur + 1].second);
                if (t2 < t1) {
                    cur ++;
                }
                else {
                    break;
                }
            }
            else {
                break;
            }
        }
        double tt = (D - pii[cur].first) * 1.0 / pii[cur].second;
        double v = D / tt;
        printf("Case #%d: %.6f\n",C ++,v);
    }
}



