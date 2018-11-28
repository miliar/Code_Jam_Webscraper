#include <bits/stdc++.h>

#define FOR(i, start, end) for (int i = start; i < end; ++i)
#define RFOR(i, start, end) for (int i = end - 1; i >= start; --i)

using namespace std;

const int MAX_N = 1000;

typedef long long ll;

struct Horse {
	double K, S;
	bool operator < (const Horse& a) const {
		return K < a.K;
	}
};

int T;
int N;
Horse horses[MAX_N];
double D;

double time_to_end(const Horse& a) {
	return (D - a.K) / a.S;
}

bool intersects(const Horse& a, const Horse& b) {
	if (a.K < b.K) {
		return time_to_end(a) < time_to_end(b);
	}
	else {
		return time_to_end(a) > time_to_end(b);
	}
}

int main()
{
	// freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-large.in", "r", stdin);
	freopen("r1b_a.out", "w", stdout);
	scanf("%d", &T);
	FOR(t, 1, T + 1) {
		printf("Case #%d: ", t);
		
		scanf("%lf %d", &D, &N);
		FOR(i, 0, N) {
			scanf("%lf %lf", &horses[i].K, &horses[i].S);
		}
		
		sort(horses, horses + N);
		
		int i = 0, j = 1;
		while (j < N) {
			if (intersects(horses[i], horses[j])) {
				i = j;
				j++;
			}
			else {
				j++;
			}
		}
		
		printf("%lf", D / time_to_end(horses[i]));
		
		printf("\n");
	}
	return 0;
}
