#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>
#include <algorithm>
#include <cstdlib>
#include <vector>
#include <cmath>
#include <map>
#include <set>
#include <utility>
#include <sstream>
#include <queue>
#include <unordered_set>
#include <bitset>
using namespace std;

unsigned long long toLong(string str){
	unsigned long long ans = 0;
	for (int i = 0; i < str.length(); i++){
		ans *= 10;
		ans += (str[i] - '0');
	}
	return ans;
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
#endif
	int t;
	cin >> t;
	for (int z = 1; z <= t; z++){
		string str;
		cin >> str;
		//if (str[0] == '0') cerr << " A7A" << endl;
		for (int i = 0; i < str.length(); i++){
			if (i == 0) continue;
			if (str[i] < str[i - 1]){
				str[i - 1]--;
				for (int j = i; j < str.length(); j++){
					str[j] = '9';
				}
				i -= 2;
			}
		}
		cout << "Case #" << z << ": " << toLong(str) << endl;
	}
	
	return 0;
}