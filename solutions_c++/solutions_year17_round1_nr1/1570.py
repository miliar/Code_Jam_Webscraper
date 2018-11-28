#include <bits/stdc++.h>

using namespace std;

#define len(x) ((int)(x).size())
#define pb push_back
#define mp make_pair
#define debug(x) cerr << #x << " is " << x << '\n';
#define bin(x,b) bitset<b> vb(x); cerr << #x << " is " << vb << '\n';

#if ( ( _WIN32 || __WIN32__ ) && __cplusplus < 201103L)
    #define lld "%I64d"
#else
#define lld "%lld"
#endif
#define tmax(a,b,c) max((a),max((b),(c)))
#define cmax(a,b,c,d) max((a),(tmax(a,b,c)))

typedef long long ll;
typedef pair <int,int> pi;

const long double EPS = 1e-10;
const ll MOD = 1e9 + 7;
const ll INF = 1e18;
const long double PI = 3.1415926535897932384626433832795028841;

map <string ,int> ssol; 
void checkAdd(string vs){ if (ssol.find(vs) != ssol.end()){ return; } ssol[vs] = 1; }

bool TST = 0;
ll powmod(ll a,ll b) {ll res=1;a%=MOD;for(;b;b>>=1){if(b&1)res=res*a%MOD;a=a*a%MOD;}return res;}
void Show(int *QQ,int N){ if (not TST){ return; } for (int x = 0;x < N;x++){ cout << QQ[x]; if (x != N-1){ cout << ','; } } cout << '\n'; }
void ShowLL(ll *QQ,int N){ if (not TST){ return; } for (int x = 0;x < N;x++){ cout << QQ[x]; if (x != N-1){ cout << ','; } } cout << '\n'; }


const int maxn = 10e5 + 5;

int main(){
	freopen("input.in","r",stdin);
	freopen("output1A.out","w+",stdout);
	int T; cin >> T;
	int ca = 1;
	while (T--){
		int r,c ; cin >> r >> c;

		char mat[100][100];


		for (int i = 0;i < 100;i++){
			for (int j = 0;j < 100;j++){
				mat[i][j] = 0;
			}
		}
		for (int i = 0;i < r;i++){
			cin >> mat[i];
		}

		
		for (int i = 0;i < r;i++){
			char last = 0;

			for (int j = 0;j < c;j++){
				if (mat[i][j] != '?'){
					last = mat[i][j];
					break;
				}
			}
			if (last){
				for (int j = 0;j < c;j++){
					if (mat[i][j] != '?') last = mat[i][j];
					if (last) mat[i][j] = last;
				
				}
			}else{
				if (i != 0){
					for (int j = 0;j < c;j++){
						mat[i][j] = mat[i-1][j];
					}
				}
			}
		}

		int i = 0;
		while (mat[i][0] == '?'){
			i ++;
		}
		i --;
		while (i >= 0){
			for (int j = 0;j < c;j++){
				mat[i][j] = mat[i+1][j];
			}
			i --;
		}
		
		printf("Case #%d: \n",ca++);
		for (int i = 0;i < r;i++){
			printf("%s\n",mat[i]);
		}
	}
}
