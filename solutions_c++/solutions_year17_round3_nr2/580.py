#include<iostream>
#include<cstdio>
#include<string>
#include<cmath>
#include<bitset>
#include<vector>
#include<map>
#include<set>
#include<algorithm>
#include<utility>
using namespace std;

#define FOR(I,A,B) for(int I=(A);I<=(B);I++)
#define REP(I,N) for(int I=0;I<(N);I++)
#define ALL(X) (X).begin(),(X).end()
#define PB push_back
#define MP make_pair
#define f first
#define s second

typedef vector<int> VI;
typedef pair<int,int> PII;
typedef long long ll;
typedef vector<string> VS;

int memo[24 * 60 + 5][24 * 60 + 5][3];

void testcase() {
	int AC, AJ;
	cin >> AC >> AJ;

	int who[24 * 60 + 1];

	REP(i, 24 * 60 + 1) who[i] = 0;
	REP(i, AC) {
		int c, d;
		cin >> c >> d;
		FOR(j, c + 1, d) who[j] = 1;	
	}

	REP(i, AJ) {
		int c, d;
		cin >> c >> d;
		FOR(j, c + 1, d) who[j] = 2;
	}

	REP(i, 24 * 60 + 3) REP(j, 24 * 60 + 3) memo[i][j][1] = memo[i][j][2] = 1000000;
	memo[0][0][1] = 0;

	FOR(i, 1, 24 * 60) {
		FOR(j, 1, i) {
			if(who[i] != 1)
				memo[j][i][1] = min(memo[j - 1][i - 1][1], memo[i - j][i - 1][2] + 1);
			if(who[i] != 2)
				memo[j][i][2] = min(memo[j - 1][i - 1][2], memo[i - j][i - 1][1] + 1);
		}
	}

	int r = min(memo[12 * 60][24 * 60][1], memo[12 * 60][24 * 60][2] + 1);

	REP(i, 24 * 60 + 3) REP(j, 24 * 60 + 3) memo[i][j][1] = memo[i][j][2] = 1000000;
	memo[0][0][2] = 0;

	FOR(i, 1, 24 * 60) {
		FOR(j, 1, i) {
			if(who[i] != 1)
				memo[j][i][1] = min(memo[j - 1][i - 1][1], memo[i - j][i - 1][2] + 1);
			if(who[i] != 2)
				memo[j][i][2] = min(memo[j - 1][i - 1][2], memo[i - j][i - 1][1] + 1);
		}
	}

	int r2 = min(memo[12 * 60][24 * 60][2], memo[12 * 60][24 * 60][1] + 1);

	cout << min(r, r2) << '\n';
}

int main() {
	int t;
	cin >> t;
	
	FOR(i, 1, t) {
		cout << "Case #" << i << ": ";
		testcase();
	}

	return 0;
}

