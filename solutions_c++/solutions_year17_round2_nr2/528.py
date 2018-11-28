#include <cstdio>
int N, R, O, Y, G, B, V;
// R = R
// O = R + Y
// Y = Y
// G = Y + B
// B = B
// V = R + B

int colors[3];

char ans[1111];
int first = -1;
int next(int cur){
	int ans = -1;
	for (int i = 1; i <= 2; i++){
		int nxt = (cur + i) % 3;
		if (colors[nxt] > 0){
			if (ans == -1 ||
				(colors[ans] < colors[nxt]) ||
				(colors[ans] == colors[nxt] && (nxt== first) ))
				ans = nxt;
		}
	}
	return ans;
}

char get_color(int x){
	if (x == 0)
		return 'R';
	if (x == 1)
		return 'Y';
	if (x == 2)
		return 'B';
	return ' ';
}

void work(){
	scanf("%d%d%d%d%d%d%d", &N, &R, &O, &Y, &G, &B, &V);
	colors[0] = R;
	colors[1] = Y;
	colors[2] = B;

	bool ok = true;
	int current = -1;
	if (colors[0] > 0)
		current = 0;
	if (colors[1] > 0)
		if (current == -1 || colors[1] > colors[current])
			current = 1;
	if (colors[2] > 0)
		if (current == -1 || colors[2] > colors[current])
			current = 2;
	first = current;
	for (int i = 0; i < N; i++){
		if (current == -1) {
			puts("IMPOSSIBLE");
			return ;
		}
		ans[i] = get_color(current);
		//printf("put %c\n", ans[i]);
		colors[current] -= 1;
		current = next(current);
	}
	ans[N] = '\0';
	if (ans[N - 1] == ans[0])
		puts("IMPOSSIBLE");
	else
		printf("%s\n", ans);
}

int main(){
	freopen("B.in", "r", stdin);
	int Tcase; scanf("%d", &Tcase);
	for (int T = 1; T <= Tcase; T++){
		printf("Case #%d: ", T);
		work();
	}
}