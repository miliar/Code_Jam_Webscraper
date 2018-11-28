#include <stdio.h>
#include <string.h>
#include <fstream>
using namespace std;
int t, dsize, k;
char d[1002];
int main() {
	ifstream fin;
	ofstream fout;
	fin.open("A-large.in");
	fout.open("out.in");
	fin >> t;
	fin.getline(d, 20);

	//scanf("%d", &t);
	for (int iter = 1; iter <= t; iter++) {
		//scanf("%s %d", d, &k);
		fin >> d >> k;
		bool f = false;
		int cnt = 0;
		dsize = strlen(d);
		for (int i = 0; i < dsize - k + 1; i++) {
			if (d[i] == '-') {
				cnt++;
				d[i] = '+';
				for (int j = 1; j < k; j++) {
					if (d[i + j] == '-') d[i + j] = '+';
					else d[i + j] = '-';
				}
			}
		}
		for (int i = dsize - k + 1; i < dsize; i++) {
			if (d[i] == '-') {
				f = true;
				break;
			}
		}
		/*if (f) printf("IMPOSSIBLE\n");
		else printf("Case #%d: %d\n", iter, cnt);*/
		if (f) fout << "Case #" << iter << ": " << "IMPOSSIBLE\n";
		else fout << "Case #" << iter << ": " << cnt << endl;
	}

	fin.close();
	fout.close();
	return 0;
}