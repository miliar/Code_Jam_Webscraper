#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <set>
#include <cmath>

#define ll long long int
#define pll pair<long long, long long>
#define pii pair<int, int>
#define pb push_back
#define mp make_pair
#define getchar_unlocked getchar
#define F first
#define S second
#define MOD 1000000007

using namespace std;

int main() {
	int testcases;
	cin >> testcases;
	for(int t=1; t<=testcases; t++) {
		string s;
		int k;
		cin >> s >> k;
		cout << "Case #" << t << ": ";
		int count = 0;
		int len = s.size();
		for(int i=0; i<len - k + 1; i++) {
			if(s[i] == '-') {
				for(int j=i; j<i+k; j++) {
					s[j] = ((s[j] == '+')? '-': '+');
				}
				count++;
			}
		}
		bool flag = true;
		for(int i=0; i<len; i++) { 
			if(s[i] == '-') {
				flag = false;
				break;
			}
		}
		if(flag) {
			cout << count << "\n";
		} else {
			cout << " IMPOSSIBLE\n";
		}
	}
	return 0;
}
