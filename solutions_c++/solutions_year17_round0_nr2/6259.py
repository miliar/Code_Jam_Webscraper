#include<iostream>
#include<string>
#include<cstring>
#include<cmath>
#include<cstdlib>
using namespace std;
typedef long long ll;

bool isTidy(ll n) {
	ll prev = 9;
	while( n > 0 ) {
		ll digit = n % 10;
		if (digit > prev)
			return false;
		prev = digit;
		n = n / 10;
	}
	return true;
}

string numberToString(ll n) {
	string num = "";
	while( n > 0 ) {
		num = (char)(n % 10 + 48) + num;
		n = n / 10;
	}
	return num;
}

void solve(ll number, string ans, ll caseNumber) {
	if (isTidy(number)) {
		//cout<<"came here for final time "<< number << " " << ans <<endl;
		string s1 = numberToString(number);
		cout << "Case #" << caseNumber << ": "<< s1 << ans <<endl;
	} else {
		ans = '9' + ans;
		number = number / 10 - 1;
		solve(number, ans, caseNumber);
	}
}
int main() {
	freopen("/Users/viverma/Downloads/inp.txt", "r", stdin);
	freopen("/Users/viverma/Downloads/out.txt", "w", stdout);
	ll T, N, test;
	string answer;
	cin>>T;
	for (test = 1; test <= T; test++) {
		answer = "";
		cin>>N;
		solve(N, "", test);
	}
	return 0;
}
