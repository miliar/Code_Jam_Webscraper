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

	int n = 0, k = 0;

	cin >> t;

	while (case_num <= t) {

		cin >> n >> k;

		string s = string(n + 2, '.');

		s[0] = s[n + 1] = 'O';

		int currentL = 0 , currentR = 0;
		int pos = 0;
		for (int i = 0; i < k; i++) {

			int l = -1, r = -1, max = 0;
			currentL = 0 , currentR = 0;

			for (int i = 0; i < n + 2; i++) {
				if (s[i] == 'O') {
					if (l != -1) {
						r = i;
						int dis = r - l - 1;
						if(dis > max){
							max = dis;
							currentL = l , currentR = r;
						}
						l = i;
					} else {
						l = i;
					}
				}
			}
			pos = ( currentR + currentL ) / 2 ;
			s[pos] = 'O';
		}

		cout << "Case #" << case_num << ": " << max(currentR - pos - 1, pos - currentL - 1) << " " << min(currentR - pos - 1, pos - currentL - 1);
		cout << endl;
		case_num++;
	}
	return 0;
}
//By : mohamed waleed
