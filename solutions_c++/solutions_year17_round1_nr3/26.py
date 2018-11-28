#include <cstdio>
#include <vector>
#include <cassert>
#include <algorithm>
#include <map>
#include <queue>

struct Pos {

	int dragH;

	int dragA;

	int kniH;

	int kniA;

};

bool operator < (const Pos &left, const Pos &right) {
	if (left.dragH != right.dragH) {
		return left.dragH < right.dragH;
	}
	if (left.dragA != right.dragA) {
		return left.dragA < right.dragA;
	}
	if (left.kniH != right.kniH) {
		return left.kniH < right.kniH;
	}
	return left.kniA < right.kniA;
}

std::string slow(int dragH, int dragA, int kniH, int kniA, int buf, int deb) {
	std::map<Pos, int> moves;
	std::queue<Pos> q;
	{
		Pos pos{dragH, dragA, kniH, kniA};
		moves[pos] = 0;
		q.push(pos);
	}
	while (!q.empty()) {
		Pos cur = q.front();
		q.pop();
		{
			Pos next = cur;
			next.kniH -= next.dragA;
			if (next.kniH <= 0) {
				return std::to_string(moves[cur] + 1);
			}
			next.dragH -= next.kniA;
			if (next.dragH > 0 && moves.count(next) == 0) {
				moves[next] = moves[cur] + 1;
				q.push(next);
			}
		}
		{
			Pos next = cur;
			next.dragA += buf;
			next.dragH -= next.kniA;
			if (next.dragH > 0 && moves.count(next) == 0) {
				moves[next] = moves[cur] + 1;
				q.push(next);
			}
		}
		{
			Pos next = cur;
			next.dragH = dragH;
			next.dragH -= next.kniA;
			if (next.dragH > 0 && moves.count(next) == 0) {
				moves[next] = moves[cur] + 1;
				q.push(next);
			}
		}
		{
			Pos next = cur;
			next.kniA -= deb;
			if (next.kniA < 0) {
				next.kniA = 0;
			}
			next.dragH -= next.kniA;
			if (next.dragH > 0 && moves.count(next) == 0) {
				moves[next] = moves[cur] + 1;
				q.push(next);
			}
		}
	}
	return "IMPOSSIBLE";
}

void solveOne(int iTest) {
	int dragH, dragA, kniH, kniA, buf, deb;
	scanf("%d %d %d %d %d %d", &dragH, &dragA, &kniH, &kniA, &buf, &deb);
	printf("Case #%d: %s\n", iTest, slow(dragH, dragA, kniH, kniA, buf, deb).c_str());
}

int main() {
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		solveOne(i);
	}
	return 0;
}
