#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
#include <map>
#define sqr(n) (int)pow(n,2)
#define sp system("pause")
#define ll long long
#define ff first
#define ss second

using namespace std;

bool isvalid(ll n){
	int d = 0, a, b;
	a = n % 10;
	bool fl = 1;
	while(n > 0){
		n /= 10;
		b = n % 10;
		if (a - b < 0)
			fl = 0;
		a = b;
	}
	return fl;
}

int main()
{
	freopen("approximate.in", "r", stdin);
	freopen("approximate.out", "w", stdout);
	ll n, t, count = 0;
	cin >> n;
	for(int i = 0; i < n ; ++i){
		cin >> t;
		while(!isvalid(t))
			--t;
		cout << "Case #" << i + 1 << ": " << t << endl;
	}
	sp;
}