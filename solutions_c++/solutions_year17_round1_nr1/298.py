#include <stdio.h>
#include <algorithm>

using namespace std;

const int MAX_N = 3e1 + 10;

int N, M; char Mp[MAX_N][MAX_N];

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int TC; scanf("%d", &TC);
	for(int tc=1; tc<=TC; tc++) {
		scanf("%d%d", &N, &M);
		for(int i=0; i<N; i++) scanf("%s", Mp[i]);
		for(int i=0; i<N; i++) {
			for(int j=1; j<M; j++)
				if(Mp[i][j] == '?' && Mp[i][j-1] != '?')
					Mp[i][j] = Mp[i][j-1];
			for(int j=M-2; j>=0; j--)
				if(Mp[i][j] == '?' && Mp[i][j+1] != '?')
					Mp[i][j] = Mp[i][j+1];
		}
		for(int i=0; i<M; i++) {
			for(int j=1; j<N; j++)
				if(Mp[j][i] == '?' && Mp[j-1][i] != '?')
					Mp[j][i] = Mp[j-1][i];
			for(int j=N-2; j>=0; j--)
				if(Mp[j][i] == '?' && Mp[j+1][i] != '?')
					Mp[j][i] = Mp[j+1][i];
		}
		printf("Case #%d:\n", tc);
		for(int i=0; i<N; i++) printf("%s\n", Mp[i]);
	}
	return 0;
}