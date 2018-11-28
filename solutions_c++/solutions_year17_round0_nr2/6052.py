#include <cstdio>
#include <cstring>

int N[20] = { 0 };
int length;

void find_tidy(int index)
{
	if (index < 0) return;
	int i;
	for (i = index; i >= 0; i--) {
		if (N[i] > N[i + 1]) {
			N[i]--;
			for (int j = i+1; j < length; j++) {
				N[j] = 9;
			}
			break;
		}
	}
	if (index == 0) return;
	else find_tidy(i-1);
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		char N_char[20] = { 0 };
		scanf("%s", N_char);
		int i = 0;
		length = strlen(N_char);
		while (N_char[i] != 0) {
			N[i] = N_char[i] - '0';
			i++;
		}
		find_tidy(length-2);

		bool leading_zero = true;
		char ans[20] = { 0 };
		int ans_index = 0;
		for (int j = 0; j < length; j++) {
			if (leading_zero && N[j] == 0) continue;
			leading_zero = false;
			ans[ans_index++] = N[j] + '0';
		}
		printf("Case #%d: %s\n", t, ans);
	}

	fclose(stdin);
	fclose(stdout);
	return 0;
}