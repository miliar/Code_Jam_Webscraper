#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for(int i=(a); i<(b); i++)
#define pb push_back
#define mk make_pair
#define debug(x) cout<<__LINE__<<": "<<#x<<" = "<<x<<endl;
#define all(c) (c).begin(), (c).end()
#define F first
#define S second
#define UNIQUE(c) sort(all(c)); (c).resize(unique(all(c))-c.begin());
#define pi 3.1415926535897932384626433832795028841971

typedef long long ll;
typedef pair<int, int> ii;
const int INF = 0x3f3f3f3f;
const double EPS = 1e-9;

inline int cmp(double x, double y = 0, double tol = EPS){
	return ((x <= y+tol) ? (x+tol < y) ? -1:0:1); }


string int2str(int x){ stringstream ss; string str; ss << x; ss >> str;  return str; }
int str2int(string str){ stringstream ss; int x; ss << str; ss >> x;  return x; }


map<pair<ii, ii>, int> dist;
typedef pair<ii, ii>  battle;

int bfs(int hd, int ad, int hk, int ak, int B, int D)
{
	dist.clear();
	int HEALTH = hd;
	
	queue<battle > q;
	battle s = mk(ii(hd,ad), ii(hk,ak));
	battle tmp;
	
	dist[s] = 0;
	q.push(s);
	while (!q.empty()){
		s = q.front(); q.pop();
		hd = s.F.F;
		ad = s.F.S;
		hk = s.S.F;
		ak = s.S.S;
		
		int atual = dist[s];
		
		int HD, HK, AD, AK;
		
		// ************************ atacar
		HD = hd; AD = ad; HK = hk; AK = ak;
		
		HK -= AD;
		if (HK > 0){
			HD -= AK;
			if (HD > 0){
				tmp = mk(ii(HD,AD), ii(HK,AK));
				if (dist.count(tmp)==0) { dist[tmp] = atual + 1; q.push(tmp); }
			}
		}else if (HK<=0){
			return atual + 1;
		}		
		
		
		// ************************ Buff
		HD = hd; AD = ad; HK = hk; AK = ak;
		AD += B;
		HD -= AK;
		if (HD > 0){
			tmp = mk(ii(HD,AD), ii(HK,AK));
			if (dist.count(tmp)==0) { dist[tmp] = atual + 1; q.push(tmp); }
		}
		
		// Cure
		HD = hd; AD = ad; HK = hk; AK = ak;
		HD = HEALTH;
		HD -= AK;
		if (HD > 0){
			tmp = mk(ii(HD,AD), ii(HK,AK));
			if (dist.count(tmp)==0) { dist[tmp] = atual + 1; q.push(tmp); }
		}
		
		
		// Debuff
		HD = hd; AD = ad; HK = hk; AK = ak;
		AK = max(0, AK-D);
		HD -= AK;
		if (HD > 0){
			tmp = mk(ii(HD,AD), ii(HK,AK));
			if (dist.count(tmp)==0) { dist[tmp] = atual + 1; q.push(tmp); }
		}
		
	}
	return -1;
}

int main(){

	int tn; cin >> tn;
	rep(t,0,tn){
		printf("Case #%d: ", (t+1));
		// code
		
		int hd, ad, hk, ak, b, d;
		cin >> hd >> ad >> hk >> ak >> b >> d;
		int ret = bfs(hd, ad, hk, ak, b, d);
		if (ret == -1) cout << "IMPOSSIBLE\n";
		else cout << ret << "\n";
	}
	return 0;
}









