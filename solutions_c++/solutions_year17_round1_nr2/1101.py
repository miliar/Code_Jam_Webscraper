#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <unordered_set>

using namespace std;

unordered_set<int> calc_q(int q, int r) {
	unordered_set<int> rv;
	double v = (double)q / r;

	if (v < 0.9)
		return rv;
	int idx = floor(v);
	
	int target = r * (idx);
	if (q >= target*0.9 && q <= target*1.1)
		rv.insert(idx);

	int i = 1;
	while(true){
		target = r * (idx+i);

		if (q >= target*0.9 && q <= target*1.1)
			rv.insert(idx + i);
		else
			break;
		++i;
	}
	i = 1;
	while (true) {
		target = r * (idx - i);

		if (q >= target*0.9 && q <= target*1.1)
			rv.insert(idx + i);
		else
			break;
		--i;
	}
	return rv;
}
struct vect {
	vector<int> v;
	vector<unordered_set<int>> ref;
	int ofs;
};

unordered_set<int> inters(unordered_set<int>& a, unordered_set<int>& b) {
	unordered_set<int> rv;
	for (auto i : a) {
		if (b.find(i) != b.end()) {
			rv.insert(i);
		}
	}
	return rv;
}
int check(vector<vect>& ing, vector<int>& quan, unordered_set<int>& ref, int idx, int& res) {
	if (idx == ing.size()) {
		++res;
		return 1;
	}

	for (int i = ing[idx].ofs; i < ing[idx].v.size(); ++i) {
		if (ing[idx].ref[i].size() == 0) continue;

		unordered_set<int> tmp = inters(ref, ing[idx].ref[i]);
		if(tmp.size() > 0){
			int r = check(ing, quan, tmp, idx + 1, res);
			if (r == 1) {
				ing[idx].ofs = i+1;
			}
		}
	}
}

int main() {
#ifdef _DEBUG
	std::ifstream in("C:\\Users\\silvio.lazzeretti\\Downloads\\example_2.in");
	std::streambuf *cinbuf = std::cin.rdbuf(); //save old buf
	std::cin.rdbuf(in.rdbuf()); //redirect std::cin to in.txt!
#endif
	int T;
	cin >> T;
	int t = 0;
	while (++t <= T) {
		int res = 0;
		int N, P;
		cin >> N >> P;

		vector<int> quan(N);
		for(int i=0;i<N;++i)
			cin >> quan[i];

		vector<vect> ing(N);
		for (int i = 0; i < N; ++i) {
			ing[i].ofs = 0;
			for (int j = 0; j < P; ++j) {
				int q;
				cin >> q;
				auto qq = calc_q(q, quan[i]);
				ing[i].v.push_back(q);
			}
			sort(ing[i].v.begin(), ing[i].v.end());
			for (int j = 0; j < P; ++j) {
				auto qq = calc_q(ing[i].v[j], quan[i]);
				ing[i].ref.push_back(qq);
			}
		}

		for (int i = 0; i < ing[0].v.size(); ++i) {
			if(ing[0].ref[i].size() > 0)
				check(ing,quan, ing[0].ref[i], 1, res);
		}

		cout << "Case #" << t << ": ";
		cout << res;
		cout << endl;
	}
	return 0;
}