#include <bits/stdc++.h>
using namespace std;



void test() {
	
	int N, P;
	cin >> N >> P;
	
	vector<int> recipe(N);
	for (int i = 0; i < N; ++i)
		cin >> recipe[i];
		
	vector<vector<int>> packages(N, std::vector<int>(P));
	vector<vector<pair<int, int>>> avail(N, vector<pair<int, int>>());
	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < P; ++j) {
			cin >> packages[i][j];
			
			int n0 = ceil(float(packages[i][j])/1.1/recipe[i]);			
			int n1 = floor(float(packages[i][j])/0.9/recipe[i]);
			
		
			//assert(packages[i][j] <= recipe[i]*1.1*n0);
			//assert(packages[i][j] > recipe[i]*1.1*(n0-1));
			
			//assert(packages[i][j] >= recipe[i]*0.9*n1);
			//assert(packages[i][j] < recipe[i]*0.9*(n1+1));
			
			if (n1 >= n0) {
				
				//cerr << "n = [" << n0 << ", " << n1 << "]" << endl;
				avail[i].push_back({n0, n1});
			}
		}
		//cerr << endl;
	}
	
	for (int i = 0; i < N; ++i) {
		sort(avail[i].begin(), avail[i].end());
	}
	
	vector< vector<pair<int, int>>::iterator > its(N);
	for (int i = 0; i < N; ++i) {
		its[i] = avail[i].begin();
	}
	
	int sol = 0;
	while (true) {
		int first_begin = 0;
		int first_end = 0;
		int last_begin = 0;
		
		for (int i = 0; i < N; ++i) {
			if (its[i] == avail[i].end()) {
				cout << sol;
				return;			
			}
			
			if (its[i]->first < its[first_begin]->first)
				first_begin = i;
			if (its[i]->first > its[last_begin]->first)
				last_begin = i;
			if (its[i]->second < its[first_end]->second)
				first_end = i;
		}
		
		if (its[last_begin]->first <= its[first_end]->second) {
			++sol;			
			for (int i = 0; i < N; ++i) {
				//cerr << i <<": [" << its[i]->first << " - " << its[i]->second << "]" << endl;
				++its[i];
			}
		} else {
			++its[first_begin];
		}
	}
}

int main()
{
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		cout << "Case #" << t << ": ";
		test();
		cout << endl;
	}
	return 0;
}
