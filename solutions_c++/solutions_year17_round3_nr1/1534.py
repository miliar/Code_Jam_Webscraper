#include <bits\stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
int T;
int N;
int R[10000], H[10000];
const double PI = acos(-1);

map< pair< pair<int,int>, int>, double> cache;
double dp(int i, int K, int prevr){
    if (K==0 || i==N)
        return 0;
    pair< pair<int,int>, int> key = make_pair( make_pair(i,K), prevr);
    if (cache.find(key)!=cache.end())
        return cache[key];
    double sol = max(
               2.0*PI*R[i]*H[i] + PI*R[i]*R[i] - PI*prevr*prevr + dp(i+1,K-1,R[i]),
                dp(i+1,K,prevr)
                );
    cache[key] = sol;
    return sol;
}

double func(int r, int h, int prevr){
    return 2*PI*r*h + PI*r*r - PI*prevr*prevr;
}

void solve(int testi){
    int K;
    scanf("%d%d",&N,&K);
    for(int i=0; i<N; i++){
        scanf("%d%d",R+i,H+i);
        //R[i] = i+1;
        //H[i] = rand()%1000;
    }

    for(int k=0; k<N; k++){
        for(int i=0; i<N-1; i++){
            if (R[i]>R[i+1]){
                swap(R[i],R[i+1]);
                swap(H[i],H[i+1]);
            }
        }
    }

    //double sol = dp(0, K, 0);
    double** DP = new double*[1007];
    for(int i=0; i<=N; i++)
        DP[i] = new double[1007];
    for(int j=1; j<=K; j++){
        if (j==1){
            for(int i=N-1; i>=0; i--){
                DP[i][1] = func(R[i],H[i],0);
            }
        }
        else{
            for(int i=0; i<N; i++){
                for(int k=i+1; k<N; k++){
                    DP[k][j] = max(DP[k][j], func(R[k],H[k],R[i])+DP[i][j-1]);
                }
            }
        }
    }
    double sol = 0;
    for(int i=0; i<N; i++)
        sol = max(sol, DP[i][K]);
    printf("Case #%d: %f\n",testi, sol);
}

int main(){
	#ifdef LOCAL_PROJECT
		freopen("d:\\src\\CppProjects\\stdin","r",stdin);
		freopen("d:\\src\\CppProjects\\stdout","w",stdout);
	#endif
	scanf("%d",&T);
	for(int testi = 1; testi<=T; testi++){
        cerr << testi << endl;
        solve(testi);
	}
	return 0;
}
