//By Ralif Rakhmatullin
#include<iostream>
#include<fstream>
#include<string>
#include<cstring>
#include<math.h>
#include<cassert>
#include<iomanip>
#include<algorithm>
#include<vector>
#include<map>
#include<ctime>
#include<queue>
#include<stack>
#include<set>
#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<bitset>
#include<valarray>
#include<iterator>
#include<list>
#define ll long long
#define ull unsigned long long
#define mp make_pair
#define S second
#define ld long double
#define F first
#define y1 LOL
#define ld long double
#define pb push_back
#define len length
#define sz size
#define beg begin
const ll INF = (ll)1e18 + 123;
const int inf=(int)2e9 + 123; 
const int mod=1e9+7;
using namespace std;
int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	//cout.tie(0);
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	cin >> t;
	for(int cas = 1; cas <= t; cas ++){
		ll x;
		cin >> x;
		string s = "";
		while(x){
			s = char(x % 10 + 48) + s;
			x /= 10;
		}
		bool is = 0;
		string ans = "";
		for(int i = 0; i < s.len() - 1; i ++){
			if(s[i] > s[i + 1]){
				is = 1;
				char x = char((int)s[i] - 1);
				int k = i - 1;
				for(k; s[k] > x; k --)
					x = char((int)s[k] - 1);
				k ++;
				for(int j = 0; j < k; j ++)
					ans += s[j];
				if(k > 0 || s[k] > '1')
					ans += char((int)s[k] - 1);
				for(int j = k + 1; j < s.len(); j ++)
					ans += '9';
				break;
			}
		}
		cout << "Case #" << cas << ": ";
		if(!is)
			cout << s;
		else
			cout << ans;
	   	if(cas < t)
	   		cout << endl;
	}
	return 0;
}  