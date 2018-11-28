#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <vector>

#define INF 1000000000

struct point {
	int x, y;
	char symbol;
	int prio[3];
	point() {
	}
	point(int x, int y, int symbol) : x(x), y(y), symbol(symbol) {}
};

int n, m;
point map[101][101];
point changedMap[101][101];
int points;

void init() {
	points = 0;
	memset(map, 0, sizeof(map));
	memset(changedMap, 0, sizeof(changedMap));
	for (int y = 1; y <= n; y++) {
		for (int x = 1; x <= n; x++) {
			point &p = map[y][x];
			p.x = x;
			p.y = y;
			int dist =
				std::min(std::min(x - 1, n - x), std::min(y - 1, n - y));
			p.prio[0] = n - 1 + 2 * dist;
			p.prio[1] = 2 * n - 2;
			p.prio[2] = p.prio[0] + p.prio[1];

			changedMap[y][x].x = x;
			changedMap[y][x].y = y;
		}
	}
}

point *getLowest(int prio) {
	point *low = 0;
	int bestPrio = INF;
	for (int y = 1; y <= n; y++) {
		for (int x = 1; x <= n; x++) {
			point &p = map[y][x];
			if (p.prio[prio] < bestPrio) {
				low = &p;
				bestPrio = p.prio[0];
			}
			if (prio == 0 && p.prio[1] < bestPrio) {
				low = &p;
				bestPrio = p.prio[1];
			}
		}
	}
	if (low && low->prio < 0) throw "";
	return low;
}

void change2(int y, int x, int dy, int dx, int prio) {
	if (y < 1 || y > n || x < 1 || x > n) return;
	if (map[y][x].prio[prio] < INF) {
		map[y][x].prio[prio]--;
	}
	if (map[y][x].prio[2] < INF) {
		map[y][x].prio[2]--;
	}
	change2(y + dy, x + dx, dy, dx, prio);
}

void change2Plus(int y, int x, int prio) {
	change2(y + 1, x + 1, 1, 1, prio);
	change2(y - 1, x - 1, -1, -1, prio);
	change2(y + 1, x - 1, 1, -1, prio);
	change2(y - 1, x + 1, -1, 1, prio);
}

void change2Cross(int y, int x, int prio) {
	change2(y + 1, x, 1, 0, prio);
	change2(y - 1, x, -1, 0, prio);
	change2(y, x + 1, 0, 1, prio);
	change2(y, x - 1, 0, -1, prio);
}

void change1(int y, int x, int dy, int dx, int prio) {
	if (y < 1 || y > n || x < 1 || x > n) return;

	if (!map[y][x].symbol) {
		if (prio == 0) {
			if (dy == dx) {
				change2(y + 1, x - 1, 1, -1, prio);
				change2(y - 1, x + 1, -1, 1, prio);
			}
			else {
				change2(y + 1, x + 1, 1, 1, prio);
				change2(y - 1, x - 1, -1, -1, prio);
			}
		}
		else if (prio == 1) {
			if (dy) {
				change2(y, x + 1, 0, 1, prio);
				change2(y, x - 1, 0, -1, prio);
			}
			if (dx) {
				change2(y + 1, x, 1, 0, prio);
				change2(y - 1, x, -1, 0, prio);
			}
		}
	}

	map[y][x].prio[prio] = INF;
	map[y][x].prio[2] = INF;
	change1(y + dy, x + dx, dy, dx, prio);
}

void put(int y, int x, char c, bool logChange = true) {
	points++;
	if (!map[y][x].symbol && c == 'o') {
		points++;
	}
	change2Plus(y, x, 0);
	change2Cross(y, x, 1);
	if (c == '+' || c == 'o') {
		change1(y - 1, x - 1, -1, -1, 0);
		change1(y + 1, x + 1, 1, 1, 0);
		change1(y + 1, x - 1, 1, -1, 0);
		change1(y - 1, x + 1, -1, 1, 0);
	}
	if (c == 'x' || c == 'o') {
		change1(y + 1, x, 1, 0, 1);
		change1(y - 1, x, -1, 0, 1);
		change1(y, x + 1, 0, 1, 1);
		change1(y, x - 1, 0, -1, 1);
	}
	if (logChange) {
		changedMap[y][x].symbol = c;
	}
	map[y][x].symbol = c;
	map[y][x].prio[0] = INF;
	map[y][x].prio[1] = INF;
	if (c == 'o') {
		map[y][x].prio[2] = INF;
	}
}

int main() {
	int T;
	scanf("%d", &T);
	
	for (int t = 0; t < T; t++) {
		scanf("%d %d", &n, &m);
		init();
		for (int i = 0; i < m; i++) {
			char c;
			int y, x;
			scanf(" %c %d %d", &c, &y, &x);
			put(y, x, c, false);
		}

		point *next;
		while (next = getLowest(0)) {
			if (next->prio[0] <= next->prio[1]) {
				put(next->y, next->x, '+');
			}
			else {
				put(next->y, next->x, 'x');
			}
		}
		while (next = getLowest(2)) {
			put(next->y, next->x, 'o');
		}
		
		std::vector<point*> changes;
		for (int y = 1; y <= n; y++) {
			for (int x = 1; x <= n; x++) {
				if (changedMap[y][x].symbol) {
					changes.push_back(&changedMap[y][x]);
				}
			}
		}

		printf("Case #%d: %d %d\n", t + 1, points, changes.size());
		for (int i = 0; i < changes.size(); i++) {
			point *p = changes[i];
			printf("%c %d %d\n", p->symbol, p->y, p->x);
		}

#if false
		//Print map
		for (int y = 1; y <= n; y++) {
			for (int x = 1; x <= n; x++) {
				printf("%c", map[y][x].symbol ? map[y][x].symbol : '.');
			}
			printf("\n");
		}
#endif
	}

	return 0;
}
