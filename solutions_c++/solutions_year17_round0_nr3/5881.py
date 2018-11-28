#include <iostream>
#include <vector>
#include <string>
#include <cassert>
#include <algorithm>
using std::cin;
using std::cout;

int count_empty(std::vector<bool>& v, int p, bool left) {
	int ctr = 0;
	int i;
	if (left)
		i = p-1;
	else
		i = p+1;
	while (i >= 0  && i < v.size() && !v[i]) {
		ctr++;
		if (left)
			i--;
		else
			i++;
	}
	return ctr;
}

int choose_stall(std::vector<bool>& v, int N) {
	assert(N==v.size());
	std::vector<int> Ls(N,-1);
	std::vector<int> Rs(N,-1);
	for (int i = 0; i < N; i++) {
		if (!v[i]) {
			Ls[i] = count_empty(v,i,true);
			Rs[i] = count_empty(v,i,false);
		}
	}
	std::vector<int> minS(N,-1);
	for (int i = 0; i < N; i++) {
		minS[i] = std::min(Ls[i],Rs[i]);
	}
	int max_min_dist = *std::max_element(minS.begin(), minS.end());
	std::vector<int> pass;
	for (int i = 0; i < N; i++) {
		if (minS[i] == max_min_dist) {
			pass.push_back(i);
		}
	}
	if (pass.size() == 1) {
		return pass[0];
	}
	else {
		std::vector<int> maxS;
		for (int i = 0; i < pass.size(); i++) {
			maxS.push_back(std::max(Ls[pass[i]], Rs[pass[i]]));
		}
		int max_max_dist = *std::max_element(maxS.begin(), maxS.end());
		std::vector<int> pass2;
		for (int i = 0; i < maxS.size(); i++) {
			if (maxS[i] == max_max_dist) {
				pass2.push_back(pass[i]);
			}
		}
		std::sort(pass2.begin(),pass2.end());
		return pass2[0];
	}
}

std::string solve(int N, int K) {
	int Smax, Smin;
	std::vector<bool> stall(N,false);
	while (K--) {
		int pos = choose_stall(stall,N);
		assert(!stall[pos]);
		stall[pos] = true;
		int Ls = count_empty(stall,pos,true);
		int Rs = count_empty(stall,pos,false);
		Smax = std::max(Ls,Rs);
		Smin = std::min(Ls,Rs);
	}
	return std::to_string(Smax) + " " + std::to_string(Smin);
}

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int N, K;
		cin >> N >> K;
		cout << "Case #" << t << ": ";
		cout << solve(N,K) << "\n";
	}
	return 0;
}
