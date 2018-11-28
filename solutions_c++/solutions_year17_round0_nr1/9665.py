#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <queue>
#include <stack>
#include <deque> 
#include <set>
#include <sstream>
#include <fstream>
#include <cmath>
#include <algorithm>
#include <cstdlib>
#include <cstdio>
#include <ctime>
using namespace std;
#define INF 2000010000

void rev(string &s, int x, int k){
	for (int i = x; i < x + k; ++i){
		if (s[i] == '+'){
			s[i] = '-';
		}
		else{
			s[i] = '+';
		}
	}
}


void rec(string s, int t, int k, map <string, int> &ck, map <string, bool> &ck2){
	if ((!ck2[s]) || (ck2[s] && ck[s] > t)){
		ck[s] = t;
		ck2[s] = true;
 		for (int i = 0; i <= s.size() - k; ++i){
			rev(s, i, k);
			rec(s, t + 1, k, ck, ck2);
			rev(s, i, k);
		}
	}
}

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	cin >> T;
	for (int t = 0; t < T; ++t){
		string s, g = "";
		int k;
		cin >> s >> k;
		for (int i = 0; i < s.size(); ++i){
			g += "+";
		}
		map <string, int> ck;
		map <string, bool> ck2;
		ck[g] = INF;
		rec(s, 0, k, ck, ck2);
		cout << "Case #" << t + 1 << ": ";
		if (ck[g] == INF){
			cout << "IMPOSSIBLE\n";
		}
		else{
			cout << ck[g] << "\n";
		}
	}
	return 0;
}