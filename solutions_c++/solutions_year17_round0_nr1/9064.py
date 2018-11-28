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

int main()
{
	freopen("approximate.in", "r", stdin);
	freopen("approximate.out", "w", stdout);
	ll k, t, count = 0;
	string s;
	char c;
	cin >> t;
	vector<char> pk;
	for(int i=0;i<t;++i){
		cin >> s;
		for(auto elem : s)
			pk.push_back(elem);
		cin >> k;
		for(int j = 0;j <= pk.size()-k;++j){
			if (pk[j] == '-'){
				++count;
				for(int l = 0;l < k;++l)
					if (pk[j+l] == '-')
						pk[j+l] = '+';
					else pk[j + l] = '-';
			} 
		}
		bool fl = 1;
		for(auto elem : pk)
			if (elem == '-')
				fl = 0;
		if (fl){
			cout << "Case #" << i+1 << ": " << count << endl;
			//for(auto elem :pk)
			//	cout << elem;
			//cout << endl;
		}
		else{
			cout << "Case #" << i+1 << ": " << "IMPOSSIBLE" << endl;
			//for(auto elem :pk)
			//	cout << elem;
			//cout << endl;
		}
		count = 0;
		pk.resize(0);
	}
	sp;
}