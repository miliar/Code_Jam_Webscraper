#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <map>
#include <utility>

using namespace std;
typedef pair<int,int> ii;

int dx[] = {1, 0, -1, 0};
int dy[] = {0, -1, 0, 1};
char A[26][26];
int R, C;

int rowfill(int i,int j1, int j2, char c)
{
	int j;
	if (i<0 || i>=R)
		return 0;
	for (j=j1; j<=j2; ++j) {
		if (A[i][j] != '?')
			break;
	}
	if (j > j2) {
		for (j=j1; j<=j2; ++j)
			A[i][j] = c;
		return 1;
	}
	return 0;
}

int colfill(int j,int i1, int i2, char c)
{
	int i;
	if (j<0 || j>=C)
		return 0;
	for (i=i1; i<=i2; ++i) {
		if (A[i][j] != '?')
			break;
	}
	if (i > i2) {
		for (i=i1; i<=i2; ++i)
			A[i][j] = c;
		return 1;
	}
	return 0;
}

int main()
{
	int T,t;
	map<char,pair<ii,ii> >M;
	scanf("%d",&T);
	for (t=1; t<=T; ++t) {
		M.clear();
		scanf("%d %d ", &R, &C);
		memset(A, 0, sizeof A);
		for (int i=0;i<R;++i) {
			for (int j=0;j<C;++j) {
				char c = getchar();
				A[i][j] = c;
				if (c != '?') {
					if (M.find(c) == M.end()) {
						M[c] = pair<ii,ii>(ii(i,j),ii(i,j));
					} else {
						if (i < M[c].first.first)
							M[c].first.first = i;
						if (j < M[c].first.second)
							M[c].first.second = j;
						if (i > M[c].second.first)
							M[c].second.first = i;
						if (j > M[c].second.second)
							M[c].second.second = j;
					}
				}
			}
			getchar();
		}
		for (map<char,pair<ii,ii> >::iterator it=M.begin(); it!=M.end(); ++it) {
			for (int i=it->second.first.first; i<=it->second.second.first; ++i)
				for (int j=it->second.first.second; j<=it->second.second.second; ++j) {
					//if (A[i][j] != '?')
						//printf("Found non? at %d %d\n", i, j);
					A[i][j] = it->first;
				}
		}
		for (map<char,pair<ii,ii> >::iterator it=M.begin(); it!=M.end(); ++it) {
			while (colfill(it->second.first.second-1,
						it->second.first.first,
						it->second.second.first,
						it->first))
				it->second.first.second--;
			while (colfill(it->second.second.second+1,
						it->second.first.first,
						it->second.second.first,
						it->first))
				it->second.second.second++;
			while (rowfill(it->second.first.first-1,
						it->second.first.second,
						it->second.second.second,
						it->first))
				it->second.first.first--;
			while (rowfill(it->second.second.first+1,
						it->second.first.second,
						it->second.second.second,
						it->first))
				it->second.second.first++;
		}
		printf("Case #%d:\n",t);
		for (int i=0; i<R; ++i) {
			for (int j=0; j<C; ++j)
				putchar(A[i][j]);
			putchar(10);
		}
	}
	return 0;
}
