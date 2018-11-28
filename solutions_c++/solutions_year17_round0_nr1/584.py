#include <cstdio>
#include <string>
using namespace std;

int t, k;
string s;
char buf[1010];

int main(void) {
	FILE *fin = fopen("A-large.in", "r");
	FILE *fout = fopen("output.txt", "w");

	fscanf(fin, "%d", &t);
	for (int iter = 1; iter <= t; iter++) {
		fprintf(fout, "Case #%d: ", iter);
		fscanf(fin, "%s%d", buf, &k);
		s = string(buf);

		int cnt = 0;
		for (int i = 0; i <= s.length() - k; i++) {
			if (s[i] == '-') {
				cnt++;
				for (int j = 0; j < k; j++)
					s[i + j] = (s[i + j] == '-' ? '+' : '-');
			}
		}

		bool f = true;
		for (int i = s.length() - k + 1; f && i < s.length(); i++)
			if (s[i] == '-')
				f = false;
		if (f)
			fprintf(fout, "%d\n", cnt);
		else
			fprintf(fout, "IMPOSSIBLE\n");
	}
	fclose(fin);
	fclose(fout);
	return 0;
}