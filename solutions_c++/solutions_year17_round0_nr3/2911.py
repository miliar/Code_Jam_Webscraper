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
unsigned long long N, K;

pair<unsigned long long, unsigned long long> GetLR(unsigned long long NN) {
	if (NN & 1ll)
		return make_pair(NN / 2, NN / 2);
	else
		return make_pair(NN / 2, NN / 2 - 1);
}

vector< pair<unsigned long long, unsigned long long> > conf_new, conf_old;

int main()
{
		std::string dir = "../../qual/";
		fstream fin(dir + "C-large.in",ifstream::in);
    fstream fout(dir + "C-large.out",ofstream::out);
    fin >> T;
    for(int t=1;t<=T;t++)
    {
			fin >> N >> K;

			pair<unsigned long long, unsigned long long> tpair;

			conf_new.resize(0);
			conf_new.push_back(make_pair(N, 1));
			conf_old = conf_new;

			unsigned long long num = 0;
			while (num < K) {
				map<unsigned long long, unsigned long long> mp;
				mp.clear();
				rep(i, conf_old.size()) {
					num += conf_old[i].second;
					tpair = GetLR(conf_old[i].first);

					if (mp.count(tpair.first) == 0)
						mp[tpair.first] = conf_old[i].second;
					else
						mp[tpair.first] += conf_old[i].second;

					if (mp.count(tpair.second) == 0)
						mp[tpair.second] = conf_old[i].second;
					else
						mp[tpair.second] += conf_old[i].second;

					if (num >= K) {
						break;
					}
				}

				if (num >= K) {
					break;
				}

				conf_new.resize(0);

				for (std::map<unsigned long long, unsigned long long>::iterator it = mp.begin(); it != mp.end(); ++it)
					conf_new.push_back(make_pair(it->first, it->second));

				sort(conf_new.begin(), conf_new.end());
				reverse(conf_new.begin(), conf_new.end());

				conf_old = conf_new;

			}

			fout << "Case #" << t << ": " << tpair.first << " " << tpair.second << "\n";
			cout << "Case #" << t << ": " << tpair.first << " " << tpair.second << "\n";
    }
    fin.close();
    fout.close();
    cout << "running time=" << clock()/(double)CLOCKS_PER_SEC;
    system("PAUSE");
    return 0;
}
