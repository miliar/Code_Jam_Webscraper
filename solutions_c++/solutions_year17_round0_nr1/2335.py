#include <string.h>
#include <string>
#include <vector>
#include <deque>
#include <list>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <iterator>
#include <functional>
#include <algorithm>
#include <numeric>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <cmath>
#include <cstdlib>
#include <cstdio>
using namespace std;
#define sz(a)  int((a).size())
#define all(a) a.begin(), a.end()
#define pb push_back
#define mp make_pair
#define CLR(a) memset((a), 0, sizeof(a))
#define INF (1 << 31) - 1
const int dh[8] = {-1, 1, 0, 0,1,1,-1,-1};
const int dw[8] = {0, 0, 1, -1,1,-1,1,-1};
typedef long long ll;
typedef pair<int, int> p;
typedef vector <int> VI;
typedef vector <string> VS;

int main(){

	int tn;
	cin >> tn;
	
	for(int i = 1; i <= tn; i++){
		string str;
		cin >> str;
		int s;
		cin >> s;
				
		int n = sz(str);
		int count = 0;
		for(int stri = 0; stri <= n - s; stri++){
			if(str[stri] == '+') continue;
			count++;
			for(int si = 0; si < s; si++){
				if(str[stri + si] == '-') str[stri + si] = '+';
				else str[stri + si] = '-';
			}
		}

		cout << "Case #" << i << ": ";
		int stri = n-s+1;
		for(stri = n-s+1; stri < n; stri++){
			if(str[stri] == '-'){
				cout << "IMPOSSIBLE" << endl;
				break;	
			} 
		}
		if(stri == n) cout << count << endl;		
	}
	return 0;	
}
