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
				
		int n = sz(str);
		for(int stri = n-1; stri > 0; stri--){
			if(str[stri - 1] > str[stri]){
				str[stri-1]--;
				str[stri] = '9';
				for(int j = stri; j < n; j++){
					str[j] = '9';
				}								
			}
		}

		cout << "Case #" << i << ": ";
		for(int stri = 0; stri < n; stri++){
			if(stri == 0 && str[0] == '0') continue;
			cout << str[stri];
		}
		cout << endl;		
	}
	return 0;	
}
