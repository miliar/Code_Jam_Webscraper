#include <iostream>
#include <unordered_map>
#include <string>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <map>
#include <set>
#include <algorithm>
#include <limits>
#include <cstring>
#include <unordered_set>
#include <stack>
#include <iostream>
#include <unordered_set>
#include <functional>
using namespace std;

pair<int, int> BathroomStalls(int N, int K){
	multiset<int,greater<int>> s;
	s.insert(N);
	while (K--){
		int Max = *s.begin();
		s.erase(s.begin());
		int left, right;
		if (Max & 1){
			left = (Max - 1) / 2;
			right = (Max - 1) / 2;
		}
		else{
			left = Max / 2;
			right = Max / 2 - 1;
		}
		if (K == 0)return make_pair(left, right);
		s.insert(left);
		s.insert(right);
	}
}

int main(){
	int T;
	cin >> T;
	int j = 1;
	while (T--){
		int N, K;
		cin >> N >> K;
		pair<int, int> p = BathroomStalls(N, K);
		printf("Case #%d: ", j++);
		cout << p.first <<" "<<p.second<< endl;
	}
}