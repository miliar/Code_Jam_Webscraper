#include <cstdio>
#include <cstring>

int main()
{
	freopen("A-large.in", "r", stdin);
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		char S[1009] = { 0 };
		char *S_ptr = S;
		int K, index, ans, length;
		scanf("%s %d", S, &K);
		index = 0, ans = 0;
		length = strlen(S);
		while (length-K >= 0) {
			if (*S_ptr == '-') {
				ans++;
				for (int i = 0; i < K; i++) {
					if (*(S_ptr + i) == '+') *(S_ptr + i) = '-';
					else *(S_ptr + i) = '+';
				}
			}
			S_ptr++;
			length--;
		}
		
		bool find = true;
		length = strlen(S);
		for (int i = 0; i < length; i++) {
			if (S[i] == '-') {
				find = false;
				break;
			}
		}
		if (find) printf("Case #%d: %d\n", t, ans);
		else printf("Case #%d: %s\n", t, "IMPOSSIBLE");
	}

	fclose(stdin);
	return 0;
}