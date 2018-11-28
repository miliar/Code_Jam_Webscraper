#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
using namespace std;
ifstream finS("small_input.txt");
ifstream finL("large_input.txt");
ofstream foutS("small_output.txt");
ofstream foutL("large_output.txt");

pair <int, int> getOddEven(int n) {
	if (n == 0) return { 0, 0 };
	if (n % 2 == 0){
		return { n / 2, n / 2 - 1 };
	}
	return { n / 2, n / 2 };
}

pair<int, int> solve(int n, int k) {
	set<int> bsTree;
	bsTree.insert(n);
	map<int, int> hashMap;
	++hashMap[n];
	pair<int, int> p;
	int cnt = 1;
	while (cnt<=k) { 
		set<int>::iterator maxim = bsTree.end();
		--maxim;
		if (*maxim == 0) return { 0,0 };
		p = getOddEven(*maxim);
		if (hashMap[p.first] == 0) bsTree.insert(p.first);
		if (hashMap[p.second] == 0) bsTree.insert(p.second);
		hashMap[p.first] += hashMap[*maxim];
		hashMap[p.second] += hashMap[*maxim];
		cnt += hashMap[*maxim];
		hashMap[*maxim] = 0;
		bsTree.erase(*maxim);
	}
	return p;
}

int t, ans, k, n;
string str;
int main() {
	finS >> t;
	for (int i = 1; i <= t; ++i) {
		finS >> n >> k;
		pair<int,int> ans = solve(n, k);
		foutS << "Case #" << i << ": " << ans.first << " " << ans.second << "\n";
	}
	/*
	finL >> t;
	for (int i = 1; i <= t; ++i) {
		finL >> n >> k;
		pair<int, int> ans = solve(n, k);
		foutL << "Case #" << i << ": " << ans.first << " " << ans.second << "\n";
	}
	*/
	return 0;
}