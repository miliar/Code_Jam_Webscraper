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
	ios_base::sync_with_stdio(false); 
	cin.tie(0);

	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int nc;
	cin >> nc;
	
	forn(caso, nc) {
		string s;
		int k;
		cin >> s >> k;
		
		int cnt = 0;
		forn(i, si(s)-k+1)
			if (s[i] == '-') {
				forsn(j, i, i+k)
					s[j] = (s[j] == '-'? '+' : '-');
				cnt++;
			}
		
		bool can = true;
		forn(i, si(s)) if (s[i] == '-') can = false;
			
		cout << "Case #" << caso+1 << ": ";
		
		if (can) cout << cnt << endl;
		else cout << "IMPOSSIBLE" << endl;
	}

	return 0;
}
