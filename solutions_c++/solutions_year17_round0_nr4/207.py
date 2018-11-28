#include <iostream>
#include <vector>

using namespace std;

struct Bipartite {
	int L, R;
	vector<vector<int> > graph;
	vector<bool> visited;
	vector<int> match;
	
	Bipartite(int l, int r) {
		L = l; R = r;
		graph.resize(L);
		visited.resize(L);
		for (int i = 0; i < R; ++i) match.push_back(-1);
	}
	
	void insert(int l, int r) {
		graph[l].push_back(r);
	}
	
	int augment(int l) {
		if (visited[l]) return 0;
		visited[l] = true;
		for (int _r = 0; _r < graph[l].size(); ++_r) {
			int r = graph[l][_r];
			if (match[r] == -1 || augment(match[r])) {
				match[r] = l;
				return 1;
			}
		}
		return 0;
	}
	
	vector<pair<int, int> > matching() {
		for (int i = 0; i < L; ++i) {
			for (int j = 0; j < L; ++j) visited[j] = false;
			augment(i);
		}
		vector<pair<int, int> > M;
		for (int i = 0; i < R; ++i) {
			if (match[i] >= 0) M.push_back(make_pair(match[i], i));
		}
		return M;
	}
};

char addP(char c) {
	if (c == '.') return '+';
	if (c == 'x') return 'o';
	return 0;
}

char addX(char c) {
	if (c == '.') return 'x';
	if (c == '+') return 'o';
	return 0;
}

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		int N, M;
		cin >> N >> M;
		int sN = 2*N-1;
		char stage[N][N];
		char newStage[N][N];
		int value = 0;
		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < N; ++j) {
				stage[i][j] = '.';
				newStage[i][j] = '.';
			}
		}
		
		vector<pair<int, int> > notP, notX;
		
		for (int i = 0; i < M; ++i) {
			char c; int x, y;
			cin >> c >> y >> x;
			stage[y-1][x-1] = c;
			newStage[y-1][x-1] = c;
			value += c == 'o' ? 2 : 1;
			if (c != '+') notP.push_back(make_pair(x-1, y-1));
			if (c != 'x') notX.push_back(make_pair(x-1, y-1));
		}
		
		//cout << "OK" << endl;
		
		bool okP[sN][sN];
		for (int y = 0; y < sN; ++y)
			for (int x = 0; x < sN; ++x)
				okP[y][x] = false;
		for (int y = 0; y < N; ++y)
			for (int x = 0; x < N; ++x)
				okP[y-x+N-1][x+y] = true;
		/*
		for (int yy = 0; yy < sN; ++yy) {
			for (int xx = 0; xx < sN; ++xx) {
				cout << okP[yy][xx];
			}
			cout << endl;
		}*/
		
		//cout << "OK" << endl;
		bool okX[N][N];
		for (int y = 0; y < N; ++y)
			for (int x = 0; x < N; ++x)
				okX[y][x] = true;
			
		//cout << "OK" << endl;
		for (int _p = 0; _p < notP.size(); ++_p) { 
			pair<int, int> p = notP[_p];
			int X = p.first, Y = p.second;
			for (int x = 0; x < N; ++x) {
				okX[Y][x] = false;
			}
			for (int y = 0; y < N; ++y) {
				okX[y][X] = false;
			}
		}
		
		//cout << "OK" << endl;
		for (int _p = 0; _p < notX.size(); ++_p) { 
			pair<int, int> p = notX[_p];
			int xx = p.first, yy = p.second;
			int X = yy + xx;
			int Y = yy-xx+N-1;
			for (int x = 0; x < sN; ++x) {
				okP[Y][x] = false;
			}
			for (int y = 0; y < sN; ++y) {
				okP[y][X] = false;
			}
		}
		/*
		for (int yy = 0; yy < sN; ++yy) {
			for (int xx = 0; xx < sN; ++xx) {
				cout << okP[yy][xx];
			}
			cout << endl;
		}*/
		
		//cout << "OK" << endl;
		Bipartite bP(sN, sN);
		//cout << "OK" << endl;
		for (int y = 0; y < sN; ++y)
			for (int x = 0; x < sN; ++x)
				if (okP[y][x]) bP.insert(x, y);
			
		//cout << "OK" << endl;
		vector<pair<int, int> > matchP = bP.matching();
		
		//cout << "OK" << endl;
		for (int _p = 0; _p < matchP.size(); ++_p) {
			pair<int, int> p = matchP[_p];
			int y = (p.first + p.second - (N-1))/2;
			int x = (p.first - p.second + (N-1))/2;
			newStage[y][x] = addP(newStage[y][x]); 
		}
		
		Bipartite bX(N, N);
		for (int y = 0; y < N; ++y)
			for (int x = 0; x < N; ++x)
				if (okX[y][x]) bX.insert(x, y);
		vector<pair<int, int> > matchX = bX.matching();
		
		for (int _p = 0; _p < matchX.size(); ++_p) {
			pair<int, int> p = matchX[_p];
			int y = p.second;
			int x = p.first;
			newStage[y][x] = addX(newStage[y][x]); 
		}
		
		int changes = 0;
		
		for (int y = 0; y < N; ++y)
			for (int x = 0; x < N; ++x)
				if (newStage[y][x] != stage[y][x]) ++changes;
			
		cout << "Case #" << t << ": " << matchP.size() + matchX.size() + value << " " << changes << endl;
		
		for (int y = 0; y < N; ++y)
			for (int x = 0; x < N; ++x)
				if (newStage[y][x] != stage[y][x]) {
					cout << newStage[y][x] << " " << y + 1 << " " << x + 1 << endl;
				}
		
		
	}	
}