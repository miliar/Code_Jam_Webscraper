#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <vector>
using namespace std;

int tn;
char A[100][100];
int R, C;

vector<pair<char, int> > chs;

int main() {

	scanf("%d\n", &tn);
	for(int ctn = 0; ctn < tn; ctn ++) {

		scanf("%d %d\n", &R, &C);
		memset(A, 0, sizeof(A));
		for(int i = 0; i < R; i++) {
			for(int j = 0; j < C; j++)
				scanf("%c", &(A[i][j]));
			scanf("\n");
		}

		char ch = '\0';
		bool flag = false;
		for(int i = 0; i < R; i++) {
			chs.clear();
			for(int j = 0; j < C; j++)
				if (A[i][j] != '?') {
					chs.push_back(make_pair(A[i][j], j));
					flag = true;
				}
			if (flag) break;
		}

		for(int k = 0; k < chs.size(); k++) {
			int start = (k == 0)? 0 : chs[k-1].second+1;
			for(int j = start; j <= chs[k].second; j++)
				A[0][j] = chs[k].first;
			if (k == chs.size() - 1) {
				for(int j = chs[k].second+1; j < C; j++)
					A[0][j] = chs[k].first;
			}
		}

		int i = 1;
		while (i < R) {
			chs.clear();
			for(int j = 0; j < C; j++)
				if (A[i][j] != '?') {
					chs.push_back(make_pair(A[i][j], j));
				}
			if (!chs.size()) {
				// no character this line
				for(int j = 0; j < C; j++)
					A[i][j] = A[i-1][j];
			}
			else {
				for(int k = 0; k < chs.size(); k++) {
					int start = (k == 0)? 0 : chs[k-1].second+1;
					for(int j = start; j <= chs[k].second; j++)
						A[i][j] = chs[k].first;
					if (k == chs.size()-1) {
						for(int j = chs[k].second+1; j < C; j++)
							A[i][j] = chs[k].first;
					}
				}
			}
			i ++;
		}

		printf("Case #%d:\n", ctn+1);
		for(int i = 0; i < R; i++) {
			for(int j = 0; j < C; j++)
				printf("%c", A[i][j]);
			printf("\n");
		}

	}

	return 0;

}