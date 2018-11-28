#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int main() {
	freopen("test.in", "rt", stdin);
	freopen("test.out", "w", stdout);

	int t = 0, case_num = 1;

	string s;

	cin >> t;

	while (case_num <= t) {

		cin >> s;

		int index = 0 ;
		for(int i = 0 ; i < s.size() - 1 ; i ++ ){
			if(s[i] > s[i + 1]){
				s[i] --;
				for(int j = i + 1 ; j < s.size() ; j ++ ){
					s[j] = '9';
				}
				index = i;
				break;
			}
		}


		for(int i = index ; i > 0 ; i -- ){
			if(s[i] < s[i - 1]) {
				s[i] = '9';
				s[i - 1] --;
			}
		}
		long long res = 0;
		stringstream ss(s);
		ss >> res;
		cout << "Case #" << case_num << ": "  << res ;
		cout << endl;
		case_num++;
	}

	return 0;
}
//By : mohamed waleed
