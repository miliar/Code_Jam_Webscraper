#include <bits/stdc++.h>
 
#define gc getchar
#define ii(x) scanf(" %d", &x)
#define ill(x) scanf(" %lld", &x)
#define ll long long
#define pb push_back
#define mp make_pair
#define F first
#define S second
#define all(x) x.begin(),x.end()
#define fill(a,b) memset(a, b, sizeof(a))
#define rep(i,a,b) for(i=a;i<b;i++)
#define per(i,a,b) for(i=a;i>=b;i--)
#define pii pair<int, int>
 
using namespace std;
 
void in(int &x){
    register int c=gc();
    x=0;
    for(;(c<48||c>57);c=gc());
    for(;c>47&&c<58;c=gc()){x=(x<<1)+(x<<3)+c-48;}
}

string s[100];
std::map<char, pair<int, int> > m;
std::vector<pii> v;
bool bad[100];
int val[100];

int main()
{
	int t, i, j, r, c, tt;
	cin >> t; rep(tt, 1, t + 1){
		cin >> r >> c;
		m.clear();
		v.clear();
		rep(i, 0, r){
			bad[i] = false;
			val[i] = 100;
			cin >> s[i];
			int cnt = 0;
			rep(j, 0, c){
				if(s[i][j] != '?') m[s[i][j]] = mp(i, j);
				else cnt++;
			}
			if(cnt == c) bad[i] = true;;
		}
		for(auto it : m){
			char ch = it.F;
			int x = it.S.F, y = it.S.S;
			rep(i, y + 1, c){
				if(s[x][i] == '?') s[x][i] = ch;
				else break;
			}
			per(i, y - 1, 0){
				if(s[x][i] == '?') s[x][i] = ch;
				else break;
			}
		}
		rep(i, 0, r) if(!bad[i]){
			rep(j, 0, r){
				val[j] = min(val[j], abs(i - j));
			}
		}
		rep(i, 0, r) if(bad[i]){
			v.pb(mp(val[i], i));
		}
		sort(all(v));
		for(pii p : v){
			int ind = p.S;
			if(ind == 0){
				s[ind] = s[ind + 1];
			}else if(ind == r - 1){
				s[ind] = s[ind - 1];
			}else{
				if(s[ind - 1][0] != '?') s[ind] = s[ind - 1];
				else s[ind] = s[ind + 1];
			}
		}
		cout << "Case #" << tt << ":" << endl;
		rep(i, 0, r) cout << s[i] << endl;
	}

	return 0;
}