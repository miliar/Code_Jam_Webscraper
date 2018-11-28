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

int N;
double D;
vector<double> X;
vector<double> V;

double sol(){
	double s = -10;
	for (int i = 0; i < N; i++){
		double ti = (D - X[i])/V[i];
		double saux = D / ti;
		if (s < 0) s = saux;
		else s = min(s, saux);
	}
	return s;
}

int main(){

	int tn; cin >> tn;
	rep(t,0,tn){
		printf("Case #%d: ", (t+1));
		cin >> D >> N;
		X.resize(N);
		V.resize(N);
		rep(i,0,N){
			cin >> X[i] >> V[i];
		}				
		
		printf("%.6lf\n", sol());
	}
	return 0;
}





