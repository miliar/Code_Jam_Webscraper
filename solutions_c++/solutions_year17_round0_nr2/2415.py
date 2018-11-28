										/* in the name of Allah */
#include <algorithm>
#include <iostream>
#include <memory.h>
#include <iomanip>
#include <sstream>
#include <fstream>
#include <cstdio>
#include <string>
#include <vector>
#include <queue>
#include <cmath>
#include <list>
#include <map>
#include <set>

using namespace std;

#define uint unsigned int
#define int64 long long
#define P pair<int, int>
#define Pss pair<string, string>
#define PLL pair<int64, int64>
#define Inf 1000000
#define Mod 1000000007LL

bool isOk(string str){
	for(int i = 1; i < str.length(); i++)
		if(str[i] < str[i - 1])
			return false;
	return true;
}

int main(){
	std::ios::sync_with_stdio(false);
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	int T, test = 0;
	for(cin >> T; T--; ){
		string str;
		cin >> str;
		bool ok = isOk(str);
		for(int p = str.length() - 1; !ok && p >= 0; p--){
			if(str[p] != '0'){
				string tmp = str;
				tmp[p]--;
				for(int i = p + 1; i < str.length(); i++)
					tmp[i] = '9';
				if(isOk(tmp)){
					ok = true;
					str = tmp;
				}
			}
		}
		while(str.length() > 1 && str[0] == '0')
			str = str.substr(1);
		cout << "Case #" << ++test << ": " << str << endl;
	}
	return 0;
}
