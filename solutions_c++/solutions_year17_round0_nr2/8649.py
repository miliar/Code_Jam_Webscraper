#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <list>
#include <stack>
#include <bitset>
#include <map>
#include <set>
#include <cmath>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <cstring>
using namespace std;

#define rep(i,a) for(int i=0; i<a;i++)
#define repd(i,a) for(int i=a - 1; i>= 0;i--)
#define forn(i,a,b) for(int i=a;i<b;i++)
#define ford(i,a,b) for(int i=a; i>=b; i--)
#define mp make_pair
#define ll long long unsigned
#define sz(x) (x).size()
#define pb push_back
#define endl '\n'
#define vi vector<int>
#define ii pair<int, int>

template <typename T>
  string NumberToString ( T Number ) {
     ostringstream ss;
     ss << Number;
     return ss.str();
  }

ll ex(ll a, ll b) {
	if (b == 0) return 1;
	if (b % 2) return a * ex(a, b - 1);
	ll c = ex(a, b / 2);
	return c * c;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	int t;
	cin >> t;
	rep(tc, t) {
		int n;
		cin >> n;
		
		if (n == 1000) {
			cout << "Case #" << tc + 1 << ": 999" << endl; 
		} else {
			int flag = 1;
			while (flag) {
				int uni = n % 10, dec = (n/10) % 10, cen = (n/100) % 10;
			
				if (uni >= dec && dec >= cen) {
					cout << "Case #" << tc + 1 << ": " << n << endl; 
					flag = 0;
				} else n--;
			}
		}
	}
	
	return 0;
}
