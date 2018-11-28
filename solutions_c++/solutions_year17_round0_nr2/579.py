#include <cstdio>
#include <string>
using namespace std;

int t;
long long n;
string ns;

int main(void) {
	FILE *fin = fopen("B-large.in", "r");
	FILE *fout = fopen("output.txt", "w");

	fscanf(fin, "%d", &t);
	for (int iter = 1; iter <= t; iter++) {
		fprintf(fout, "Case #%d: ", iter);
		fscanf(fin, "%lld", &n);
		if (n < 10) {
			fprintf(fout, "%lld\n", n);
			continue;
		}

		ns = to_string(n);
		int fl = -1;
		for (int i = 1; i < ns.length(); i++)
			if (ns[i - 1] > ns[i]) {
				fl = i - 1;
				break;
			}

		if (fl == -1) {
			fprintf(fout, "%lld\n", n);
			continue;
		}
		
		for (; fl >= 1; fl--)
			if (ns[fl] != ns[fl - 1])
				break;
		
		if (ns[fl] == '1') {
			for (int i = 0; i < ns.length() - 1; i++)
				fprintf(fout, "%d", 9);
			fprintf(fout, "\n");
		}
		else {
			for (int i = 0; i < fl; i++)
				fprintf(fout, "%c", ns[i]);
			fprintf(fout, "%c", ns[fl] - 1);
			for (int i = fl + 1; i < ns.length(); i++)
				fprintf(fout, "%d", 9);
			fprintf(fout, "\n");
		}
	}
	fclose(fin);
	fclose(fout);
	return 0;
}