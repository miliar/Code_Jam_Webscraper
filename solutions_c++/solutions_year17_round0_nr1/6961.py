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
int rev[1011], a[1011];
int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	//cout.tie(0);
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	cin >> t;
	for(int cas = 1; cas <= t; cas ++){
		string s;
		int k;
		cin >> s >> k;
		memset(rev, 0, sizeof(rev));
		memset(a, 0, sizeof(a));
		bool x = 0;
		int n = s.len();
		for(int i = 0; i < s.len(); i ++){	
			if(s[i] == '+')
				a[i + 1] = 1;
		}
		int cnt = 0;
		bool is = 0;
		for(int i = 1; i <= n; i ++){
			x ^= rev[i];
			a[i] = a[i] ^ x;
			if(a[i] != 1 && i <= n - k + 1){
				x = x ^ 1;
				rev[i + k] = rev[i + k] ^ 1;
				cnt ++;
				a[i] = 1;
			}
			if(a[i] != 1)
				is = 1;
		}
		cout << "Case #" << cas << ": ";
		if(is)
			cout << "IMPOSSIBLE";
		else
			cout << cnt;
		if(cas < t)
			cout << endl;
	}	 
	return 0;
}