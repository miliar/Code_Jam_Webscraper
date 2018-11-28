#include <cstdio>
#include <cstring>

int main () {
	char pancs[1010];
	int t, flp, size, ans;
	bool print;
	scanf ("%d", &t);

	for (int i = 1; i <=t; i++) {
		scanf ("%s %d", pancs, &flp);
		size = strlen (pancs);
		ans = 0;
		print = false;

		for (int j = 0; j <= size-flp; j++) {
			if (pancs[j] == '-') {
				ans++;
				for (int k = j; k < j+flp; k++)
					pancs[k] = (pancs[k] == '+') ? '-' : '+';
			}
		}

		for (int j = size-flp; j<size; j++)
			if (pancs[j] == '-') {
				printf ("Case #%d: IMPOSSIBLE\n", i);
				print = true;
				break;
			}
			
	
		if (!print)
			printf ("Case #%d: %d\n", i, ans);
	}

	return 0;
}
