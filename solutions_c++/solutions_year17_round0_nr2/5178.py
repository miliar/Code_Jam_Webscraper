#include <stdio.h>
#include <iostream>
#include <math.h>
#include <string>
#include <vector>
#include <set>
#include <unordered_set>
#include <map>
#include <unordered_map>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>

#define endl "\n"

using namespace std;

typedef long long ll;
typedef unsigned int uint;
typedef unsigned long long ull;
typedef pair<ll,ll> pll;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

inline int numSize(long long n){
	int cnt = 0;

	while(n != 0){
		cnt++;
		n /= 10;
	}
	return cnt;
}



vector<int> vectorize(long long n){
	vector<int> ret;

	while(n != 0){
		ret.push_back(n % 10);
		n /= 10;
	}

	int l = 0, r = ret.size() - 1, t;

	while(l < r){
		t = ret[l];
		ret[l] = ret[r];
		ret[r] = t;
		l++;
		r--;
	}

	return ret;
}



long long getTidy(long long n){
	vector<int> v = vectorize(n);
	for(int i = 1; i < v.size(); i++){
		if(v[i] < v[i - 1]){
			for(int j = i; j < v.size(); j++) v[j] = 9;
			int sz = numSize(n) - i;
			for(int j = 0; j < sz; j++) n /= 10;
			n--;
			for(int j = 0; j < sz; j++){
				n *= 10;
				n += 9;
			}
			n = getTidy(n);
			break;
		}
	}
	return n;
}

int main(){
	ios::sync_with_stdio(0);

	int T;
	long long n;
	string str;
	cin >> T;
	for(int i = 1; i <= T; i++){
		cout << "Case #" << i << ": ";

		cin >> n;
		
		cout << getTidy(n);

		cout << endl;
//Case #2: 0
//Case #3: IMPOSSIBLE

	}

	
}
