#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <cmath>
using namespace std;

struct StallInfo {
	unsigned int _ls;
	unsigned int _rs;
	StallInfo() : _ls(0), _rs(0) {}
	StallInfo(unsigned int ls, unsigned int rs) : _ls(ls), _rs(rs) {}
};

class Bathroom {
	unsigned int _maxdistance;
	map<unsigned int, StallInfo> _m_stalls;
public:
	Bathroom(unsigned int& N) : _maxdistance(N) {
		_m_stalls[0] = StallInfo(0, N);
		_m_stalls[N + 1] = StallInfo(N, 0);
	}
	StallInfo findStall() {
		unsigned int maxdistancefound = 0;
		unsigned int leftmaxdistancefound = 0;
		for (map<unsigned int, StallInfo >::iterator it = _m_stalls.begin(); it != _m_stalls.end(); ++it) {
			map<unsigned int, StallInfo >::iterator previt = it;
			previt--;
			if (it->second._ls == _maxdistance) {
				maxdistancefound = _maxdistance;
				leftmaxdistancefound = (previt)->first;
				break;
			}
			else if (it->second._rs == _maxdistance) {
				maxdistancefound = _maxdistance;
				leftmaxdistancefound = it->first;
				break;
			}
			else if (it->second._ls >= it->second._rs && it->second._ls > maxdistancefound) {
				maxdistancefound = it->second._ls;
				leftmaxdistancefound = (previt)->first;
			}
			else if (it->second._rs > maxdistancefound) {
				maxdistancefound = it->second._rs;
				leftmaxdistancefound = it->first;
			}
		}
		_maxdistance = maxdistancefound;
		// find stall
		unsigned int stallrelativepos = (_m_stalls[leftmaxdistancefound]._rs / 2) + 1;
		StallInfo si(stallrelativepos - 1, maxdistancefound - stallrelativepos);
		_m_stalls[leftmaxdistancefound + stallrelativepos] = si;
		_m_stalls[leftmaxdistancefound]._rs = si._ls;
		_m_stalls[leftmaxdistancefound + maxdistancefound + 1]._ls = si._rs;
		return si;
	}
};

int main(int argc, char const *argv[])
{
	int T;
	cin >> T;
	unsigned int N;
	unsigned int K;
	for (int c = 0; c < T; ++c) {
		cin >> N;
		cin >> K;
		StallInfo si(0, 0);
		Bathroom br(N);
		for (unsigned int i = 0; i < K; ++i) {
			si = br.findStall();
		}
		cout << "Case #" << c + 1 << ": " << max(si._ls, si._rs) << " " << min(si._ls, si._rs) << endl;
	}
	return 0;
}
