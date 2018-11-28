#include <bits/stdc++.h>
using namespace std;

#define rep(i,a,n) for (int i=a;i<n;i++)
#define per(i,a,n) for (int i=n-1;i>=a;i--)
#define pb push_back
#define mp make_pair
#define all(x) (x).begin(),(x).end()
#define fi first
#define se second
#define SZ(x) ((int)(x).size())
typedef vector<int> VI;
typedef long long ll;
typedef pair<int,int> PII;
const ll mod=1000000007;
ll powmod(ll a,ll b) {ll res=1;a%=mod; assert(b>=0); for(;b;b>>=1){if(b&1)res=res*a%mod;a=a*a%mod;}return res;}

vector<pair<int,int> > horses;

int main(){
	int T,N,D,PA,VA;
	
	double V,actT,actS,time,speed;
	
	cin >> T;
	for (int testCase = 1 ; testCase <= T; ++testCase){
		cin >> D >> N;
		horses.clear();
		for (int i = 0; i < N; ++i){
			cin >> PA >> VA;
			horses.push_back(mp(PA,VA));
		}
		
		time = -1;	
		speed = -1;
		
		for (int i = 0; i <horses.size();++i){
			time = max(time,(1.0*D - horses[i].fi)/horses[i].se);
			if (speed == -1) speed = D*1.0/time;
			else speed = min(speed,D*1.0/time);
		}
		
		printf("Case #%d: %.6f\n",testCase,speed);	
	}
	return 0;
}
