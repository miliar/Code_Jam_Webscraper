#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int main()
{
	ifstream fin;
	ofstream fout;
	fin.open("C-large.in");
	fout.open("output3.txt");

	int T;
	fin >> T;

	for (int cas = 1; cas <= T; cas++){
		long long n, k;
		fin >> n >> k;

		fout << "Case #" << cas << ": ";

		long long now = 1;
		long long t = 1;
		long long ls = ((n - 1) / 2);
		long long rs = ((n - 1) / 2) + ((n - 1) % 2);
		long long lsn = 1;
		long long rsn = 1;

		if (ls == rs){
			rsn = 2;
			lsn = 0;
		}

		if (k != 1){
			while (1){
				t *= 2;
				now += t;

				if (now >= k){
					if (k - (now - t) <= rsn){
						ls = (rs - 1) / 2;
						rs = ((rs - 1) / 2) + ((rs - 1) % 2);
					}
					else{
						rs = ((ls - 1) / 2) + ((ls - 1) % 2);
						ls = ((ls - 1) / 2);
					}
					break;
				}

				if (rs == ls){
					rs = ((ls - 1) / 2) + ((ls - 1) % 2);
					ls = ((ls - 1) / 2);

					if (rs == ls)
						rsn = rsn * 2;
					else
						lsn = rsn;
				}
				else if (rs % 2){
					rs = ((ls - 1) / 2) + ((ls - 1) % 2);
					ls = ((ls - 1) / 2);

					rsn = rsn * 2 + lsn;
				}
				else{
					ls = ((rs - 1) / 2);
					rs = ((rs - 1) / 2) + ((rs - 1) % 2);

					lsn = lsn * 2 + rsn;
				}
			}
		}
		
		if (rs < 0)
			rs = 0;
		if (ls < 0)
			ls = 0;

		fout << rs << ' ' << ls << endl;
	}
}