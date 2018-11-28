#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>

typedef long long int lli;

class bathroomstalls {
	private:
		lli n, k;

		lli solmind, solmaxd;

	public:
		void input(std::istream &is) {
			is >> n >> k;
		}

		void solve() {
			std::map<lli, lli> segments;
			segments[n] = 1;
			lli i = 0;
			while (true) {
				std::pair<lli, lli> maxs = *(segments.rbegin());
				segments.erase(maxs.first);
				lli cmind = (maxs.first - 1) / 2;
				lli cmaxd = maxs.first / 2;
				i += maxs.second;
				if (i >= k) {
					solmind = cmind;
					solmaxd = cmaxd;
					break;
				}
				segments[cmind] += maxs.second;
				segments[cmaxd] += maxs.second;
			}	
		}

		void output(std::ostream &os) {
			os << solmaxd << ' ' << solmind;
		}
};

int main(void) {
	bathroomstalls task;
	int znj;
	std::cin >> znj;
	for (int i = 0; i < znj; ++i) {
		task.input(std::cin);
		task.solve();
		std::cout << "Case #" << (i + 1) << ": ";
		task.output(std::cout);
		std::cout << std::endl;
	}
}
