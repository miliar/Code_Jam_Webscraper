#include <iostream>
#include <algorithm>
#include <queue>
#include <cstdio>
#include <cstring>

#define pb push_back
typedef long long ll;
const int N = 100;

using namespace std;

#define pii pair<pair<int, int>, int> 
#define mp make_pair

int last_move = -1;
int dx[] = {1, -1, 0, 0};
int dy[] = {0, 0, 1, -1};
int id, cell_id, tmp_id;
int n, m, a[N][N];
int number_of_player;
bool vis[N][N];
pair<int, int> b[N];
string ans[] = {"DOWN", "UP", "RIGHT", "LEFT"};
int invalid[] = {1, 0, 3, 2};
bool flag = false;

bool check(int x, int y) {
	return (0 <= x && x < n && 0 <= y && y < m);
}

int distance(int xx1, int yy1, int xx2, int yy2) {
	return (abs(xx1 - xx2) + abs(yy1 - yy2));
}

int distance2(int xx1, int yy1) {
	int ret = 100000;
	for (int i = 1; i <= number_of_player; i++) {
		if (i == id) continue;
		if (b[i].first == -1) continue;
		ret = min(ret, distance(xx1, yy1, b[i].first, b[i].second));
	}
	return ret;
}

void process_inside() {
	flag = false;
	memset(vis, 0, sizeof(vis));
	queue<pair<int, int> > p;
	queue< pii > ret;
	p.push(mp(b[id].first, b[id].second));
	vis[b[id].first][b[id].second] = 1;
	while (!p.empty()) {
		pair<int, int> x = p.front();
		p.pop();
		for (int i = 0; i < 4; i++) {
			int newx = x.first + dx[i];
			int newy = x.second + dy[i];
			if (!check(newx, newy) || vis[newx][newy]) continue;
			if (a[newx][newy] != cell_id) {
				int _move = distance2(newx, newy);
				if (_move < 5) continue;
				ret.push(mp(mp(newx, newy), _move));
			}
			else {
				vis[newx][newy] = 1;
				p.push(mp(newx, newy));
			}
		}
	}
	int _max = -1, pos;
	pair<int, int> res;
	while (!ret.empty()) {
		pii x = ret.front();
		ret.pop();
		if (x.second > _max) {
			_max = x.second;
			res = x.first;
		}
	}
	if (_max > -1) {
		if (res.first != b[id].first) {
			if (res.first > b[id].first) { cout << "DOWN\n"; last_move = 0; }
			else { cout << "UP\n"; last_move = 1; }
		}
		else {
			if (res.second > b[id].second) { cout << "RIGHT\n"; last_move = 2; }
			else { cout << "LEFT\n"; last_move = 3; }
		}
		return;
	}
	_max = -1, pos;
	for (int i = 3; i >= 0; i--) {
		if (i == last_move) continue;
		int newx = b[id].first + dx[i];
		int newy = b[id].second + dy[i];
		if (distance2(newx, newy) > _max) {
			_max = distance2(newx, newy);
			pos = i;
		}
	}
	cout << ans[pos] << endl;
	last_move = pos;
}

int bfs(int enemy_id) {
	memset(vis, 0, sizeof(vis));
	queue< pii > p;
	p.push(mp(mp(b[enemy_id].first, b[enemy_id].second), 0));
	vis[b[enemy_id].first][b[enemy_id].second] = 1;
	while (!p.empty()) {
		pii x = p.front();
		p.pop();
		for (int i = 0; i < 4; i++) {
			int newx = x.first.first + dx[i];
			int newy = x.first.second + dy[i];
			if (!check(newx, newy) || vis[newx][newy]) continue;
			if (a[newx][newy] == tmp_id) {
				return x.second + 1;
			}
			else {
				vis[newx][newy] = 1;
				p.push(mp(mp(newx, newy), x.second + 1));
			}
		}
	}	
	return 0;
}

pii bfs2() {
	memset(vis, 0, sizeof(vis));
	queue< pii > p;
	p.push(mp(mp(b[id].first, b[id].second), 0));
	vis[b[id].first][b[id].second] = 1;
	while (!p.empty()) {
		pii x = p.front();
		p.pop();
		for (int i = 0; i < 4; i++) {
			int newx = x.first.first + dx[i];
			int newy = x.first.second + dy[i];
			if (!check(newx, newy) || vis[newx][newy] || a[newx][newy] == tmp_id) continue;
			if (a[newx][newy] == cell_id) {
				return mp(mp(newx, newy), x.second + 1);
			}
			else {
				vis[newx][newy] = 1;
				p.push(mp(mp(newx, newy), x.second + 1));
			}
		}
	}
	return mp(mp(b[id].first, b[id].second), 0);
}

void process_outside() {
	int move = 10000;
	for (int i = 1; i <= number_of_player; i++) {
		if (i == id) continue;
		if (b[i].first == -1) continue;
		move = min(move, bfs(i));
		pii x = bfs2();
		int home = x.second;
		if (flag || move <= home + 5) {
			flag = true;
			int pos = 0, _min = 100000;
			for (int i = 0; i < 4; i++)	{
				int newx = b[id].first + dx[i];
				int newy = b[id].second + dy[i];
				if (check(newx, newy) && i != invalid[last_move] && a[newx][newy] != tmp_id) {
					if (distance(newx, newy, x.first.first, x.first.second) < _min) {
						_min = distance(newx, newy, x.first.first, x.first.second);
						pos = i;
					}
				}
			}
			cout << ans[pos] << endl;
			last_move = pos;
			return;
		}
		else {
			int i = last_move;
			{
				int newx = b[id].first + dx[i];
				int newy = b[id].second + dy[i];
				if (check(newx, newy) && a[newx][newy] != tmp_id) {
					cout << ans[i] << endl;
					last_move = i;
					return;
				}
			}
			for (i = 0; i < 4; i++) {
				int newx = b[id].first + dx[i];
				int newy = b[id].second + dy[i];
				if (check(newx, newy) && i != last_move && i != invalid[last_move] && a[newx][newy] != tmp_id) {
					cout << ans[i] << endl;
					last_move = i;
					return;
				}
			}
		}
	}
}

int main() {
	cin >> number_of_player;
	cin >> id;
	cell_id = id * 2 - 1;
	tmp_id = id * 2;
	n = 20, m = 30;
	while (1) {
		for (int i = 0; i < n; i++) { 
			for (int j = 0; j < m; j++) {
				char ch;
				cin >> ch;
				a[i][j] = ch - '0';
			}
		}
		for (int i = 1; i <= number_of_player; i++) {
			cin >> b[i].first >> b[i].second;
		}
		if (a[b[id].first][b[id].second] == cell_id) {
			process_inside();
		}
		else {
			process_outside();
		}
		fflush(stdout);
	}
	return 0;
}