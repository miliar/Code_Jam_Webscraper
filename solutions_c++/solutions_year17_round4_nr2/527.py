#include<bits/stdc++.h>
using namespace std;
#define ALL(v) (v).begin(),(v).end()
int ceildiv(int p, int q) { return (p + q - 1) / q; }
int main() {
	int T; cin >> T;
	for(int tc=1;tc<=T;tc++) {
		int nplaces, npeople, ntickets;
		cin >> nplaces >> npeople >> ntickets;
		static int A[1005][1005]; // row: position, column: client
		memset(A,0,sizeof A);
		for (int it=0; it<ntickets; it++) {
			int i, j; cin >> i >> j;
			i--, j--;
			A[i][j]++;
		}
		int answer = 0;
		for (int j=0; j<npeople; j++) {
			int s=0;
			for(int i=0;i<nplaces;i++)s+=A[i][j];
			answer=max(answer,s);
		}
		for (int i=0, cumsu=0; i<nplaces; i++) {
			for(int j=0;j<npeople;j++)cumsu+=A[i][j];
			answer=max(answer,ceildiv(cumsu, i + 1));
		}
		int promotions=0;
		for (int i=0; i<nplaces; i++) {
			int s=0;
			for (int j=0; j<npeople; j++)s+=A[i][j];
			promotions += max(0, s - answer);
		}
		printf("Case #%d: %d %d\n", tc, answer, promotions);
	}
}
