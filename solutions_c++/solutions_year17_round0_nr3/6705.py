#include <iostream>
#include <queue>
using namespace std;
int main() {
	int T;
	scanf("%d", &T);
	for (int tT = 1 ; tT <= T; tT++) {
		int n, k;
		scanf(" %d %d", &n, &k);
		k--;
		priority_queue<int> p;
		p.push(n);
		while (k--) {
			int tmp = p.top();
			p.pop();
			if (tmp % 2 == 1) {
				tmp /= 2;
				p.push(tmp);
				p.push(tmp);
			}
			else {
				tmp /= 2;
				p.push(tmp);
				p.push(tmp - 1);
			}
		}
		int tmp = p.top(), ans1, ans2;
		if (tmp % 2 == 1) {
			tmp /= 2;
			ans1 = ans2 = tmp;
		}
		else {
			tmp /= 2;
			ans2 = tmp - 1;
			ans1 = tmp;
		}
		printf("Case #%d: %d %d\n", tT, ans1, ans2);

	}
}