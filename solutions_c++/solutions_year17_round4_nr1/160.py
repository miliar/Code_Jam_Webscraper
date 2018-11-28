#include <iostream>
#include <climits>
#include <array>
#include <map>

using namespace std;
typedef long long int Z;

int N, P;
typedef array<int, 4> C;
C cnt;
map<pair<C, int>, int> mem;

int opt(C left, int lo) {
	bool done = true;
	for(int i = 0; i < P; ++i) {
		if(left[i]) done = false;
	}
	if(done) return 0;
	auto it = mem.find(make_pair(left, lo));
	if(it == mem.end()) {
		int val = -1;
		for(int i = 0; i < P; ++i) {
			if(left[i]) {
				--left[i];
				val = max(val, opt(left, (lo + P - i) % P) + (lo ? 0 : 1));
				++left[i];
			}
		}
		if(val == -1) throw 0;
		it = mem.emplace(make_pair(left, lo), val).first;
	}
	return it->second;
}

int main() {
	cin.sync_with_stdio(false);
	cin.tie(nullptr);
	
	int Tc;
	cin >> Tc;
	
	for(int Ti = 1; Ti <= Tc; ++Ti) {
		cin >> N >> P;
		fill(cnt.begin(), cnt.end(), 0);
		mem.clear();
		for(int i = 0; i < N; ++i) {
			int g;
			cin >> g;
			++cnt[g % P];
		}
		cout << "Case #" << Ti << ": ";
		cout << opt(cnt, 0);
		cout << "\n";
	}
	
	return 0;
}
