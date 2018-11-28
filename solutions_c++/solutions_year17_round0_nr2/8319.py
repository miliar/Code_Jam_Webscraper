#include <cstdio>
#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main()
{
	FILE *infile, *outfile;
	infile = fopen("input.in", "r");
	outfile = fopen("output.txt", "w");
	int test_case;
	fscanf(infile, "%d", &test_case);

	for (int tc = 1; tc <= test_case; tc++) {
		vector<short> v;
		v.push_back(-1);
		char tmp;
		fscanf(infile, " %c", &tmp);
		while (tmp != '\n') {
			v.push_back(tmp - '0');
			fscanf(infile, "%c", &tmp);
		}
		int ld = 5000;
		for (int i = v.size() - 1; i >= 1; i--) {
			if (v[i - 1] > v[i]) {
				if (i > 1) {
					if (v[i - 1] == v[i - 2]) v[i - 1]--;
				}
				ld = i;
			}
		}
		if (ld != 5000) {
			v[ld - 1]--;
			while (v[ld - 1] == 0) {
				ld--;
				v[ld - 1]--;
			}
			if (ld == 1) {
				v[1] = 0;
				ld = 2;
			}
			for (int i = ld; i < v.size(); i++) {
				v[i] = 9;
			}
		}
		int i = 1;
		while (v[i] == 0) i++;
		fprintf(outfile, "Case #%d: ", tc);
		for (i; i < v.size(); i++) fprintf(outfile, "%hd", v[i]);
		fprintf(outfile, "\n");
	}

	fclose(infile);
	fclose(outfile);

	return 0;
}