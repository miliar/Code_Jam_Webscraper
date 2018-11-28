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
#include <functional>
#include <set>
using namespace std;

typedef long long ll;
typedef pair<ll,ll> pii;
int T;
int n,m;
pii a[1010];
const double pi = acos(-1.0);

int main() {
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
	int CC = 1;
	cin >> T;
	while (T --) {
        priority_queue<ll,vector<ll>,greater<ll> > que;
        cin >> n >> m;
        for (int i = 0;i < n;i ++) {
            cin >> a[i].first >> a[i].second;
        }
        sort(a, a + n);
        ll sum = 0;
        for (int i = 0;i < m - 1;i ++) {
            que.push(a[i].first * a[i].second);
            sum += a[i].first * a[i].second;
        }
        double maxs = 0;

        for (int i = m - 1;i < n;i ++) {
			maxs = max(maxs, sum * 2 * pi + pi * a[i].first * a[i].first + 2 * pi * a[i].first * a[i].second);
            que.push(a[i].first * a[i].second);
            sum += a[i].first * a[i].second;
            sum -= que.top();
            que.pop();
        }
		printf("Case #%d: %.7f\n",CC ++,maxs);
	}
}
