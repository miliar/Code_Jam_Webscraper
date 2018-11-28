#define _CRT_SECURE_NO_WARNINGS
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
int main(){
	freopen("B-small-attempt2.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	std::cin.tie();
	std::ios::sync_with_stdio(false);
	int cases;
	cin >> cases; int t = 1;
	while (cases--){
		bool ch = 0;
		long long x; string ans="";
		cin >> x;
		string s = to_string(x);
		string temp = s;
		cout << "Case #" << t++ << ": ";
		sort(temp.begin(), temp.end());
		if (s == temp){
			cout << s << endl;
			continue;
		}
		
		if (s.size() < 2){
			cout << s << endl;
			continue;
		}

		for (int i = 0; i < s.size(); i++){
			if (s[i] >= s[i + 1] && i + 1 < s.size()){
				s[i]--;
				for (int f = i + 1; f < s.size(); s[f++] = '9');
			}
			long long tmp = stoll(s, NULL, 10);
			if (x > tmp){
				for (int i = 0; i < s.size(); i++){
					if (s[i] != '0'){
						cout << s[i];
					}
				}
				ch = 1;
				break;
			}
		}
		if (!ch)
		for (int i = 0; i < s.size() - 1; i++)
			cout << '9';
		cout << endl;
	}
	return 0;
}