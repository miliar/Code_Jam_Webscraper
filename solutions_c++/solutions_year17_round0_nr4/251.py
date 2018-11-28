#include <bits/stdc++.h>

using namespace std;

void doCase(int t) {
	int N, M;
	cin >> N >> M;
	
	vector<vector<char>> sgrid(N, vector<char>(N,'.'));
	vector<vector<bool>> rook(N,vector<bool>(N, false)), bishop(N,vector<bool>(N,false));
	
	vector<bool> rowused(N, false), colused(N,false);
	vector<bool> sdiagused(2*N-1, false), ddiagused(2*N-1,false);
	
	for (int i=0; i<M; i++) {
		char c; int x,y;
		cin >> c >> x >> y;
		x--; y--;
		sgrid[x][y] = c;
		if (c == 'x' || c == 'o') {
			rook[x][y] = true;
			rowused[x] = true;
			colused[y] = true;
		}
		if (c == '+' || c == 'o') {
			bishop[x][y] = true;
			sdiagused[x+y] = true;
			ddiagused[N-1+x-y] = true;
		}
	}
	
	// Solve the rook problem
	int j = 0;
	for (int i=0; i<N; i++) {
		if (rowused[i]) continue;
		while (colused[j]) j++;
		rook[i][j] = true;
		j++;
	}
	
	// Solve the bisshop problem
	priority_queue<pair<int, int>> work;
	vector<int> sdiagfree(2*N-1), ddiagfree(2*N-1);
	for (int s = 0; s < 2*N-1; s++) {
		if (sdiagused[s])
			continue;
		for (int x = 0; x<N; x++) {
			int y = s-x;
			if (y < 0 || y >= N)
				continue;
			if (!ddiagused[N-1+x-y])
				sdiagfree[s]++;
		}
		if (sdiagfree[s] != 0)
			work.push({-sdiagfree[s], s});
	}
	for (int d = 0; d < 2*N-1; d++) {
		if (ddiagused[d])
			continue;
		for (int x = 0; x<N; x++) {
			int y = N-1+x-d;
			if (y < 0 || y >= N)
				continue;
			if (!sdiagused[x+y])
				ddiagfree[d]++;
		}
		if (ddiagfree[d] != 0)
			work.push({-ddiagfree[d], 4*N+d});
	}
	
	while (!work.empty()) {
		auto cur = work.top(); work.pop();
		int i = cur.second;
		if (i < 4*N) {
			if (sdiagfree[i] != -cur.first || sdiagused[i])
				continue;
			
			int x;
			int y;
			for (x = 0; x<N; x++) {
				y = i-x;
				if (y < 0 || y >= N) continue;
				if (!ddiagused[N-1+x-y]) break;
			}
			
			bishop[x][y] = true;
			sdiagused[x+y] = true;
			ddiagused[N-1+x-y] = true;
			
			for (int i=-N+1; i<N; i++) {
				if (x+i >= 0 && x+i < N && y+i >= 0 && y+i < N && !sdiagused[x+y+2*i]) {
					sdiagfree[x+y+2*i]--;
					if (sdiagfree[x+y+2*i] != 0)
						work.push({-sdiagfree[x+y+2*i], x+y+2*i});
				}
				if (x+i >= 0 && x+i < N && y-i >= 0 && y-i < N && !ddiagused[N-1+x-y+2*i]) {
					ddiagfree[N-1+x-y+2*i]--;
					if (ddiagfree[N-1+x-y+2*i] != 0)
						work.push({-ddiagfree[N-1+x-y+2*i], N-1+x-y+2*i});
				}
			}
		} else {
			i -= 4*N;
			if (ddiagfree[i] != -cur.first || ddiagused[i])
				continue;
			
			int x;
			int y;
			for (x=0; x<N; x++) {
				y = N-1+x-i;
				if (y < 0 || y >= N)
					continue;
				if (!sdiagused[x+y]) break;
			}
			
			bishop[x][y] = true;
			sdiagused[x+y] = true;
			ddiagused[N-1+x-y] = true;
			
			for (int i=-N+1; i<N; i++) {
				if (x+i >= 0 && x+i < N && y+i >= 0 && y+i < N && !sdiagused[x+y+2*i]) {
					sdiagfree[x+y+2*i]--;
					if (sdiagfree[x+y+2*i] != 0)
						work.push({-sdiagfree[x+y+2*i], x+y+2*i});
				}
				if (x+i >= 0 && x+i < N && y-i >= 0 && y-i < N && !ddiagused[N-1+x-y+2*i]) {
					ddiagfree[N-1+x-y+2*i]--;
					if (ddiagfree[N-1+x-y+2*i] != 0)
						work.push({-ddiagfree[N-1+x-y+2*i], N-1+x-y+2*i});
				}
			}
		}
	}
	
	// Build target grid
	vector<vector<char>> tgrid(N,vector<char>(N,'.'));
	int count = 0, diffs = 0;
	for (int i=0; i<N; i++) {
		for (int j=0; j<N; j++) {
			if (rook[i][j] && bishop[i][j]) {
				count += 2;
				tgrid[i][j] = 'o';
			} else if (rook[i][j]) {
				count += 1;
				tgrid[i][j] = 'x';
			} else if (bishop[i][j]) {
				count += 1;
				tgrid[i][j] = '+';
			}
			if (tgrid[i][j] != sgrid[i][j])
				diffs++;
		}
	}
	
	// And output results
	cout << "Case #" << t << ": " << count << " " << diffs << endl;
	if (N != 1 && count != 3*N-2) cerr << "ERROR IN TC " << t << endl;
	for (int i=0; i<N; i++) {
		for (int j=0; j<N; j++) {
			if (sgrid[i][j] != tgrid[i][j]) {
				cout << tgrid[i][j] << " " << i+1 << " " << j+1 << endl;
			}
		}
	}
	
	/*cerr << endl;
	for (int i=0; i<N; i++) {
		for (int j=0; j<N; j++) {
			cerr << tgrid[i][j];
		}
		cerr << endl;
	}
	cerr << endl;
	
	for (int i=0; i<N; i++) {
		for (int j=0; j<N; j++) {
			cerr << bishop[i][j];
		}
		cerr << endl;
	}
	cerr << endl;*/
}

int main() {
	int T;
	cin >> T;
	for (int i=0; i<T; i++)
		doCase(i+1);
	return 0;
}
