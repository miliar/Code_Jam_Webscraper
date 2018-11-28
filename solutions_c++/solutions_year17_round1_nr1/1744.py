#include <bits/stdc++.h>
#include <string.h>
#include <cmath>
#define mp make_pair
#define pb push_back
#define f first
#define s second
#define lb lower_bound
#define ub upper_bound

using namespace std;

typedef long long int ll;
typedef unsigned long long int ull;
typedef vector<int> vi;
typedef vector<pair<int,int> > vii;
typedef pair<int,int> pii;

const int N = 50;
const int INF = 0x3f3f3f3f;
const long long int INFL = 0x3f3f3f3f3f3f3f3f;
const double pi = atan(1.0)*4.0;

char matrix[N][N];
int r, c;
int mrc[N];

void cpyl(int a, int b);
void srcl(int a);

int main(void) {
	int t;
	
	
	scanf("%d", &t);
	
	for(int test = 1; test <= t; test++) {
		memset(mrc, 0, sizeof(int)*N);
		scanf("%d %d", &r, &c);
		for(int i = 0; i < r; i++) {
			getchar();
			for(int j = 0; j < c; j++) {
				matrix[i][j] = getchar();
			}
		}
		srcl(0);
		printf("Case #%d:\n", test);
		for(int i = 0; i < r; i++) {
			for(int j = 0; j < c; j++) {
				putchar(matrix[i][j]);
			}
			puts("");
		}
	}


	return 0;
}

void cpyl(int m, int k) {
	if(mrc[k] == 0) srcl(k);
	for(int i = 0; i < r; i++) matrix[i][m] = matrix[i][k];
	mrc[m] = 1;
	for(int i = m + 1; i < c; i++) {
		if(mrc[i] == 0) {
			srcl(i);
			return;
		}
	}
}

void srcl(int m) {
	int idx = 0;
	while(idx < r && matrix[idx][m] == '?') idx++;
	if(idx == r) {
		if(m == 0 || mrc[m-1] == 0) cpyl(m, m + 1);
		else {
			cpyl(m, m - 1);
			if(m + 1 < c) srcl(m+1);
		}
		return;			
	}
	for(int i = 0; i < idx; i++) matrix[i][m] = matrix[idx][m];
	while(idx + 1 < r) {
		if(matrix[idx+1][m] == '?') matrix[idx+1][m] = matrix[idx][m];
		idx++;
	}
	mrc[m] = 1;
	if(m + 1 < c) srcl(m+1);
}
