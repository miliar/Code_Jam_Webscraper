#include <cstdio>
#include <queue>
#include <iostream>       
#include <string>
#include <vector>
#include <fstream>        
#include <functional> 
#include <algorithm>  
#include <cstdlib>    
#include <cstring>    
#include <map>        
#include <iomanip>    
#include <limits> 
#include <unordered_map>
#include <set>
#include <cmath>
#include <numeric> //accumulate
#include <stack>
#include <bitset>

//#include <unordered_set>//unordered_set

#define rep(i,a) for (int i = 0; i < (a); ++i)
#define rep2(i,a,b) for (int i = (a); i < (b); ++i)
#define pb push_back
#define mp make_pair
#define all(x) (x).begin(),(x).end()
#define PI 3.14159265359;

using namespace std;
typedef long long ll;
typedef double lf;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<ll, int> pli;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<double> vd;
typedef vector<string> vs;
typedef vector<pair<int, int>> vpii;
typedef vector<vector<int>> vvi;
typedef const vector<int> cvi;
typedef vector<bool> vb;

//const ll INF = 1ull << 62;
const int INF = 987654321;
const int MOD = 1000000007;

string tmp;
bool flip(int begin, int size, bool& fin, int& nxt) {
	if (begin + size > tmp.size()) 
		return false;
	for (int i = begin; i < begin + size; ++i) {
		if (tmp[i] == '+') tmp[i] = '-';
		else tmp[i] = '+';

		if (tmp[i] == '-' && nxt == -1)
			nxt = i;
	}
	if (nxt == -1) {
		

		for (int i = begin + size; i < tmp.size(); ++i) 
			if (tmp[i] == '-') {
				nxt = i;
				break;
			}
	}


	if (nxt == -1)
		fin = true;
	
	return true;
}
int main() {
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	ios::sync_with_stdio(false); cin.tie(0);
	int cs; cin >> cs;
	rep(cc, cs) {
		string str; cin >> str;
		tmp = str;
		int k; cin >> k;
		int here = 0;
		bool ok;
		int sol = 0;
		if (tmp == string(tmp.size(), '+'))
			ok = true;
		else {
			here = tmp.find('-');// -tmp.begin();
			while (true) {
				sol++;
				bool fin = false;
				int nxt = -1;
				ok = flip(here, k, fin, nxt);
				if (ok == false) {
					break;
				}
				if (fin) break;
				here = nxt;
			}
		}
		if (ok)
			cout << "Case #" << cc + 1 << ": " << sol << '\n';
		else
			cout << "Case #" << cc + 1 << ": " << "IMPOSSIBLE" << '\n';
	}
	return 0;
}