#include <cstdio>
#include <vector>
#include <list>

using namespace std;

int main() {
	int t, casenum;
	int r, c, i, j;
	char ch;
	char** result;

	vector< list< pair<int, char> > > vec;
	bool waiting;
	scanf("%d", &t);
	for(casenum = 1; casenum <= t; casenum++) {
		vec.clear();
		scanf("%d%d", &r, &c);
		vec.resize(r);
		ch = '\0';
		for(i = 0; i < r; i++) {
			while((ch < 'A' || ch > 'Z') && ch != '?') ch = getchar();
			j = 0;
			while((ch >= 'A' && ch <= 'Z') || ch == '?') {
				if(ch != '?') {
					vec[i].push_back(pair<int, char>(j, ch));
				}
				j++;
				ch = getchar();
			}
		}

		waiting = false;
		result = new char*[r];
		for(i = 0; i < r; i++) {
			result[i] = new char[c + 1];
			result[i][c] = '\0';
			if(vec[i].size() == 0) {
				if(i > 0) {
					if(!waiting) {
						for(j = 0; j < c; j++) {
							result[i][j] = result[i - 1][j];
						}
					}
				} else {
					waiting = true;
				}
			} else {
				j = 0;
				for(auto iter = vec[i].begin(); iter != vec[i].end(); ++iter) {
					for(; j <= iter->first; j++) {
						result[i][j] = iter->second;
					}
				}
				ch = vec[i].back().second;
				for(; j < c; j++) {
					result[i][j] = ch;
				}

				if(waiting) {
					for(int n = 0; n < i; n++) {
						for(j = 0; j < c; j++) {
							result[n][j] = result[i][j];
						}
					}
					waiting = false;
				}
			}
		}

		printf("Case #%d:\n", casenum);
		for(i = 0; i < r; i++) {
			puts(result[i]);
		}
	}
}