#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

int main() {
	ofstream fout("recipe.out");
	ifstream fin("recipe.in");
	int T;
	fin >> T;
	for (int t = 0; t<T; t++) {
		int N, P;
		fin >> N >> P;
		long size[60];
		vector<vector<long> > packs(N,vector<long>(P));
		int in[60];
		long tmax[60];
		long tmin[60];
		for (int n = 0; n < N; n++) {
			long temp;
			fin >> temp;
			size[n] = temp;
		}
		for (int n = 0; n < N; n++) {
			for (int p = 0; p < P; p++) {
				long temp;
				fin >> temp;
				packs[n][p] = temp;
			}
			sort(packs[n].begin(), packs[n].end());
			in[n] = P-1;
		}
		bool go = true;
		int count = 0;
		while (go) {
			long mi = 1000010;
			for (int n = 0; n < N; n++) {
				double temp = packs[n][in[n]];
				tmax[n] = floor((temp / 0.9) / size[n]);
				tmin[n] = ceil((temp / 1.1) / size[n]);
				while (tmin[n]>tmax[n] && in[n] > -1) {
					in[n]--;
					if (in[n] > -1) {
						double temp = packs[n][in[n]];
						tmax[n] = floor((temp / 0.9) / size[n]);
						tmin[n] = ceil((temp / 1.1) / size[n]);
					}
				}
				mi = min(tmax[n], mi);
			}
			bool going = true;
			while (going) {
				going = false;
				for (int n = 0; n < N; n++) {
					while ((in[n] > -1)&&((tmin[n] > mi) || (tmin[n] > tmax[n]))) {
						in[n]--;
						going = true;
						if (in[n] > -1) {
							double temp = packs[n][in[n]];
							tmax[n] = floor((temp / 0.9) / size[n]);
							tmin[n] = ceil((temp / 1.1) / size[n]);
							mi = min(tmax[n], mi);
						}
					}
				}
			}
			for (int n = 0; n < N; n++) {
				if (in[n] < 0) go = false;
			}
			if (go) {
				count++;
				for (int n = 0; n < N; n++) {
					in[n]--;
				}
			}
			for (int n = 0; n < N; n++) {
				if (in[n] < 0) go = false;
			}
		}
		fout << "Case #" << t + 1 << ": " << count << endl;
		cout << "Case #" << t + 1 << ": " << count << endl;
	}
	system("pause");
}