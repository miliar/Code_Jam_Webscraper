#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <queue>
#include <cstring>
#include <string>
#include <sstream>
#include <vector>
#define ffor(_a,_f,_t) for(int _a=(_f),__t=(_t);_a<__t;_a++)
#define all(_v) (_v).begin() , (_v).end()
#define sz size()
#define pb push_back
#define SET(__set, val) memset(__set, val, sizeof(__set))
#define FOR(__i, __n) ffor (__i, 0, __n)
#define syso system("pause")
#define mp make_pair

using namespace std;

int main() {
  freopen("Bl.out","wt", stdout);
  freopen("Bl.in","r", stdin);
  int tests;
  cin >> tests;
  scanf("\n");
  
  FOR (test, tests){
    cout << "Case #" << (test + 1) << ": ";
    string str;
    cin >> str;
    bool putLargest = false;
    string ret = "";
    FOR (i, str.sz) {
    	if (putLargest) {
    		ret = ret + '9';
    		continue;
			}
			for (char dig = '9'; dig >= '0'; dig--) {
				bool possible = true;
				ffor (j, i, str.sz)
					if (dig > str[j]) {
						possible = false;
						break;
					}
					else if (dig < str[j])
						break;
				if (possible) {
					if (dig < str[i])
						putLargest = true;
					if (dig == '0') {
						if (i)
							ret = ret + dig;
					}
					else
						ret = ret + dig;
					break;
				}
			}
		}
		cout << ret;
    cout << "\n";
  }
  return 0;
}
