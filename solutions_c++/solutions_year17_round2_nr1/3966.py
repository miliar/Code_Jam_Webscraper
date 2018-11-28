#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>

using namespace std;

typedef struct node {
	long long k, s;
};

long long d, n;
struct node map[1000];
double tt[1000];
int t;

int compare_ints(const void* a, const void* b)
{
    long long arg1 = (*(const struct node*)a).k;
    long long arg2 = (*(const struct node*)b).k;

    long long arg12 = (*(const struct node*)a).k;
    long long arg22 = (*(const struct node*)b).k;

    if (arg1 < arg2) return -1;
    if (arg1 > arg2) return 1;

    if (arg1 = arg2) {
	    if (arg12 < arg22) return -1;
	    if (arg12 > arg22) return 1;
    }
    return 0;

    // return (arg1 > arg2) - (arg1 < arg2); // possible shortcut
    // return arg1 - arg2; // erroneous shortcut (fails if INT_MIN is present)
}

void proc(int id) {
	scanf("%lld %lld", &d, &n);

	for (long long i = 0; i < n; i++) {
		scanf("%lld %lld", &map[i].k, &map[i].s);
	}

    qsort(map, n, sizeof(struct node), compare_ints);

	for (long long i = n - 1; i >= 0; i--) {
		tt[i] = ((double)d - map[i].k) / map[i].s;
		if (i < n - 1) {
			if (tt[i + 1] <= tt[i])
				continue;
			else {
				double t1 = ((double)map[i+1].k - map[i].k) / (map[i].s - map[i+1].s);
				double s = t1 * map[i].s;
				double t2 = (d - map[i].k - s) / map[i+1].s;
				tt[i] = t1 + t2;
				map[i].s = map[i + 1].s;
			}
		} else {
			//pass
		}
	}

	printf("Case #%d: %llf\n", id, d / tt[0]);
}

int main() {
	scanf("%d\n", &t);

	for (int i = 0; i < t; i++)
		proc(i + 1);

	return 0;
}
