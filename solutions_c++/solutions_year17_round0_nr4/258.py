#include <bits/stdc++.h>

using namespace std;
//memset
#define MEMSET_INF 127 // about 2B
#define set0(a) memset(a,0,sizeof(a));
#define setminus1(a) memset(a,-1,sizeof(a));
#define setinf(a) memset(a,MEMSET_INF,sizeof(a));

//stl
#define mp make_pair
#define pb push_back
//#define pc(x) putchar_unlocked(x)
//#define gc() getchar_unlocked()

//Loops
#define REP(i,n) for(int i = 0;i < (int)(n); i++)
#define REP1(i,a,b) for(int i = (int)(a);i <= (int)(b); i++)
#define REPMAP(i,mm) for(auto i = mm.begin();i !=mm.end(); i++)

//Sort
#define sortvec(vec) sort(vec.begin(), vec.end())

//Misc
#define LSOne(i) (i & (-i))	// the first Least Significant One-bit in i

//modulo
#define mod %
#define NUM 1000000007


#define LONG_LONG_MAX	9223372036854775807LL
#define LONG_LONG_MIN	(-LONG_LONG_MAX-1)

#define LMAX LONG_LONG_MAX
#define LMIN LONG_LONG_MIN
#define IMAX INT_MAX
#define IMIN INT_MIN
#define PI M_PI
#define EPS 1e-9
#define INF 1e9
#define M_PI		3.14159265358979323846
#define cin(x) scanf("%d",&x)
#define cout(x) printf("$d",x)
#define endl '\n'
#define s(n) scanf("%d",&n)
#define sll(n) scanf("%I64d",&n)
#define p(n) printf("%d",n)
#define pll(n) printf("%I64d",n)
#define all(v) (v).begin(),(v).end()

//typedef
typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef set<int> si;
typedef map<string, int> msi;
typedef map<int, int> mii;
typedef tuple<int,int,int> iii;

#define MAX_N 100005
int initial[105][105];
int ar[105][105];
int vis[105][105];
int getscore(char c){

	int sc = 0;
	if(c == '+')
		sc = 1;
	else if(c == 'x')
		sc = 2;
	else
		sc = 3;
	return sc;
}
char getChar(int x){
	if(x == 1)
		return '+';
	if(x == 2)
		return 'x';
	return 'o';
}
void solve(){
	int n , m;
	cin>>n>>m;
	set0(initial);
	REP( i , m){
		char c;
		int row, col;
		cin>>c>>row>>col;
		row -- , col -- ;
		initial[row][col] += getscore(c);
	}

	map<int,int> xrow , xcol , apdiag ,andiag;
	int total = 0;
	REP( i , n){
		REP( j , n){
			ar[i][j] = initial[i][j];
			if(ar[i][j] & 1){
				apdiag[i+j] = 1;
				andiag[i-j] = 1;
				total++;
			}
			if(ar[i][j] > 1){
				xrow[i] = 1;
				xcol[j] = 1;
				total++;
			}
		}
	}
	int cnt = 0;
	set0(vis);
	int left = n*n;
	int i = 0, j = 0;
	while(left){
		while(vis[i][j] == 0){
			vis[i][j] = 1;
			left --;
			{
				int fg = 0;
				if(xrow[i] == 0 && xcol[j] == 0){
					xrow[i] = 1;
					xcol[j] = 1;
					ar[i][j] += 2;
					total++;
					fg++;
				}
				if(apdiag[i+j] == 0 && andiag[i-j] == 0){
					apdiag[i+j] = 1;
					andiag[i-j] = 1;
					ar[i][j] += 1;
					total++;
					fg++;
				}
				if(fg)
					cnt ++;
			}
			if(j+1 < n && vis[i][j+1] == 0)
				j++;
			else
				break;
		}
		if(!left)
			break;
		i++;
		while(vis[i][j] == 0){
			vis[i][j] = 1;
			left --;
			{
				int fg = 0;
				if(xrow[i] == 0 && xcol[j] == 0){
					xrow[i] = 1;
					xcol[j] = 1;
					ar[i][j] += 2;
					total++;
					fg++;
				}
				if(apdiag[i+j] == 0 && andiag[i-j] == 0){
					apdiag[i+j] = 1;
					andiag[i-j] = 1;
					ar[i][j] += 1;
					total++;
					fg++;
				}
				if(fg)
					cnt ++;
			}
			if(i+1 < n && vis[i+1][j] == 0)
				i++;
			else
				break;
		}
		if(!left)
			break;
		j--;
		while(vis[i][j] == 0){
			vis[i][j] = 1;
			left --;
			{
				int fg = 0;
				if(xrow[i] == 0 && xcol[j] == 0){
					xrow[i] = 1;
					xcol[j] = 1;
					ar[i][j] += 2;
					total++;
					fg++;
				}
				if(apdiag[i+j] == 0 && andiag[i-j] == 0){
					apdiag[i+j] = 1;
					andiag[i-j] = 1;
					ar[i][j] += 1;
					total++;
					fg++;
				}
				if(fg)
					cnt ++;
			}
			if(j > 0  && vis[i][j-1] == 0)
				j--;
			else
				break;
		}
		if(!left)
			break;
		i--;
		while(vis[i][j] == 0){
			vis[i][j] = 1;
			left --;
			{
				int fg = 0;
				if(xrow[i] == 0 && xcol[j] == 0){
					xrow[i] = 1;
					xcol[j] = 1;
					ar[i][j] += 2;
					total++;
					fg++;
				}
				if(apdiag[i+j] == 0 && andiag[i-j] == 0){
					apdiag[i+j] = 1;
					andiag[i-j] = 1;
					ar[i][j] += 1;
					total++;
					fg++;
				}
				if(fg)
					cnt ++;
			}
			if(i > 0 && vis[i-1][j] == 0)
				i--;
			else
				break;
		}

		if(!left)
			break;
		j++;

	}

	cout<<total<<' '<<cnt<<'\n';
	REP( i ,n){
		REP( j , n){
			if(ar[i][j] != initial[i][j]){
				cout<<getChar(ar[i][j])<<' '<<i+1<<' '<<j+1<<'\n';
			}
		}
	}



}

int main(){

	cin.tie(0);
	cout.tie(0);
	cin.sync_with_stdio(0);
	cout.sync_with_stdio(0);
//
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);

	int TC = 1;
	cin>>TC;
	for(int ZZ=1;ZZ<=TC;ZZ++){
		cout<<"Case #"<<ZZ<<": ";
		clock_t start = clock();
//		double ans;
//		cout.precision(10);
//		cout<<fixed<<ans<<endl;
		solve();
		clock_t end = clock();
		cerr <<"Time: " <<(double)(end-start)/CLOCKS_PER_SEC <<" seconds" <<endl;
	}
	return 0;
}
