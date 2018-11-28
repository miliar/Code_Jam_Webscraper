#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for(int i = (a); i < int(b); ++i)
#define rrep(i, a, b) for(int i = (a) - 1; i >= int(b); --i)
#define trav(it, v) for(typeof((v).begin()) it = (v).begin(); it != (v).end(); ++it)
#define all(v) (v).begin(), (v).end()
#define what_is(x) cerr << #x << " is " << x << endl;
#define sz(x) (int)(x).size()

typedef double fl;
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<pii> vpi;

bool ok(char c1, char c2){
	if((c1 == 'R' || c1 == 'O' || c1 == 'V') &&
	   (c2 == 'R' || c2 == 'O' || c2 == 'V'))
		return false;
	if((c1 == 'Y' || c1 == 'O' || c1 == 'G') &&
	   (c2 == 'Y' || c2 == 'O' || c2 == 'G'))
		return false;
	if((c1 == 'B' || c1 == 'G' || c1 == 'V') &&
	   (c2 == 'B' || c2 == 'G' || c2 == 'V'))
		return false;
	return true;
}

bool bruteforce(int R, int O, int Y, int G, int B, int V){
	vector<char> s;
	rep(i,0,B)s.push_back('B');
	rep(i,0,G)s.push_back('G');
	rep(i,0,O)s.push_back('O');
	rep(i,0,R)s.push_back('R');
	rep(i,0,V)s.push_back('V');
	rep(i,0,Y)s.push_back('Y');
	do{
		bool isOk = true;
		rep(i,0,sz(s)){
			int j=(i+1)%sz(s);
			if(!ok(s[i], s[j]))
				isOk = false;
		}
		if(isOk)
			return true;
	}while(next_permutation(all(s)));
	return false;
}

string ans;
int num[6][6];

struct Entry{
	char start, last;
	int O, G, V, R, Y, B;

	bool operator< (const Entry &other)const{
		if(start != other.start)return start < other.start;
		if(last != other.last)return last < other.last;
		if(O != other.O)return O < other.O;
		if(G != other.G)return G < other.G;
		if(V != other.V)return V < other.V;
		if(R != other.R)return R < other.R;
		if(Y != other.Y)return Y < other.Y;
		if(B != other.B)return B < other.B;
		return false;
	}
};

set<Entry> cache;

bool rec(char start, char last, int O, int G, int V, int R, int Y, int B){
	if(!O && !G && !V && !R && !Y && !B){
		return ok(start, last);
	}
	int totNum = O+G+V+R+Y+B;
	int rs = O+R+V;
	int ys = G+Y+O;
	int bs = V+B+G;
	int maxc = max(max(rs, ys), bs);
	if(maxc > totNum-maxc+1)
		return false;
	Entry entry;
	entry.start = start;
	entry.last = last;
	entry.O = O;
	entry.G = G;
	entry.V = V;
	entry.R = R;
	entry.Y = Y;
	entry.B = B;
	if(cache.count(entry))
		return false;
	char cs[6]={'O','G','V','R','Y','B'};
	rep(i,0,6){
		if(!ok(last, cs[i]))
			continue;
		if(i == 0 && !O)
			continue;
		if(i == 1 && !G)
			continue;
		if(i == 2 && !V)
			continue;
		if(i == 3 && !R)
			continue;
		if(i == 4 && !Y)
			continue;
		if(i == 5 && !B)
			continue;
		/*if(i >= 3 && R+O+Y+G+B+V > 3){
			if(cs[i] == 'R' && ((Y > R && ok(last, 'Y')) || ((B > R) && ok(last, 'B'))))
				continue;
			if(cs[i] == 'Y' && ((B > Y && ok(last, 'B')) || ((R > Y) && ok(last, 'R'))))
				continue;
			if(cs[i] == 'B' && ((R > B && ok(last, 'R')) || ((Y > B) && ok(last, 'Y'))))
				continue;
		}*/
		ans.push_back(cs[i]);
		if(rec(start, cs[i], 
					O-num[i][0],
					G-num[i][1],
					V-num[i][2],
					R-num[i][3],
					Y-num[i][4],
					B-num[i][5])){
			return true;
		}
		ans.pop_back();
		/*if(R+O+Y+G+B+V > 3){
			cache.insert(entry);
			return false;
		}*/
		if(i < 3)
			break;
	}
	cache.insert(entry);
	return false;
}

void solve(){
	rep(i,0,6)
		rep(j,0,6)
			num[i][j]=0;
	rep(i,0,6)
		num[i][i]=1;
	int N, R, O, Y, G, B, V;
	cin >> N >> R >> O >> Y >> G >> B >> V;
	/*for(N=3; N <= 15; ++N){
	R=0;O=0;Y=0;G=0;B=0;V=0;
	for(R=0; R+O+Y+G+B+V <= N; ++R){
	O=0;Y=0;G=0;B=0;V=0;
	for(O=0; R+O+Y+G+B+V <= N; ++O){
	Y=0;G=0;B=0;V=0;
	for(Y=0; R+O+Y+G+B+V <= N; ++Y){
	G=0;B=0;V=0;
	for(G=0; R+O+Y+G+B+V <= N; ++G){
	B=0;V=0;
	for(B=0; R+O+Y+G+B+V <= N || true; ++B){
	V=N-R-O-Y-G-B;
	//R=250;O=0;Y=250;G=0;B=501;V=0;
	R=rand()%200;
	G=rand()%200;
	B=rand()%200;
	Y=rand()%200;
	V=rand()%200;
	O=rand()%200;
	cout << R << " " << O << " " << Y << " " << G << " " << B << " " << V << endl;*/
	ans.clear();
	char cs[6]={'O','G','V','R','G','B'};
	int has[6]={O,G,V,R,Y,B};
	bool solved = false;
	rep(i,0,6){
		if(!has[i])
			continue;
		cache.clear();
		ans.push_back(cs[i]);
		if(rec(cs[i], cs[i], 
					O-num[i][0],
					G-num[i][1],
					V-num[i][2],
					R-num[i][3],
					Y-num[i][4],
					B-num[i][5])){
			cout << ans << endl;
			solved = true;
			break;
		}
		ans.pop_back();
	}
	if(!solved)
		cout << "IMPOSSIBLE" << endl;
	/*if(solved != bruteforce(R, O, Y, G, B, V)){
		cout << R << " " << O << " " << Y << " " << G << " " << B << " " << V << endl;
		assert(0);
	}*/
	//cerr << (bruteforce(R, O, Y, G, B, V) ? "OK" : "IMPOSSIBLE") << endl;
	/*V=0;
	}
	B=0;
	}
	G=0;
	}
	Y=0;
	}
	O=0;
	}
	R=0;
	}*/
}

int main(){
	ios::sync_with_stdio(0);
	int T;
	cin >> T;
	for(int i=1; i <= T; ++i){
		cout << "Case #" << i << ": ";
		solve();
	}
}
