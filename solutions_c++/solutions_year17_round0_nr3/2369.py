#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>

using namespace std;

typedef struct node
{
	long long n, times;
} node;

int t;

node map[100000000];
node map2[100000000];

void cal(long long n, long long *min_c, long long *max_c) {
	if ((n & 1) == 1) {
		*min_c = (n - 1) >> 1;
		*max_c = (n - 1) >> 1;
	} else {
		*min_c = (n >> 1) - 1;
		*max_c = (n >> 1);
	}
}

int compare_ints(const void* a, const void* b)
{
    node arg1 = *(const node*)a;
    node arg2 = *(const node*)b;

    if (arg1.n < arg2.n) return 1;
    if (arg1.n > arg2.n) return -1;
    return 0;
}

void proc(int tid) {
	long long n;
	long long k;
	long long len, len2;
	long long num;
	scanf("%lld %lld", &n, &k);

	node *queue = map;
	node *queue2 = map2;

	len = 1;
	queue[0].n = n; queue[0].times = 1;

	while (1) {
		num = -1;
		for (long long i = 0; i < len; i++) {
			if (queue[i].times >= k) {
				num = queue[i].n;
				break;
			} else {
				long long min_c, max_c;
				cal(queue[i].n, &min_c, &max_c);
				queue2[i << 1].n = max_c;
				queue2[i << 1].times = queue[i].times;
				queue2[(i << 1) + 1].n = min_c;
				queue2[(i << 1) + 1].times = queue[i].times;
				k -= queue[i].times;
				// printf("divide %lld x %lld, k %lld\n", queue[i].n, queue[i].times, k);
			}
		}
		if (num != -1) break;
		qsort(queue2, 2 * len, sizeof(node), compare_ints);
		long long pre = 0;
		len2 = 1;
		for (long long i = 1; i < 2 * len; i++) {
			if (queue2[i].n <= 0) break;
			if (queue2[i].n != queue2[pre].n) {
				pre++; len2++;
				queue2[pre].n = queue2[i].n;
				queue2[pre].times = queue2[i].times;
			} else {
				queue2[pre].n = queue2[i].n;
				queue2[pre].times += queue2[i].times;
			}
		}
		len = len2;
		node *t = queue;
		queue = queue2;
		queue2 = t;
		// printf("====\n");
	}

	long long min_c, max_c;
	cal(num, &min_c, &max_c);

	printf("Case #%d: %lld %lld\n", tid, max_c, min_c);
}

int main() {
	scanf("%d\n", &t);

	for (int i = 0; i < t; i++)
		proc(i + 1);

	return 0;
}
