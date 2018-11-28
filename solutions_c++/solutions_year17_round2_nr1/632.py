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
unsigned long long N, D;
vector<int> K, S;

pair<unsigned long long, unsigned long long> GetLR(unsigned long long NN) {
	if (NN & 1ll)
		return make_pair(NN / 2, NN / 2);
	else
		return make_pair(NN / 2, NN / 2 - 1);
}

vector< pair<unsigned long long, unsigned long long> > conf_new, conf_old;

int main()
{
	std::string dir = "../../1B/";
	fstream fin(dir + "A-large.in", ifstream::in);
	fstream fout(dir + "A-large.out", ofstream::out);

	cout.precision(10);
	fout.precision(10);

	fin >> T;
	for (int t = 1; t <= T; t++)
	{
		fin >> D >> N;
		K.resize(N);
		S.resize(N);

		rep(i, N)
			fin >> K[i] >> S[i];

		vector<double> times(N);

		rep(i, N)
			times[i] = (D - K[i]) / (double)(S[i]);

		sort(times.begin(), times.end());

		fout << "Case #" << t << ": " << D / times[times.size()-1] << "\n";
		cout << "Case #" << t << ": " << D / times[times.size() - 1] << "\n";
	}
	fin.close();
	fout.close();
	cout << "running time=" << clock() / (double)CLOCKS_PER_SEC;
	system("PAUSE");
	return 0;
}
