#include <cstdio>
#include <queue>
#include <cstring>

using namespace std;

char line[1024];


static inline void proc(int caseno) {
	int len;
	queue<int> range_end;
	int rot_cnt = 0;

	scanf("%s %d", line, &len);

	const int l = strlen(line);
	for (int i = 0; i < l; i++) {
		while (!range_end.empty() && range_end.front() < i)
			range_end.pop();

		if ((range_end.size() + (line[i] == '+' ? 0 : 1)) % 2 == 1) {
			const int last_rot = i + len - 1;
			if (last_rot >= l) {
				printf("Case #%d: IMPOSSIBLE\n", caseno);
				return;
			}

			range_end.push(last_rot);
			rot_cnt++;
		}
	}

	printf("Case #%d: %d\n", caseno, rot_cnt);	
}

int main() {
	int cases;
	scanf("%d", &cases);
	for (int i = 0; i < cases; i++)
		proc(i+1);
	return 0;
}


