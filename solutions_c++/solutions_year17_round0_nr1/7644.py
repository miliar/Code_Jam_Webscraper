#include <stdio.h>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#include <vector>
#include <deque>
#include <stack>
#include <queue>
#include <iterator>
#include <utility>
#include <numeric>
using namespace std;
char stop;
const int CN = 1e4 + 10;


int main(){
	freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
	string str;
	int n, t;

	cin >> t;
	for (int i = 1; i <= t; ++i){
		int number = i, ans = 0;
		cin >> str >> n;

		for (int j = 0; j < str.length(); ++j){

			if (str[j] == '-' && j + n - 1 < str.length()){
				ans++;
				for (int k = j; k < j + n; ++k)
					if (str[k] == '-') str[k] = '+';
					else str[k] = '-';
			}
		}

		for (int j = str.length() - 1; j >= 0; --j){
			if (str[j] == '-') {cout << "Case #" << number << ": " << "IMPOSSIBLE\n"; break;}
			if (!j) {cout << "Case #" << number << ": " << ans << endl;}
		}
	}

//cin >> stop;
return 0;
}