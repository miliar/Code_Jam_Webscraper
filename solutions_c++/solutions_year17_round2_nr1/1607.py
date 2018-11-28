#include <bits\stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
int T;
int K[1007], S[1007];

void solve(int testi){
    int D, N;
    scanf("%d%d",&D,&N);
    for(int i=0; i<N; i++){
        scanf("%d%d",K+i,S+i);
    }
    double time, maxtime = 0;
    for(int i=0; i<N; i++){
        time = (D-K[i])*1.0/S[i];
        maxtime = max(time, maxtime);
    }
    double sol = D*1.0/maxtime;
    printf("Case #%d: %f\n",testi,sol);
}

int main(){
	#ifdef LOCAL_PROJECT
		freopen("d:\\src\\CppProjects\\stdin","r",stdin);
		freopen("d:\\src\\CppProjects\\stdout","w",stdout);
	#endif
	scanf("%d",&T);
	for(int testi = 1; testi<=T; testi++)
        solve(testi);
	return 0;
}
