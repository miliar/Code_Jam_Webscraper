#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <unordered_set>
#include <iomanip>
#include <limits>

using namespace std;
struct intv {
	int a, b;
	int p;
};
int main() {
#ifdef _DEBUG
	std::ifstream in("C:\\Users\\silvio.lazzeretti\\Downloads\\b.in");
	std::streambuf *cinbuf = std::cin.rdbuf(); //save old buf
	std::cin.rdbuf(in.rdbuf()); //redirect std::cin to in.txt!
#endif
	int T;
	cin >> T;
	int t = 0;
	while (++t <= T) {
		int ac, aj; 
		cin >> ac >> aj;
		vector<int> rem(2,720);
		vector<intv> d;
		for (int i = 0; i < ac; ++i) {
			int a, b;
			cin >> a >> b;
			rem[1] -= b - a;
			d.push_back({ a,b,1 });
		}
		for (int i = 0; i < aj; ++i) {
			int a, b;
			cin >> a >> b;
			rem[0] -= b - a;
			d.push_back({ a,b,0 });
		}

		sort(d.begin(), d.end(), [](intv& a, intv& b) {
			return a.a < b.a;
		});

		vector<intv> best;
		for (int i = 0; i < d.size(); ++i) {
			if (d[i].p == d[(i + 1)%d.size()].p) {
				best.push_back({ d[i].b,d[(i + 1) % d.size()].a,d[i].p });
			}
		}

		sort(best.begin(), best.end(), [](intv& a, intv& b) {
			return (a.b - a.a+1440) % 1440 < (b.b - b.a+1440) % 1440;
		});

		for (auto ii : best) {
			if (rem[ii.p] >= (ii.b - ii.a+1440)%1440) {
				rem[ii.p] -= (ii.b - ii.a+1440) % 1440;
				d.push_back(ii);
			}
		}

		vector<int> dd(1440, -1);
		for (auto ii : d) {
			for (int i = 0; i < (ii.b-ii.a+1440)%1440; ++i)
				dd[(i+ii.a)%1440] = ii.p;
		}

		int start = 0;
		for (int i = 0; i < dd.size(); ++i) {
			if (dd[i] !=- 1) {
				start = i;
				break;
			}
				
		}

		for (int i = 0; i < 1439; ++i) {
			if (dd[i]!=-1 && dd[i + 1] == -1) {
				if (rem[dd[i]] > 0) {
					dd[i + 1] = dd[i];
					rem[dd[i]]--;
				}
				else if (rem[(dd[i]+1)%2] > 0) {
					dd[i + 1] = (dd[i] + 1) % 2;
					rem[(dd[i] + 1) % 2]--;
				}
			}
		}
	
		int i = 0;
		while (dd[i] == -1) {
			if (rem[dd[(1440+i-1)%1440]] > 0) {
				dd[i] = dd[(1440 + i - 1) % 1440];
				rem[dd[(1440 + i - 1) % 1440]]--;
			}
			else if (rem[(dd[(1440 + i - 1) % 1440] + 1) % 2] > 0) {
				dd[i] = (dd[(1440 + i - 1) % 1440] + 1) % 2;
				rem[(dd[(1440 + i - 1) % 1440] + 1) % 2]--;
			}
			++i;
		}

		int cnt = 0;
		int last = dd[1439];
		for (int i = 0; i < dd.size(); ++i){
			if (dd[i] != last) {
				++cnt;
				last = dd[i];
			}
		}

		cout << "Case #" << t << ": " << cnt;

		cout << endl;
	}
	return 0;
}