#include<stdio.h>
#include<algorithm>
#define Max(a,b) (a > b ? a : b)
using namespace std;
struct time {
	int ro, lo;
	int index;
	bool operator<(time a) const{
		return a.lo > lo;
	}
};
time T[201],lo[101],ro[101];
int arr[201];
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t, test = 1;
	scanf("%d", &t);
	while (test <= t) {
		int n, m;
		scanf("%d %d", &n, &m);
		for (int i = 0; i < n; i++) {
			scanf("%d %d", &T[i].lo, &T[i].ro);
			lo[i].lo = T[i].lo;
			lo[i].ro = T[i].ro;
			T[i].index = lo[i].index = i;
		}
		sort(lo, lo + n);
		for (int i = 0; i < m; i++) {
			scanf("%d %d", &T[i+n].lo, &T[i+n].ro);
			ro[i].lo = T[i+n].lo;
			ro[i].ro = T[i+n].ro;
			T[i + n].index = ro[i].index = i + n;
		}
		sort(ro, ro + m);
		sort(T, T + n + m);
		int t = 0, ans = 0, cnt = 0;
		int a, b,tmp;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n + m; j++) {
				if (lo[i].index == T[j].index)
					a = j;
				if (lo[(i + 1) % n].index == T[j].index)
					b = j;
			}
			if ((i + 1) % n == i) {
				tmp = lo[i].lo - lo[i].ro;
			}
			else {
				tmp = lo[(i + 1) % n].lo - lo[i].ro;
	
			}
			if (tmp < 0)
				tmp += 1440;
			if (a==b ||(a + 1) % (n + m) == b) {
				arr[cnt++] = tmp;
			}
			else {
				ans++;
				t += tmp;
			}
		}
		sort(arr, arr + cnt);
		while (t < 720 && cnt !=0) {
			t += arr[--cnt];
			ans++;
		}
		t = 0, cnt = 0;
		int ansTmp = 0;
		for (int i = 0; i < m; i++) {
			for (int j = 0; j < n + m; j++) {
				if (ro[i].index == T[j].index)
					a = j;
				if (ro[(i + 1) % m].index == T[j].index)
					b = j;
			}
			if ((i + 1) % m == i)
				tmp = ro[i].lo - ro[i].ro;
			else
				tmp = ro[(i + 1) % m].lo - ro[i].ro;
			if (tmp < 0)
				tmp += 1440;
			if (a == b ||(a + 1) % (n + m) == b) {
				arr[cnt++] = tmp;
			}
			else {
				ansTmp++;
				t += tmp;
			}
		}
		sort(arr, arr + cnt);
		while (t < 720 && cnt !=0) {
			t += arr[--cnt];
			ansTmp++;
		}
		ans = Max(ans, ansTmp);
		printf("Case #%d: %d\n", test++, ans * 2);
	}
}