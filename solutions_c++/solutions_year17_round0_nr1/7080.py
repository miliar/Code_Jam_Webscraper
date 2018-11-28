#include <iostream>
#include <cstdio>
#include <cmath>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <algorithm>
#include <sstream>
#include <bitset>
#include <cstdlib>
#define sqr(x) (x) * (x)    
#define F first
#define S second                     
#define pb push_back
#define sz(a) int((a).size())
#define mp make_pair
            
using namespace std;
            
typedef long long ll;
typedef vector<int> vi;
typedef vector<long long, long long> vll;
typedef pair<int, int> pii;
typedef pair<long long, long long> pll;
const int oo = (int)1e9 + 1;
const int mod = (int)1e9 + 7;
const int maxn = (int)1e6 + 7;

int t, k, ans;
string s;

       
int main(){
	cin >> t;
	for (int c = 0; c < t; c++){
		cin >> s >> k;
		ans = 0;
		bool ok = 0;
		for (int i = 0; i < sz(s); i++){
			if (s[i] == '+')
				continue;
			if (i + k - 1 >= sz(s)){
				ok = 1;
				break;
			}
			ans++;
				
			for (int j = i; j < i + k; j++)
				if (s[j] == '-')
					s[j] = '+';
				else
					s[j] = '-';	
		}
		cout << "Case #" << c + 1 << ": ";
		if (ok)
			cout << "IMPOSSIBLE\n";
		else
			cout << ans << '\n';
	}
    return 0;
}
