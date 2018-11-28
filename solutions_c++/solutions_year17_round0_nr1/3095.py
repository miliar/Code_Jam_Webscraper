

#include <map>
#include <string>
#include <stdio.h>
#include <vector>
#include <sstream>
#include <stack>
#include <bitset>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <iostream>
#include <algorithm>
#include <limits.h>
#include <float.h>


using namespace std;


void flip(vector<bool>& s, int k, int st){
	int des = st + k - 1;
	if (des < s.size()){
		
		for (int i = st; i <= des; i++){
			s[i] = s[i] ^ 1;
		}
		return;
	}
	return;
}

vector<bool> stob(string& s){
	vector<bool> res;
	for (char& c : s){
		if (c == '+') res.push_back(true);
		else if (c == '-') res.push_back(false);
	}
	return res;
}


int main(){
	int n;
	cin >> n;

	for (int i = 0; i < n; i++){
		string s;
		int k;
		cin >> s >> k;
		vector<bool> b = stob(s);
		int cnt = 0;
		
		bool hasSolution = true;
		for (int j = 0; j < b.size(); j++){

			if (b[j] == false){
				flip(b, k, j);
				cnt++;
			}

			if (b[j] == false) {
				hasSolution = false;
				break;
			}
			
		}

		if (hasSolution)
			printf("Case #%d: %d\n", i+1, cnt);
		else{
			printf("Case #%d: IMPOSSIBLE\n", i + 1);
		}

	}
	
}
