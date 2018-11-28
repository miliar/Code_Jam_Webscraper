#include <stdio.h>

char v_c[6] = {'R' , 'O', 'Y', 'G', 'B', 'V'};
void func(int i, int &v0, int &v2, int &v4) {
	if (i == 0 && v0 > 0) {
		for (int i = 0; i < v0; i++) {
			printf("%c%c", v_c[3], v_c[0]);
		}
		v0 = 0;
	}
	else if (i == 1 && v2 > 0) {
		for (int i = 0; i < v2; i++) {
			printf("%c%c", v_c[5], v_c[2]);
		}
		v2 = 0;
	}
	else if (i == 2 && v4 > 0) {
		for (int i = 0; i < v4; i++) {
			printf("%c%c", v_c[1], v_c[4]);
		}
		v4 = 0;
	}
}

int main() {
	int T;
	scanf("%d", &T);
	int count = 1;
	int N;
	while(scanf("%d", &N) != EOF) {
		int v[6];
		for (int i = 0; i < 6; i++) {
			scanf("%d", &v[i]);
		}
		int v4 = v[1];
		int v2 = v[5];
		int v0 = v[3];
		int dup_sum = v4 + v2 + v0;
		if (dup_sum > 0) {
				if (v[3] == v[0] && N == v[3] + v[0]) {
					printf("Case #%d: ", count++);
					for (int i = 0; i < v[0]; i++) {
						printf("%c%c", v_c[0], v_c[3]);
					}
					printf("\n");
					continue;
				}
				else if (v[5] == v[2] && N == v[2] + v[5]) {
					printf("Case #%d: ", count++);
					for (int i = 0; i < v[2] ; i++) {
						printf("%c%c", v_c[2], v_c[5]);
					}
					printf("\n");
					continue;
				}
				else if (v[1] == v[4] && N == v[1] + v[4]) {
					printf("Case #%d: ", count++);
					for (int i = 0; i < v[1]; i++) {
						printf("%c%c", v_c[1], v_c[4]);
					}
					printf("\n");
					continue;
				}
			v[0] -= v0;
			v[2] -= v2;
			v[4] -= v4;
		}
		bool t_f = false;
		for (int i = 0; i < 6; i++) {
			if (v[i] < 0) {
				t_f = true;
				break;
			}
		}
		if (v0 > 0 && v[0] <= 0) {
			t_f = true;
		}
		if (v2 > 0 && v[2] <= 0) {
			t_f = true;
		}
		if (v4 > 0 && v[4] <= 0) {
			t_f = true;
		}
		if (t_f) {
			printf("Case #%d: IMPOSSIBLE\n", count++);
			continue;
		}
		int t[3];
		char t_c[3] = {'R', 'Y', 'B'};
		t[0] = v[0];
		t[1] = v[2];
		t[2] = v[4];
		int max_t = 0;
		for (int i = 0; i < 3; i++) {
			if (t[max_t] < t[i])
				max_t = i;
		}
		int max_sum = 0;
		for (int i = 0; i < 3; i++) {
			if (max_t != i) {
				max_sum += t[i];
			}
		}
		if (t[max_t] > max_sum) {
			printf("Case #%d: IMPOSSIBLE\n", count++);
			continue;
		}
		printf("Case #%d: ", count++);
		int num = t[max_t];
		for (int i = 0; i < num; i++) {
			printf("%c", t_c[max_t]);
			func(max_t, v0, v2, v4);
			if (t[max_t] < max_sum) {
				for (int i = 0; i < 3; i++) {
					if (max_t != i) {
						printf("%c", t_c[i]);
						func(i, v0, v2, v4);
						t[i]--;
					}
				}
				max_sum-=2;
				t[max_t]--;
			}
			else {
				for (int i = 0; i < 3; i++) {
					if (max_t != i && t[i] > 0) {
						printf("%c", t_c[i]);
						t[i]--;
						func(i, v0, v2, v4);
						break;
					}
				}
			}
		}
		printf("\n");
	}
}