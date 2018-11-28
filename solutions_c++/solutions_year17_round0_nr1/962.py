#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for(int i = (a); i < int(b); ++i)
#define rrep(i, a, b) for(int i = (a) - 1; i >= int(b); --i)
#define trav(it, v) for(typeof((v).begin()) it = (v).begin(); it != (v).end(); ++it)
#define all(v) (v).begin(), (v).end()
#define what_is(x) cerr << #x << " is " << x << endl;

typedef double fl;
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<pii> vpi;

char S[1005];

void solve(){
	int K;
	scanf("%s%d", S, &K);
	int N=strlen(S);
	int ans=0;
	rep(i,0,N){
		if(S[i] == '-'){
			if(i+K > N){
				printf("IMPOSSIBLE\n");
				return;
			}
			else{
				rep(j,i,i+K){
					S[j]='-'+'+'-S[j];
				}
				++ans;
			}
		}
	}
	printf("%d\n", ans);
}

int main(){
	int T;
	scanf("%d", &T);
	for(int i=1; i <= T; ++i){
		printf("Case #%d: ", i);
		solve();
	}
}
