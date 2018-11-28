#include <stdio.h>
#include <vector>

struct point {
	int x, y;
	point(int x, int y) : x(x), y(y) {}
};

struct shooter;
struct hitmap {
	bool success;
	int dir;
	int visited[50][50];
	shooter *parent;
	hitmap() {
		success = false;
		memset(visited, 0, sizeof(visited));
	}
};

struct shooter {
	int x, y;
	bool used;
	hitmap vhit, hhit;
	shooter(int x, int y) : x(x), y(y), used(false) {}
};

int h, w;
char map[50][51];
int totvisited[50][50];
int requireVisit[50][50];
std::vector<shooter> shooters;

int dfs(hitmap &hm, int x, int y, int dx, int dy) {
	while (true) {
		if (x < 0 || x >= w || y < 0 || y >= h) return true;
		if (map[y][x] == '-' || map[y][x] == '|') return false;

		if (map[y][x] == '.') {
			if (!hm.visited[y][x]) {
				hm.visited[y][x] = 1;
			}
		}
		else if (map[y][x] == '#') {
			return true;
		}
		else if (map[y][x] == '/') {
			std::swap(dx, dy);
			dx = -dx;
			dy = -dy;
		}
		else if (map[y][x] == '\\') {
			std::swap(dx, dy);
		}
		else throw "";
		x += dx;
		y += dy;
	}
}

hitmap test(shooter &orig, int dir) {
	int dx = 0, dy = 0;
	if (dir == 0) dx = 1;
	else dy = 1;
	hitmap hm;
	hm.parent = &orig;
	hm.dir = dir;
	if (dfs(hm, orig.x + dx, orig.y + dy, dx, dy) &&
		dfs(hm, orig.x - dx, orig.y - dy, -dx, -dy))
	{
		hm.success = true;
		return hitmap(hm);
	}
	hm.success = false;
	return hitmap(hm);
}

void put(hitmap &hm) {
	if (hm.dir == 0) {
		map[hm.parent->y][hm.parent->x] = '-';
	}
	else {
		map[hm.parent->y][hm.parent->x] = '|';
	}
	for (int y = 0; y < h; y++) {
		for (int x = 0; x < w; x++) {
			if (hm.visited[y][x]) {
				requireVisit[y][x] = 0;
			}
			if (hm.parent->hhit.success && hm.parent->hhit.visited[y][x] ||
				hm.parent->vhit.success && hm.parent->vhit.visited[y][x])
			{
				totvisited[y][x]--;
			}
		}
	}
	hm.parent->used = true;
}

void solve() {
	shooters.clear();
	scanf("%d %d", &h, &w);
	for (int y = 0; y < h; y++) {
		scanf("%s", map[y]);
	}

	for (int y = 0; y < h; y++) {
		for (int x = 0; x < w; x++) {
			requireVisit[y][x] = 0;
			totvisited[y][x] = 0;
			char c = map[y][x];
			if (c == '-' || c == '|') {
				shooters.push_back(shooter(x, y));
			}
			else if (c == '.') {
				requireVisit[y][x] = 1;
			}
		}
	}

	std::vector<shooter*> oneway;
	for (int i = 0; i < shooters.size(); i++) {
		shooter &s = shooters[i];
		s.hhit = test(s, 0);
		s.vhit = test(s, 1);
		for (int y = 0; y < h; y++) {
			for (int x = 0; x < w; x++) {
				totvisited[y][x] +=
					(s.hhit.success && s.hhit.visited[y][x]) ||
					(s.vhit.success && s.vhit.visited[y][x]);
			}
		}
		int ways = s.hhit.success + s.vhit.success;
		if (ways == 0) {
			printf("IMPOSSIBLE\n");
			return;
		}
		else if (ways == 1) {
			oneway.push_back(&shooters[i]);
		}
	}

	for (int i = 0; i < oneway.size(); i++) {
		shooter &s = *oneway[i];
		if (s.hhit.success) {
			put(s.hhit);
		}
		else {
			put(s.vhit);
		}
	}

	int bestX, bestY, bestTot;
	while (true) {
		bestTot = 2e9;
		for (int y = 0; y < h; y++) {
			for (int x = 0; x < w; x++) {
				if (requireVisit[y][x]) {
					if (totvisited[y][x] < bestTot) {
						if (totvisited[y][x] < 0) throw "";
						bestTot = totvisited[y][x];
						bestX = x;
						bestY = y;
					}
				}
			}
		}
		if (bestTot == 2e9) break;
		if (bestTot == 0) {
			printf("IMPOSSIBLE\n");
			return;
		}
		for (int i = 0; i < shooters.size(); i++) {
			if (shooters[i].used) continue;
			if (shooters[i].hhit.visited[bestY][bestX]) {
				put(shooters[i].hhit);
				break;
			}
			else if (shooters[i].vhit.visited[bestY][bestX]) {
				put(shooters[i].vhit);
				break;
			}
		}
	}

	for (int i = 0; i < shooters.size(); i++) {
		shooter &s = shooters[i];
		if (!s.used) {
			put(s.hhit);
		}
	}

	printf("POSSIBLE\n");
	for (int y = 0; y < h; y++) {
		for (int x = 0; x < w; x++) {
			printf("%c", map[y][x]);
		}
		printf("\n");
	}
}

int main() {
	int T;
	scanf("%d", &T);

	for (int t = 0; t < T; t++) {
		printf("Case #%d: ", t + 1);
		solve();
	}

	return 0;
}
