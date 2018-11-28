#include <set>
#include <map>
#include <cmath>
#include <ctime>
#include <queue>
#include <string>
#include <cstdio>
#include <vector>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <algorithm>
using namespace std;
int Test, n, a[100];
long long N, B;

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	scanf("%d", &Test);
	for (int Case = 1; Case <= Test; Case ++) {
        scanf("%lld", &N);
        n = 0;
        memset(a, -1, sizeof(a));
        while (N > 0) {
            a[n++] = N % 10;
            N /= 10;
        }
        for (int i = n-1; i >= 1; i --) {
            if (a[i]>a[i-1]) {
                for (; a[i+1] == a[i]; i ++);
                a[i] --;
                for (int j = i-1; j >= 0; j --) {
                    a[j] = 9;
                }
                break;
            }
        }
        for (int i = n-1; i >= 0; i --) {
            N = N * 10 + a[i];
        }
		printf("Case #%d: %lld\n", Case, N);
	}
	return 0;
}
