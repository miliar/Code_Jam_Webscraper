#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cassert>
#include <iomanip>
#include <algorithm>
using namespace std;

using ll = long long int;
ifstream fin("2.in");
ofstream fout("2.out");

int main() {
	int T;
	fin >> T;
	for (int t = 1; t <= T; t++) {
		int N, C, M;
		fin >> N >> C >> M;
		int pos[1000];
		int holder[1000];
		for (int i = 0; i < M; i++) {
			fin >> pos[i] >> holder[i];
			holder[i]--;
			pos[i]--;
		}
		int nTickets[1000] = {};
		for (int i = 0; i < M; i++)
			nTickets[holder[i]]++;
		int a = 0;
		for (int i = 0; i < C; i++)
			a = max(a, nTickets[i]);

		int hist[1000] = {}, accum[1000] = {};
		for (int i = 0; i < M; i++)
			hist[pos[i]]++;
		for (int i = 0; i < N; i++) {
			accum[i] = hist[i];
			if(i > 0)
				accum[i] += accum[i-1];
		}
		int b = 0;
		for (int i = 0; i < N; i++)
			b = max(b,(accum[i] + i) / (i+1));
		
		int nCoasters = max(a, b);
		int nPromos = 0;
		for (int i = 0; i < N; i++)
			nPromos += max(hist[i] - nCoasters, 0);

			
		fout << "Case #" << t << ": " << nCoasters << " " << nPromos << endl;
	}
}
