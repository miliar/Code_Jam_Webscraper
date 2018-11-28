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
pii b[1010];

int main() {
   freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
	int CC = 1;
	cin >> T;
	while (T --) {
        cin >> n >> m;
        if (n + m == 1) {
            cin >> a[0].first >> a[0].second;
            if (a[0].first < 720 && a[0].second > 720) {
                printf("Case #%d: %d\n",CC ++,2);
            }
            else {
                printf("Case #%d: %d\n",CC ++,2);
            }
        }else {
            if (n >= 2 || m >= 2) {
                cin >> a[0].first >> a[0].second;
                cin >> a[1].first >> a[1].second;
                sort(a,a + 2);
                int cnt = 0;
                if (a[0].first > 0) {
                    b[cnt].first = a[0].first;
                    b[cnt].second = 1;
                    cnt ++;
                }
                if (a[0].second < a[1].first) {
                    b[cnt].first = a[1].first - a[0].second;
                    b[cnt].second = 0;
                    cnt ++;
                }
                if (a[1].second < 1440) {
                    b[cnt].first = 1440 - a[1].second;
                    b[cnt].second = 1;
                    cnt ++;
                }
                sort(b,b + cnt);
                int cursum = 0;
                int pos = cnt - 1;
                int anscnt = 0;
                int fg = 0;
                while (cursum < 720 && pos >= 0) {
                    cursum += b[pos].first;
                    anscnt ++;
                    fg += b[pos].second;
                    pos --;
                }

                anscnt += (anscnt + 1);
                anscnt -= fg;
                if (fg == 2 || fg == 0) anscnt --;
                printf("Case #%d: %d\n",CC ++,anscnt);
            }
            else {
                cin >> a[0].first >> a[0].second;
                cin >> a[0].first >> a[0].second;
                printf("Case #%d: %d\n",CC ++,2);
            }
        }
		//printf("Case #%d: %.7f\n",CC ++,maxs);
	}
}






