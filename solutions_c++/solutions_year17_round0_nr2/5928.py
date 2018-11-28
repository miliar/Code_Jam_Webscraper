#include <iostream>
#include <sstream>
#include <string>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
#include <cmath>
#include <queue>
#include <set>
using namespace std;

int T;
int RN = 0;
long long N;
string NS;

string toString(long long num) {
	stringstream ss;
	ss << num;
	string str;
	ss >> str;
	return str;
}

bool check(string s)
{
	for(int i=0; i < s.length()-1; i++) {
		if(s[i+1] < s[i])
			return false;
	}
	return true;
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
#ifdef _DEBUG
	freopen("test.in", "r", stdin);
#else
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("out", "w", stdout);
#endif
	cin >> T;
	while(T--) {
		cin >> N;
		while(N) {
			NS = toString(N);
			if(check(NS))
				break;
			N--;
		}
		cout << "Case #" << ++RN << ": " << NS << '\n';

	}
	return 0;
}