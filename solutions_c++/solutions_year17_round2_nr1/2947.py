using namespace std;
#include <bits/stdc++.h>
#define rep(i,n) for(int i=0; i<(n); i++)
#define mem(x,val) memset((x),(val),sizeof(x));
#define rite(x) freopen(x,"w",stdout);
#define read(x) freopen(x,"r",stdin);
#define all(x) x.begin(),x.end()
#define sz(x) ((int)x.size())
#define sqr(x) ((x)*(x))
#define pb push_back
#define clr clear()
#define inf (1<<30)
#define ins insert
#define xx first
#define yy second
#define eps 1e-9
typedef long long i64;
typedef unsigned long long ui64;
typedef string st;
typedef vector<int> vi;
typedef vector<st> vs;
typedef map<int,int> mii;
typedef map<st,int> msi;
typedef set<int> si;
typedef set<st> ss;
typedef pair<int,int> pii;
typedef vector<pii> vpii;
#define MAX 1005
typedef long double ld;
typedef long long ll;

ld d[MAX], v[MAX];
ld l;
int n;
int main() {
   	ios_base::sync_with_stdio(0);cin.tie(NULL);
   	//Solution
   	int T; cin >> T;
   	for (int t = 0; t < T; ++t)
   	{
	   	
	   	cin >> l >> n;
	   	ld MV = 0;
	   	int mv = 0;
	   	rep(i, n) {
	   		cin >> d[i];	
	   		cin >> v[i];
	   		if((l-d[i])/v[i]> MV){
	   			MV = (l-d[i])/v[i];
	   			mv = i;
	   		}
	   	}
	 	printf("Case #%d: %.6f\n", t+1, (double)(l/MV));  	
   	}
   
   	return 0;
}


//g++-4.9 a.cpp -o a && ./a < a.in > a.out



