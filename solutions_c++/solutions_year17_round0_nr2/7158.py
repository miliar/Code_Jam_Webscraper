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


int main() {
	freopen("B-large.in", "r", stdin);
	//freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	ios::sync_with_stdio(false); cin.tie(0);
	int cs; cin >> cs;
	rep(cc, cs) {
		string str; cin >> str;
		int base1 = -1, base2 = -1;
		rep2(i, 1, str.size()) if (str[i - 1] > str[i]) {
			base1 = i;
			break;
		}
		if (base1 == -1) {
			cout << "Case #" << cc + 1 << ": " << str << '\n';
			continue;
		}
		base1--;
		for (int i = base1; i >= 0; --i) {
			if (str[i] > str[i + 1]) {
				//str[i] = str[i + 1];
				str[i] = str[i] - 1;
			}
			else {
				base2 = i;
				break;
			}
		}
		if (base2 == -1) 
			base2 = 1;
		else
			base2 += 2;
		rep2(i, base2,str.size()) str[i] = '9';
		string sol = str;
		if (str[0] == '0')
			sol = str.substr(1);
		cout << "Case #" << cc + 1 << ": " << sol << '\n';
	}
	return 0;
}