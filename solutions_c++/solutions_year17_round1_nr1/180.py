#include <bits/stdc++.h>

#define x first
#define y second

using namespace std;

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
typedef pair<ll,ll> pll;

const int mod=1000000000+7;

int addm(int& a,int b) {return (a+=b)<mod?a:a-=mod;}

template<class T,class U> bool smin(T& a,U b) {return a>b?(a=b,1):0;}
template<class T,class U> bool smax(T& a,U b) {return a<b?(a=b,1):0;}

int T,R,C;
string bd[25];

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	cin >> T;
	for (int cas=1;cas<=T;cas++) {
		cin >> R >> C;
		for (int i=0;i<R;i++) {
			cin >> bd[i];
			char l='?';
			for (int j=0;j<C;j++) {
				if (bd[i][j]!='?') l=bd[i][j];
				bd[i][j]=l;
			}
			l='?';
			for (int j=C-1;j>=0;j--) {
				if (bd[i][j]!='?') l=bd[i][j];
				else bd[i][j]=l;
			}
		}

		for (int j=0;j<C;j++) {
			char l='?';
			for (int i=0;i<R;i++) {
				if (bd[i][j]=='?') bd[i][j]=l;
				else l=bd[i][j];
			}
			l='?';
			for (int i=R-1;i>=0;i--) {
				if (bd[i][j]=='?') bd[i][j]=l;
				else l=bd[i][j];
			}
		}

		cout << "Case #" << cas << ":\n";
		for (int i=0;i<R;i++) cout << bd[i] << '\n';
	}
}
