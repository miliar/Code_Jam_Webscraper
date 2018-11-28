#define  _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <algorithm>
#include <utility>
#include <functional>
#include <cstring>
#include <queue>
#include <stack>
#include <math.h>
#include <iterator>
#include <vector>
#include <string>
#include <set>
#include <math.h>
#include <iostream> 
#include<map>
#include <iomanip>
#include <time.h>
#include <stdlib.h>
#include <list>
#include <typeinfo>
#include <list>
#include <set>
using namespace std;
#define LONG_INF 10000000000000000
#define MAX_MOD 1000000007
#define REP(i,n) for(long long i = 0;i < n;++i)
int main() {
	int t;
	cin >> t;
	REP(test_case, t) {
		int n;
		cin >> n;
		int r, o, y,g,b, v;
		cin >> r >> o >> y >> g >> b >> v;
		cout << "Case #" << test_case + 1 << ": ";
		string ans;
		if (g != 0) {
			int hogehoge = g;
			for (int i = 0;i < hogehoge;++i) {
				ans += "RG";
				g--;
				r--;
				if (r < 0) {
					cout << "IMPOSSIBLE" << endl;
					goto failed;
				}
			}
			if (r != 0) {
				ans += "R";
				r--;
			}
			else {
				if (r == 0 && g == 0 && y == 0 && o == 0 && v == 0 && b == 0) {

				}
				else {
					cout << "IMPOSSIBLE" << endl;
					goto failed;
				}
			}
		}
		if (v != 0) {
			int hogehoge = v;
			for (int i = 0;i < hogehoge;++i) {
				ans += "YV";
				y--;
				v--;
				if (y < 0) {
					cout << "IMPOSSIBLE" << endl;
					goto failed;
				}
			}
			if (y != 0) {
				ans += "Y";
				y--;
				if (y < 0) {
					cout << "IMPOSSIBLE" << endl;
					goto failed;
				}
			}else{
				if (r == 0 && g == 0 && y == 0 && o == 0 && v == 0 && b == 0) {

				}
				else {
					cout << "IMPOSSIBLE" << endl;
					goto failed;
				}
			}
		}
		if (o != 0) {
			int hogehoge = o;
			for (int i = 0;i < hogehoge;++i) {
				ans += "BO";
				b--;
				o--;
				if (b < 0) {
					cout << "IMPOSSIBLE" << endl;
					goto failed;
				}
			}
			if (b != 0) {
				ans += "B";
				b--;
				if (b < 0) {
					cout << "IMPOSSIBLE" << endl;
					goto failed;
				}
			}
			else {
				if (r == 0 && g == 0 && y == 0 && o == 0 && v == 0 && b == 0) {

				}
				else {
					cout << "IMPOSSIBLE" << endl;
					goto failed;
				}
			}
		}
		while (b > 0 || y > 0 || r > 0) {
			if (ans.length() != 0) {
				if (ans[ans.length() - 1] == 'R') {
					if (y < b) {
						ans.push_back('B');
						b--;
					}
					else if (y > b) {
						y--;
						ans.push_back('Y');
					}
					else {
						if (ans[0] == 'B') {
							b--;
							ans.push_back('B');
						}
						else {
							y--;
							ans.push_back('Y');
						}
					}
				}
				else if (ans[ans.length() - 1] == 'Y') {
					if (r < b) {
						b--;
						ans.push_back('B');
					}
					else if (r > b) {
						r--;
						ans.push_back('R');
					}
					else {
						if (ans[0] == 'B') {
							b--;
							ans.push_back('B');
						}
						else {
							r--;
							ans.push_back('R');
						}
					}
				}
				else {
					if (r < y) {
						y--;
						ans.push_back('Y');
					}
					else if (r > y) {
						r--;
						ans.push_back('R');
					}
					else {
						if (ans[0] == 'Y') {
							y--;
							ans.push_back('Y');
						}
						else {
							r--;
							ans.push_back('R');
						}
					}
				}
			}
			else {
				if (r < b) {
					if (b < y) {
						ans.push_back('Y');
						y--;
					}
					else {
						ans.push_back('B');
						b--;
					}
				}
				else {
					if (r < y) {
						ans.push_back('Y');
						y--;
					}
					else {
						r--;
						ans.push_back('R');
					}
				}
			}
		}
		if (b == 0 && y == 0 && r == 0&&ans[0] != ans[ans.length()-1]) {
			cout << ans << endl;
		}
		else {
			cout << "IMPOSSIBLE" << endl;
		}

	failed			:;
	}
}