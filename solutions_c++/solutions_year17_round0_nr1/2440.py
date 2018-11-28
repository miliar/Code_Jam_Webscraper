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

int main(){
	std::ios::sync_with_stdio(false);
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int T, test = 0;
	for(cin >> T; T--; ){
		int k, cnt = 0;
		string str;
		cin >> str >> k;
		for(int i = 0; i + k <= str.length(); i++){
			if(str[i] == '-'){
				cnt++;
				for(int j = 0; j < k; j++)
					str[i + j] = '+' + '-' - str[i + j];
			}
		}
		bool ok = true;
		for(int i = 0; i < str.length(); i++)
			if(str[i] == '-')
				ok = false;
		cout << "Case #" << ++test << ": ";
		if(ok)
			cout << cnt << endl;
		else cout << "IMPOSSIBLE" << endl;
	}
	return 0;
}
