#include<iostream>
#include<fstream>
#include<vector>
#include<string>
#include<map>
#include<list>
#include<queue>
#include<algorithm>
#include<functional>
using namespace std;


ifstream fin("A-large.in");
ofstream fout("output.txt");

int T;
int D, N;
int K[1001];
int S[1001];

int main() {

	fin >> T;
	//printf("%.6f", D /max_time);
	fout << fixed;
	fout.precision(6);

	for (int t = 1; t <= T; t++) {
		fout << "Case #" << t << ": ";
		fin >> D >> N;
		double max_time = 0.0;
		for (int n = 0; n < N; n++) {
			fin >> K[n] >> S[n];
			
			int dist = D - K[n];
			double time = dist /(double) S[n];
			if (max_time < time)
				max_time = time;
		}
		
		fout << D / max_time;
		fout << "\n";
	}

	return 0;
}