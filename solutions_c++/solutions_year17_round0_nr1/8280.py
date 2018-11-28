#include <cstdio>
#include <iostream>
#include <queue>
#include <vector>
#include <set>
#include <cstring>
#include <fstream>

using namespace std;

int main()
{
	FILE *infile, *outfile;
	infile = fopen("input.in", "r");
	outfile = fopen("output.txt", "w");
	int tc;
	fscanf(infile, "%d", &tc);
	for (int tci = 1; tci <= tc; tci++) {
		bool vis[1024];
		memset(vis, 0, sizeof(vis));
		int pancake = 0;
		int len = 0;
		int p = 1;
		char ip;
		fscanf(infile, " %c", &ip);
		while (ip != ' ') {
			len++;
			if (ip == '+') {
				pancake += p;
			}
			p *= 2;
			fscanf(infile, "%c", &ip);
		}
		p--;
		fprintf(outfile, "Case #%d: ", tci);
		int k;
		fscanf(infile, "%d", &k);
		int cmp = 1;
		for (int i = 0; i < k; i++) cmp *= 2;
		cmp--;
		vis[pancake] = true;
		long long res = -1;
		queue<pair<int, int>> q;
		q.push(make_pair(pancake, 0));
		while (!q.empty()) {
			int cp = q.front().first;
			int cn = q.front().second;
			q.pop();
			if (cp == p) {
				res = cn;
				break;
			}
			else {
				int ccmp = cmp;
				for (int i = 0; i <= len - k; i++) {
					int np = cp ^ ccmp;
					if (!vis[np]) {
						vis[np] = true;
						q.push(make_pair(np, cn + 1));
					}
					ccmp *= 2;
				}
			}
		}
		if (res == -1) {
			fprintf(outfile, "IMPOSSIBLE\n");
		}
		else {
			fprintf(outfile, "%lld\n", res);
		}
	}

	return 0;
}