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
#include <string>
#define rep(i,n) for(int i=0;i<n;i++)

using namespace std;

int T;
int N;
int R, O, Y, G, B, V;

int main()
{
	std::string dir = "../../1B/";
	fstream fin(dir + "B-small-attempt0.in", ifstream::in);
	fstream fout(dir + "B-small-attempt0.out", ofstream::out);

	cout.precision(10);
	fout.precision(10);

	fin >> T;
	for (int t = 1; t <= T; t++)
	{
		fin >> N >> R >> O >> Y >> G >> B >> V;

		vector< pair<int, char> > conf;
		conf.push_back(make_pair(R, 'R'));
		conf.push_back(make_pair(Y, 'Y'));
		conf.push_back(make_pair(B, 'B'));

		sort(conf.begin(), conf.end());
		reverse(conf.begin(), conf.end());

		string ret;

		if (conf[1].first + conf[2].first < conf[0].first) {
			ret = "IMPOSSIBLE";
			fout << "Case #" << t << ": " << ret << "\n";
			cout << "Case #" << t << ": " << ret << "\n";
			continue;
		}

		while (conf[1].first > conf[2].first) {
			ret.push_back(conf[0].second);
			ret.push_back(conf[1].second);
			conf[0].first--;
			conf[1].first--;
		}

		while (conf[0].first > 0) {
			ret.push_back(conf[0].second);
			ret.push_back(conf[1].second);
			conf[0].first--;
			conf[1].first--;

			if (conf[0].first > 0) {
				ret.push_back(conf[0].second);
				ret.push_back(conf[2].second);
				conf[0].first--;
				conf[2].first--;
			}
		}

		int ind1 = 2, ind2 = 1;
		if (ret[ret.size() - 1] == conf[2].second) {
			ind1 = 1;
			ind2 = 2;
		}

		while (conf[ind1].first > 0 && conf[ind2].first > 0) {
			ret.push_back(conf[ind1].second);
			ret.push_back(conf[ind2].second);
			conf[ind1].first--;
			conf[ind2].first--;
		}

		if (conf[ind1].first > 0) {
			ret.push_back(conf[ind1].second);
			conf[ind1].first--;
		}


		fout << "Case #" << t << ": " << ret << "\n";
		cout << "Case #" << t << ": " << ret << "\n";
	}
	fin.close();
	fout.close();
	cout << "running time=" << clock() / (double)CLOCKS_PER_SEC;
	system("PAUSE");
	return 0;
}
