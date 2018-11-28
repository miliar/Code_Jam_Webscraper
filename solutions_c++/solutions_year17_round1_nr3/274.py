#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
typedef unsigned int uint;
typedef unsigned char uchar;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef vector<int> vi;

#define REP(i,x) for(int i=0;i<(int)(x);i++)
#define REPS(i,x) for(int i=1;i<=(int)(x);i++)
#define RREP(i,x) for(int i=((int)(x)-1);i>=0;i--)
#define RREPS(i,x) for(int i=((int)(x));i>0;i--)
#define FOR(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();i++)
#define RFOR(i,c) for(__typeof((c).rbegin())i=(c).rbegin();i!=(c).rend();i++)
#define ALL(container) (container).begin(), (container).end()
#define RALL(container) (container).rbegin(), (container).rend()
#define SZ(container) ((int)container.size())
#define mp(a,b) make_pair(a, b)
#define pb push_back
#define eb emplace_back
#define UNIQUE(v) v.erase( unique(v.begin(), v.end()), v.end() );

template<class T> bool chmax(T &a, const T &b) { if (a<b) { a=b; return 1; } return 0; }
template<class T> bool chmin(T &a, const T &b) { if (a>b) { a=b; return 1; } return 0; }
template<class T> ostream& operator<<(ostream &os, const vector<T> &t) {
os<<"["; FOR(it,t) {if(it!=t.begin()) os<<","; os<<*it;} os<<"]"; return os;
}
template<class T> ostream& operator<<(ostream &os, const set<T> &t) {
os<<"{"; FOR(it,t) {if(it!=t.begin()) os<<","; os<<*it;} os<<"}"; return os;
}
template<class S, class T> ostream& operator<<(ostream &os, const pair<S,T> &t) { return os<<"("<<t.first<<","<<t.second<<")";}
template<class S, class T> pair<S,T> operator+(const pair<S,T> &s, const pair<S,T> &t){ return pair<S,T>(s.first+t.first, s.second+t.second);}
template<class S, class T> pair<S,T> operator-(const pair<S,T> &s, const pair<S,T> &t){ return pair<S,T>(s.first-t.first, s.second-t.second);}

const int INF = 1<<28;
const double EPS = 1e-8;
const int MOD = 1000000007;

int T, Hd, Ad, Hk, Ak, B, D;

int calcAtk(){
	int ans = MOD;
	REP(i, 101){
		ans = min(ans, i + (Hk - 1) / (Ad + B * i) + 1);
	}
	return ans;
}

int calcDef(int atkNum){
	if(atkNum == 1) return 1;
	int ans = MOD;
	REP(i, 101){
		int HP = Hd;
		int Atk = Ak;
		int dres = i;
		int ares = atkNum;
		ans = min(ans, [&](){
			int turn = 0;
			while(1){
				if(dres > 0) {
					if(HP <= Atk - D){
						if(Hd <= 2 * Atk - D) return MOD;
						HP = Hd;
					}else{
						Atk -= D;
						dres --;
					}
				} else {
					if(HP <= Atk){
						if(Hd <= 2 * Atk) return MOD;
						HP = Hd;
					}else{
						ares --;
					}
				}
				HP -= Atk;
				turn ++;
				if(ares == 1){
					return turn + 1;
				}
			}
		}());
	}
	return ans;
}

int main(int argc, char *argv[]){
	ios::sync_with_stdio(false);
	cin >> T;
	REPS(t, T){
		cin >> Hd >> Ad >> Hk >> Ak >> B >> D;
		int atknum = calcAtk();
		int ans = calcDef(atknum);
		if(ans >= MOD) cout << "Case #" << t << ": " << "IMPOSSIBLE" << endl;
		else cout << "Case #" << t << ": " << ans << endl;
	}
	return 0;
}
