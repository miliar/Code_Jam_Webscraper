/**
*
*			Arif Hosan
*American International University Bangladesh
*		hosan.arif0@gmail.com
*
**/

#include<bits/stdc++.h>
#define PI				2*acos(0.0)
#define endl			'\n'
int caseno = 1;
using namespace std;

#define D(x)			cout << __LINE__ << " " << #x" = " << (x) << endl
#define D2(x,y)			cout << __LINE__ << " " << #x" = " << (x) << ", " << #y" = " << (y) << endl

#define CP()			printf("Case %d: ",caseno++)
#define R()				freopen("read.in","r",stdin)
#define W()				freopen("out.txt","w",stdout)
#define RW				R(); W()

#define SFI(_i)			scanf("%d",&_i)
#define SFL(_i)			scanf("%lld",&_i)
#define SFII(_i,_ii)	scanf("%d%d",&_i,&_ii)
#define SFD(_i)			scanf("%lf",&_i)
#define SFC(_c)			scanf("%c",&_c)

#define PFIL(_i)		printf("%d\n",_i)
#define PFI(_i)			printf("%d",_i)
#define PFSL(_i)		printf("%s\n",_i)
#define PFS(_i)			printf("%s",_i)
#define NL				printf("\n")
#define SPC				printf(" ")

#define ALL(_c)			_c.begin(),_c.end()
#define ITE(_a,_b)		map<_a,_b>::iterator
#define MEM(_c,_v)		memset(_c,_v,sizeof(_c))
#define FOR(i,a,b)		for(i=(a);i<(b);i++)
#define REV(i,a,b)		for(i=(a);i>=(b);i--)
#define valid(nx,ny)	nx>=0 && nx<30 && ny>=0 && ny<30

typedef long long LL;
typedef vector<int> VI;
typedef pair<int, int> PII;
typedef vector< PII > VII;

template<class T> inline T GCD(T a, T b) { if (a<0) return GCD(-a, b); if (b<0)return GCD(a, -b); while (b) { b ^= a ^= b ^= a %= b; } return a; }
template<class T> inline T LCM(T a, T b) { return a / GCD(a, b)*b; }
inline LL POW(const int &n, const int &k) { LL res = 1; int i; FOR(i, 0, k - 1) res *= n; return res; }
inline int BigMod(int a, int p, int M) { int res = 1, x = a; while (p) { if (p & 1) res = ((LL)res * x) % M; x = ((LL)x * x) % M; p >>= 1; }	return res; }

bool isTidy(int N) {
	stringstream ss;
	ss << N;
	string s;
	ss >> s;
	int i;
	FOR(i, 1, s.size()) {
		if (s[i] < s[i - 1]) return false;
	}
	return true;
}

int main() {
	//RW;
	int i, j, N, M, k, xx, x;
	int l, r, T;
	SFI(T);
	while (T--) {
		//string s;
		//cin >> s;
		SFI(N);
		printf("Case #%d: ", caseno++);
		while (N>=1) {
			if (isTidy(N)) {
				cout << N << endl;
				break;
			}
			N--;
		}
		/*if (s.size()== 1) cout << s << endl;
		else {
			FOR(i, 1, s.size()) {
				if (s[i] < s[i - 1]) {
					break;
				}
			}
			if (i == s.size()) cout << s << endl;
			else {
				i--;
				while (i >= 0 && s[i] == '1') i--;
				if (i <0) {
					FOR(j, 0, s.size() - 1) cout << '9';
					NL;
				}
				else {
					FOR(j, 0, i) cout << s[j];
					cout <<(char) (s[i] - 1);
					FOR(j, i+1, s.size()) cout << '9';
					NL;
				}
			}
		}*/
	}
	
    return 0;
}
