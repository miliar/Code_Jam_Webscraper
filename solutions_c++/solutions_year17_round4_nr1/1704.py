#include <bits/stdc++.h>


#define debug(x) cerr<< #x << ": "<< x << endl;
#define print(x) cerr<< x << endl;

#define mp make_pair
#define pb push_back
#define all(x) (x).begin() , (x).end()
#define rall(x) (x).rbegin() , (x).rend()
#define REP(i,x,y) for(int i=x;i<y;i++)
#define REPIT(it,A) for(typeof(A.begin()) it = (A.begin()); it!=A.end();it++)
#define fst first
#define snd second
#define sqr(x) ((x)*(x))

#define fastio ios_base::sync_with_stdio(0);cin.tie(0);
#define ones(x) __builtin_popcountll(x)
using namespace std;

typedef pair<int,int> ii ;
typedef long long ll ;
typedef vector<int> vi;
typedef vector<ii> vii;

const int MAXN = 120;
int n,p;
int g[MAXN];

int main(){
   fastio;
	int T; cin >> T;
	REP(tt,1,T+1){
		cout<<"Case #"<<tt<<": ";
		cin >> n >> p;
		REP(i,0,n) cin >> g[i];
		if(p == 2){
			int even = 0, odd = 0;
			REP(i,0,n) if(g[i] % 2) odd++; else even++;
			int res = even + (odd + 1)/ 2;
			cout<<res<<endl;
			continue;
		}
		if(p == 3){
			int arr[3];
			REP(i,0,3) arr[i] = 0;
			REP(i,0,n) arr[g[i]%3]++;
			int res = arr[0];
			if(arr[1] < arr[2]){
				int val = arr[1] + (arr[2] - arr[1] + 2) / 3;
				res += val;
			}else{
				int val = arr[2] + (arr[1] - arr[2] + 2) / 3;
				res += val;
			}
			cout<<res<<endl;
			continue;

		}

	}

   return 0;
}

