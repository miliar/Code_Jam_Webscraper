#include <cstdio>
#include <iostream>
#include <fstream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <queue>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define rep(i,n) for(int i=0;i<n;i++)

using namespace std;

int T;
int N, P;
vector<int> G;


int main()
{
	std::string dir = "../../2/";
	fstream fin(dir + "A-large.in", ifstream::in);
	fstream fout(dir + "A-large.out", ofstream::out);

	cout.precision(10);
	fout.precision(10);

	fin >> T;
	for (int t = 1; t <= T; t++)
	{
		fin >> N >> P;
		
		G.resize(N);
		rep(i, N)
			fin >> G[i];

		int ret = 0;

		if (P == 2) {
			int N0 = 0, N1 = 0;
			rep(i, N)
				if (G[i] % P == 0) N0++;
			N1 = N - N0;

			ret = N1 / 2;
		}
		else if (P == 3) {
			int N0 = 0, N1 = 0, N2 = 0;
			rep(i, N) {
				if (G[i] % P == 0) N0++;
				if (G[i] % P == 1) N1++;
				if (G[i] % P == 2) N2++;
			}

			ret = (min(N1,N2));
			ret += 2 * (abs(N1 - N2) / 3);
			if ((abs(N1 - N2) % 3 == 2)) ret++;
		}
		else if (P == 4) {
			int N0 = 0, N1 = 0, N2 = 0, N3 = 0;
			rep(i, N) {
				if (G[i] % P == 0) N0++;
				if (G[i] % P == 1) N1++;
				if (G[i] % P == 2) N2++;
				if (G[i] % P == 3) N3++;
			}

			ret = N2 / 2;
			ret += (min(N1, N3));
			ret += 3 * (abs(N1 - N3) / 4);
			if ((abs(N1 - N3) % 4 == 2)) ret += 1;
			if ((abs(N1 - N3) % 4 == 3)) ret += 2;
			if ((abs(N1 - N3) % 4 != 0) && (abs(N1 - N3) % 4 != 3)) ret += (N2%2);
		}

		ret = N - ret;

		fout << "Case #" << t << ": " << ret << "\n";
		cout << "Case #" << t << ": " << ret << "\n";
	}
	fin.close();
	fout.close();
	cout << "running time=" << clock() / (double)CLOCKS_PER_SEC;
	//system("PAUSE");
	return 0;
}
