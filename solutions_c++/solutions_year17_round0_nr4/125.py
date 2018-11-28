#include <cassert>
#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

const int MAX = 110;

class BipartiteMatcher {
public:
	const int size;
	int *matched;
	bool *visited;

	vector < int > *edge;

	BipartiteMatcher(int size) : size(size) {
		matched = new int[2*size];
		visited = new bool[2*size];
		edge = new vector < int >[2*size];

		for (int i = 0; i < 2*size; i++) {
			matched[i] = -1;
		}
	}

	~BipartiteMatcher() {
		delete[] matched;
		delete[] visited;
		delete[] edge;
	}

	void addConnection(int a, int b) {
		assert(0 <= a && a < size && 0 <= b && b < size);
		b += size;
		edge[a].push_back(b);
		edge[b].push_back(a);
	}

	vector < pair < int, int > > match() {
		for (int left = 0; left < size; left++) {
			memset(visited, 0, sizeof(bool)*(2*size));
			tryMatch(left);
		}

		vector < pair < int, int > > ret;
		for (int left = 0; left < size; left++) {
			if (matched[left] != -1) {
				ret.push_back(make_pair(left, matched[left]-size));
			}
		}

		return ret;
	}

private: 
	bool tryMatch(int left) {
		for (auto right : edge[left]) {
			if (!visited[right]) {
				visited[right] = 1;
				if (matched[right] < 0 || tryMatch(matched[right])) {
					matched[right] = left;
					matched[left] = right;
					return 1;
				}
			}
		}
		return 0;
	}
};

int gridSize, numModel;
char original[MAX][MAX], ans[MAX][MAX];

void input() {
	scanf("%d%d", &gridSize, &numModel);

	for (int r = 1; r <= gridSize; r++) {
		for (int c = 1; c <= gridSize; c++) {
			original[r][c] = '.';
		}
		original[r][gridSize+1] = 0;
		ans[r][gridSize+1] = 0;
	}

	for (int i = 0; i < numModel; i++) {
		char t[2];
		int r, c;
		scanf("%s%d%d", t, &r, &c);
		original[r][c] = t[0];
	}

	for (int r = 1; r <= gridSize; r++) {
		for (int c = 1; c <= gridSize; c++) {
			ans[r][c] = original[r][c];
		}
	}
}

bool rowCheck[MAX], colCheck[MAX], ldiagCheck[MAX*2], rdiagCheck[MAX*2];

void solve() {
	memset(rowCheck, 0, sizeof(rowCheck));
	memset(colCheck, 0, sizeof(colCheck));
	memset(ldiagCheck, 0, sizeof(ldiagCheck));
	memset(rdiagCheck, 0, sizeof(rdiagCheck));

	for (int r = 1; r <= gridSize; r++) {
		for (int c = 1; c <= gridSize; c++) {
			int rowNum = r-1;
			int colNum = c-1;
			int ldiagNum = r+c-2;
			int rdiagNum = r-c+gridSize-1;
			if (ans[r][c] != '.') {
				if (ans[r][c] != '+') {
					rowCheck[rowNum] = 1;
					colCheck[colNum] = 1;
				}
				if (ans[r][c] != 'x') {
					ldiagCheck[ldiagNum] = 1;
					rdiagCheck[rdiagNum] = 1;
				}
			}
		}
	}

	BipartiteMatcher xy(gridSize), diag(gridSize*2-1);

	for (int r = 1; r <= gridSize; r++) {
		for (int c = 1; c <= gridSize; c++) {
			int rowNum = r-1;
			int colNum = c-1;
			int ldiagNum = r+c-2;
			int rdiagNum = r-c+gridSize-1;

			if (!rowCheck[rowNum] && !colCheck[colNum]) {
				xy.addConnection(rowNum, colNum);
			}
			if (!ldiagCheck[ldiagNum] && !rdiagCheck[rdiagNum]) {
				diag.addConnection(ldiagNum, rdiagNum);
			}
		}
	}

	for (auto p: xy.match()) {
		int rowNum = p.first;
		int colNum = p.second;

		int r = rowNum+1;
		int c = colNum+1;

		if (ans[r][c] == '.') ans[r][c] = 'x';
		else if (ans[r][c] == '+') ans[r][c] = 'o';
	}

	for (auto p: diag.match()) {
		int ldiagNum = p.first;
		int rdiagNum = p.second;

		int r = (ldiagNum+rdiagNum-gridSize+3)/2;
		int c = (ldiagNum-rdiagNum+gridSize+1)/2;
		
		if (ans[r][c] == '.') ans[r][c] = '+';
		else if (ans[r][c] == 'x') ans[r][c] = 'o';
	}

	int score = 0;
	int changed = 0;
	for (int r = 1; r <= gridSize; r++) {
		for (int c = 1; c <= gridSize; c++) {
			if (ans[r][c] != original[r][c]) {
				changed++;
			}
			score += ans[r][c] != '.';
			score += ans[r][c] == 'o';
		}
	}

	printf("%d %d\n", score, changed);

	for (int r = 1; r <= gridSize; r++) {
		for (int c = 1; c <= gridSize; c++) {
			if (ans[r][c] != original[r][c]) {
				printf("%c %d %d\n", ans[r][c], r, c);
			}
		}
	}
}

int main() {
	freopen("output.txt", "w", stdout);

	int numCase;
	scanf("%d", &numCase);
	for (int nowCase = 1; nowCase <= numCase; nowCase++) {
		input();

		printf("Case #%d: ", nowCase);
		solve();
	}

	return 0;
}