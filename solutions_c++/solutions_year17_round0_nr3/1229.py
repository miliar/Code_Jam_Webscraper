#include <bits\stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
int T;

void solvesmall(int testi){
    ll K, N;
    ll minlr, maxlr;
    scanf("%lld%lld",&N,&K);
    priority_queue<ll> Q;
    Q.push(N);
    for(int i=0; i<K; i++){
        ll q = Q.top(); Q.pop();
        //printf("%lld \n",q);
        minlr = (q-1)/2;
        maxlr = q-1-minlr;
        Q.push(minlr);
        Q.push(maxlr);
    }
    printf("Case #%d: %lld %lld\n",testi, maxlr, minlr);
}

struct mp{
    ll first, second;
    bool operator < (const mp& o) const {
        return first < o.first;
    }
};

void solve(int testi){
    ll K, N;
    ll minlr, maxlr;
    scanf("%lld%lld",&N,&K);
    map<ll, ll> Q;
    Q[N] = 1;
    ll cnt = 0;
    while(1){
        auto it = Q.rbegin();
        ll q = it->first;
        ll c = it->second;
        cnt += c;
        minlr = (q-1)/2;
        maxlr = q-1-minlr;
        if (cnt>=K){
            break;
        }
        Q.erase(q);
        Q[minlr] += c;
        Q[maxlr] += c;
    }
    printf("Case #%d: %lld %lld\n",testi, maxlr, minlr);
}

int main(){
	#ifdef LOCAL_PROJECT
		freopen("d:\\src\\CppProjects\\stdin","r",stdin);
		freopen("d:\\src\\CppProjects\\stdout","w",stdout);
	#endif
	scanf("%d",&T);
	for(int testi = 1; testi<=T; testi++){
        solve(testi);
	}
	return 0;
}
