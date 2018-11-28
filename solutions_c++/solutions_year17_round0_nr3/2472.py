#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
#include<queue>
#include<map>

using namespace std;

FILE *out = fopen("output.txt", "w");
FILE *in = fopen("input.txt", "r");

int main() {
	

	int tc;
	fscanf(in, "%d", &tc);

	for(int tt=1;tt<=tc;tt++){

		long long ans;

		long long n, k;
		fscanf(in, "%lld %lld", &n, &k);

		map<long long, long long> count;
		priority_queue<long long> q;

		q.push(n);
		count[n] = 1;
		while (k > 0) {
			long long topcount = q.top();
			q.pop();
			if (topcount % 2 == 1) {
				if (count.find((topcount - 1) / 2) == count.end()) {
					q.push((topcount - 1) / 2);
				}
				k -= count[topcount];
				if (k <= 0) {
					ans = topcount;
					break;
				}
				count[(topcount - 1) / 2] += count[topcount] * 2;
				count[topcount] = 0;
			}
			else {
				if (count.find((topcount - 1) / 2) == count.end()) {
					q.push((topcount - 1) / 2);
				}

				if (count.find((topcount) / 2) == count.end()) {
					q.push((topcount) / 2);
				}
				k -= count[topcount];
				if (k <= 0) {
					ans = topcount;
					break;
				}
				count[(topcount - 1) / 2] += count[topcount];
				count[(topcount) / 2] += count[topcount];
				count[topcount] = 0;
			}
		}
		if (ans % 2 == 0)fprintf(out, "Case #%d: %lld %lld\n", tt, ans / 2, (ans / 2) - 1);
		else fprintf(out, "Case #%d: %lld %lld\n", tt, ans / 2, ans / 2);
		

		

	}
	return 0;
}