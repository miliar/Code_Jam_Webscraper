#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <queue>
#include <cassert>
#include <map>
#include <string>
#include <iomanip>
#include <set>
#include <unordered_set>
#include <queue>
#include <unordered_map>
#include <ctime>
#include <vector>
#include <bitset>
#include <list>
#include <stack>
using namespace std;

#define FOR(i, n) for (int i = 0; i < (int)(n); ++i)
#define pb push_back
#define sz(v) (int)(v).size()
#define mp make_pair
#define all(v) (v).begin(), (v).end()
#define for1(i,n) for(int i = 1; i <= (int)(n); ++ i)
#define ford1(i,n) for(int i = (int)(n); i >= 1; -- i)
#define ford(i,n) for(int i = (int)(n)-1; i >= 0; -- i)
#define forn(i,n) for(int i = 0; i < (int)(n); ++ i)
#define debug(x) cerr << #x << " = " << x << endl
typedef vector<int> vi;
typedef vector<pair<int, int> > vpi;
typedef pair<int, int> pii;
typedef long long LL;
typedef long double LD;

int a[ 3 ][ 3 ];

int mi[ 3 ], ma[3];

string ans;

char ch[3] = {'0','1','2'};

bool possible(int Q0,int Q1,int Q2){
	int q[3];
	q[0] = Q0;
	q[1] = Q1;
	q[2] = Q2;
	vector< pair<int,int> > a;
	forn(i,3){
		a.push_back(mp(q[i],i));
	}
	sort(all(a));
	if(a[0].first+a[1].first < a[2].first)
		return false;
	int u[3];
	forn(i,3)
		u[i] = a[i].first;
	string S;
	//cout<<u[0]<<" "<<u[1]<<" "<<u[2]<<endl;
	while(u[2]){
		S+='0'+a[2].second;
		if(u[1]){
			S+='0'+a[1].second;
			-- u[1];
		}
		else{
			S+='0'+a[0].second;;
			--u[0];
		}
		-- u[2];
	}
	//u[0] hat mnac
	ans = "";
	for(int i = 0; i < sz(S); i+=2){
		ans+=S[i];
		ans+=S[i+1];
		if(u[0]){
			ans+='0'+a[0].second;;
			-- u[0];
		}
	}
	return true;
}

char E[ 6 ] = {'R', 'O', 'Y', 'G', 'B','V'};

char pat[ 3 ][ 3 ];
void solve() {
	int n;
	scanf("%d", &n);
	
	scanf("%d", &a[0][0]);
	pat[0][0] = E[0];
	
	scanf("%d", &a[0][1]);
	pat[0][1] = E[1];
	
	scanf("%d", &a[1][1]);
	pat[1][1] = E[2];
	
	scanf("%d", &a[1][2]);
	pat[1][2] = E[3];
	
	scanf("%d", &a[2][2]);
	pat[2][2] = E[4];
	
	scanf("%d", &a[0][2]);
	pat[0][2] = E[5];
	
	
	for(int i = 0; i < 3; ++ i){
		for(int j = i+1; j < 3; ++ j){
			int k = 0^1^2^i^j;
			if(a[k][k]+a[i][j]==n){
				if(a[k][k]!=a[i][j]){
					puts("IMPOSSIBLE");
					return;
				}
				string res;
				forn(iter,a[k][k]){
					res+=pat[k][k];
					res+=pat[i][j];
				}
				printf("%s\n", res.c_str());
				return;
			}
		}
	}
	for(int i = 0; i < 3; ++ i){
		for(int j = i+1; j < 3; ++ j){
			int k = 0^1^2^i^j;
			if(a[i][j] && a[k][k] < a[i][j]+1){
				puts("IMPOSSIBLE");
				return;
			}
		}
	}
	//cout<<"wa"<<endl;
	int Q0, Q1, Q2;
	Q0 = a[0][0]-a[1][2];
	Q1 = a[1][1]-a[0][2];
	Q2 = a[2][2]-a[0][1];
	if(!possible(Q0,Q1,Q2)){
		puts("IMPOSSIBLE");
		return;
	}
	//cout<<ans<<endl;
	bool ok[ 3 ] = {false, false, false};
	string res;
	forn(i,sz(ans)){
		int in = ans[i]-'0';
		if(!ok[in]){
			int j = (in+1)%3, k = (in+2)%3;
			if(j > k)
				swap(j,k);
			if(a[ j ][ k ]){
				forn(iter,a[j][k]){
					res+=pat[in][in];
					res+=pat[j][k];
				}
			}
			ok[in] = true;
		}
		res+=pat[in][in];
	}
	printf("%s\n", res.c_str());
	
	forn(i,sz(res)){
		char ch = res[i];
		char ch2 = res[ (i+1)%sz(res) ];
		int i1, i2;
		forn(u,6)
			if(ch==E[u])
				i1 = u;
		forn(u,6)
			if(ch2==E[u])
				i2 = u;
		if( (i1+1)%6==i2 || (i2+1)%6==i1 || i1==i2){
			assert(false);
		}
	}
}

void testgen() {
    FILE *f = fopen("input.txt", "w");
    // srand(time(0));
    fclose(f);
}

int  main(int argc, char* argv[]) {
#ifdef 	albert96
    // testgen();
    //freopen("input.txt", "r", stdin);
    
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    
    // freopen("output.txt", "w", stdout);
#else
#define task "blackjack"
    // freopen(task".in", "r", stdin);
    // freopen(task".out", "w", stdout);
#endif
	cout<<fixed;
	cout.precision(23);
	
    int T;
    scanf("%d", &T);
    for1(iter,T){
		printf("Case #%d: ", iter);
		solve();
	}

#ifdef albert96
    cerr << "\ntime = " << clock() / (double)CLOCKS_PER_SEC << endl;
#endif
    return 0;
}
