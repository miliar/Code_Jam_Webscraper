#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define F first
#define S second
#define oioi printf("oioi\n")
#define eoq cout << "eoq" << '\n'
using namespace std;
typedef long long int ll;
typedef unsigned long long int llu;
typedef pair<ll, ll> ii;
typedef pair<double, double> dd;
typedef vector<ll> vi;
typedef vector<ii> vii;
const int dx[] = {0 ,1,-1,0,1,-1,-1, 1};
const int dy[] = {-1,0,0, 1,1, 1,-1,-1};
const ll MOD = 0;
const ll N = 0;

string s;

void flip(int l, int r){
	for (int i = l; i <= r; i++)
	{
		if(s[i]=='+') s[i] = '-';
		else s[i] = '+';
	}
}

bool ok(){
	for (int i = 0; i < s.size(); i++)
	{
		if(s[i]=='-') return false;
	}
	return true;
}

int main () {
	int t, k;
	int caso=1;
	cin >> t;
	while (t--)
	{
		cin >> s >> k;
		int l = 0, r = k-1;
		int ans = 0;
		
		while (r < s.size())
		{
			if(s[l]=='-'){
				flip(l, r);
				ans++;
			}
			
			l++; r++;
		}
		
		if(ok()) cout << "Case #" << caso++ << ": " << ans << "\n";
		else cout << "Case #" << caso++ << ": IMPOSSIBLE\n";
		
	}
	
	
	
	return 0;
}
