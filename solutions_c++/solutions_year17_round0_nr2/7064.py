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

int t;
ll n, tmp;
string s;

bool check(string k){
	if (sz(k) == 1)
		return 1;
	for (int j = 0; j < sz(k) - 1; j++)
		if (k[j] > k[j + 1])
			return 0;
	return 1;
}
       
int main(){
	cin >> t;
	for (int i = 0; i < t; i++){
		cin >> n;
		
		if (n >= 1 && n < 10){
			cout << "Case #" << i + 1 << ": " << n << '\n';
			continue;
		}		
		s = "";
		tmp = n;
		while (tmp){
			s += char(tmp % 10 + '0');
			tmp /= 10;
		}		
		reverse(s.begin(), s.end());
		while (true){
			for (int j = 0; j < sz(s) - 1; j++){
				if (s[j] > s[j + 1]){
					s[j + 1] = '9';
					s[j] = char(s[j] - '0' - 1 + '0');
					for (int q = j + 1; q < sz(s); q++)
						s[q] = '9';
					break;
				}		
			}
			if (check(s))
				break;
		}
		int pos = 0;
		for (int j = 0; j < sz(s); j++){
			if (s[j] == '0')
				pos++;
			else
				break;
		}
		cout << "Case #" << i + 1 << ": ";
		for (int j = pos; j < sz(s); j++)
			cout << s[j];
		cout << endl;
	}
    return 0;
}
