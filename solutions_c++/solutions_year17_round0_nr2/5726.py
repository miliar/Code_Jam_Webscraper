#include <bits/stdc++.h>
using namespace std;

#define forn(i,n) for(int i=0;i<int(n);i++)
#define forsn(i,s,n) for(int i=(int)(s);i<(int)(n);i++)
#define dforsn(i,s,n) for(int i=(int)(n-1);i>=int(s);i--)
#define si(a) ((int)(a).size())
#define pb push_back
#define mp make_pair
#define endl '\n'
#define all(c) (c).begin(), (c).end()
#define D(a) cerr << #a << "=" << a << endl;
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef long long int tint;

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	ios_base::sync_with_stdio(false); 
	cin.tie(0);

	int nc;
	cin >> nc;
	
	forn(caso, nc) {
		string s;
		cin >> s;
		
		dforsn(i, 1, si(s)) {
			int a = s[i-1]-'0', b = s[i]-'0';
			
			if (a > b) {
				forsn(j, i, si(s))
					s[j] = '9';
				s[i-1] = s[i-1]-1;
			} 
		}
		
		if (s[0] == '0') s.erase(0, 1);
		
		cout << "Case #" << caso+1 << ": " << s << endl;
	}

	return 0;
}
