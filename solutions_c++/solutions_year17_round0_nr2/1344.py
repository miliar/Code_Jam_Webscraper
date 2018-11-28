#include"stdio.h"
#include"algorithm"
using namespace std;
int T, N, Mark;
unsigned long long Ans;
char S[100];
int main() {
	//freopen("B-small-attempt0.in", "r", stdin);
	//freopen("B-small-attempt0.txt", "w", stdout);
	freopen("B-large.in", "r", stdin);
	freopen("B-large.txt", "w", stdout);
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		scanf("%s", S);
		for (N = 0; S[N]; N++);
		Mark = N;
		for (int i = N - 1; i > 0; i--)
			if (S[i] < S[i-1]) {
				S[i-1]--;
				Mark = i;
			}
		Ans = 0;
		for (int i = 0; i < Mark; i++)
			Ans = Ans * 10 + (S[i] - '0');
		for (int i = Mark; i < N; i++)
			Ans = Ans * 10 + 9;
		printf("Case #%d: %llu\n", t, Ans);
	}
}
