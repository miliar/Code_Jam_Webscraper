#define _CRT_SECURE_NO_WARNINGS
#define MIN(a,b) ((a>b)?b:a)
#define MAX(a,b) ((a>b)?b:a)
#define FOR(i,size) for(i ; i < size ; ++i)
#define FOR_IN(i,size) for(i ; i <= size ; ++i)
#define FOR_REV(i) for(i ; i >=0 ; --i)
#define FOR_REV_SIZE(i,size) for(i ; i >=size ; --i)


#include <iostream>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>

using namespace std;

typedef const int C_INT;
typedef unsigned int UINT;
typedef const unsigned int C_UINT;
typedef unsigned char UCHAR;
typedef const unsigned char C_UCHAR;
typedef const char C_CHAR;
typedef const unsigned long long C_ULL;
typedef unsigned long long ULL;

typedef std::pair<int, int> PINT;
typedef std::vector<std::vector<int>> V2INT;
typedef std::vector<int> VINT;
typedef std::vector<string> VSTR;

using namespace std;

UINT memo[100][100];


int main() {

	freopen("C:\\Users\\goodd\\Downloads\\C-small-1-attempt0.in", "r", stdin);
	freopen("C:\\Users\\goodd\\Desktop\\C-small.out", "w", stdout);

	int size = 0;
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.precision(10);

	int caseSize = 0;
	scanf("%d", &caseSize);

	for (int t = 0; t < caseSize; ++t) {

		int stalls, mans;
		scanf("%d %d", &stalls, &mans);

		PINT solve;
		if (stalls != mans) {
			std::priority_queue<int> q;
			q.push(stalls);
			int i = 0;
			FOR(i, mans-1) {
				int maxi = q.top();
				q.pop();
				int l, r;
				if (maxi % 2 == 0) {
					r = maxi / 2;
					l = maxi / 2 - 1;
				}
				else {
					l = r = maxi / 2;
				}

				q.push(l);
				q.push(r);
			}
			int f = q.top();
			int max, min;
			if (f % 2 == 0) {
				max = f / 2;
				min = f / 2 - 1;
			}
			else {
				min = max = f / 2;
			}
			solve = PINT(max, min);
		}
		else
			solve = PINT(0, 0);

		printf("Case #%d: %d %d\n", (t + 1), solve.first, solve.second);
				
	}

	return 0;
}
