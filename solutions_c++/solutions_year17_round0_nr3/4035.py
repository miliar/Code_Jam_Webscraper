#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
typedef vector<ii> vii;

#define INF LONG_LONG_MAX
#define loop(i,a,b) for(ll i=(ll)a;i<=(ll)b;i++)
#define mem(a, v) memset(a, v, sizeof a)
#define pb push_back
#define mp make_pair
#define MAXN 1000009
#define MOD 1000000007
#define MAX(a,b) (((a)>(b))?(a):(b))
#define MIN(a,b) (((a)<(b))?(a):(b))
#define left(x) x<<1
#define right(x) (x<<1)|1
#define PI acos(-1.0)
#define EPS 1e-9

int T, t;
int N, K;

bool comp(ii a, ii b){
	if(a.first==b.first) return a.second > b.second;
	return a.first < b.first;
}

void solve(){
	cin>>N>>K;
	priority_queue< ii, vii, decltype(&comp) > pq(&comp);
	pq.push(ii(N,1));
	loop(i,1,K){
		ii u=pq.top();
		int d=u.first, idx=u.second, place;
		pq.pop();

		place=(idx+idx+d-1)/2;
		
		pq.push(ii(place-idx, idx));
		pq.push(ii(idx+d-place-1, place+1));
		
		if(i==K)
			cout<<"Case #"<<++t<<": "<<MAX(place-idx, idx+d-place-1)<<" "<<MIN(place-idx, idx+d-place-1)<<endl;
	}
}

int main(){
    ios_base::sync_with_stdio(false);
  	freopen("C-small-2-attempt0.in","r",stdin);
    freopen("output.out","w",stdout);  
    cin>>T;
    while(T--){
    	solve();
    }
    return 0;
}
