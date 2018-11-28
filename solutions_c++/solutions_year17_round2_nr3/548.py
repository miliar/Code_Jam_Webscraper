#include <cstdio>
#include <cstring>

int N;
long long E[111], S[111];
long long D[111][111];
int Q;

int T;

bool vst[111];

int u,v;

void update(double &x, double y){
	if (x == -1)
		x = y;
	else
		if (y < x)
			x = y;
}

double used[111];

double dfs(int now, double us){
	double ans = -1;
	if (now == v){
		return 0;
	}
	if (us > used[now])
		return -1;
	used[now] = us;
	for (int i = 0; i < N; i++){
		if (!vst[i]){
			if (D[now][i] != -1){
				vst[i] = true;
				if (E[now] >= D[now][i]){
					double r = dfs(i, us + D[now][i] / (double)S[now]);
					if (r != -1){
						r += D[now][i] / (double)S[now];
						update(ans, r);
					}
				}
				vst[i] = false;
			}
		}
	}
	return ans;
}


void work(){
	scanf("%d%d", &N, &Q);
	for (int i = 0; i < N; i++)  {
		scanf("%lld%lld", E + i, S + i);
		
	}
	for (int i = 0; i < N; i++)
		for (int j = 0; j < N; j++)
			scanf("%lld", &D[i][j]);

	for (int k = 0; k < N; k++)
		for (int i = 0; i < N; i++)
			for (int j = 0; j < N; j++)
				if (D[i][k] != -1 && D[k][j] != -1){
					long long d = D[i][k] + D[k][j];
					if (D[i][j] == -1 || (D[i][j] > d))
						D[i][j] = d;
				}
	if(T==50){
		for (int i = 0; i < N; i++)
			for (int j = 0; j < N; j++)
				if (D[i][j] < -1) {
					fprintf(stderr,"Wrong %d %d\n", i,j);
				}
		for (int i = 0; i < N; i++)
			if (E[i] < 0){
				fprintf(stderr,"Wrong E %d\n", i);
			}
		for (int i = 0; i < N; i++)
			if (S[i] < 0){
				fprintf(stderr,"Wrong E %d\n", i);
			}
	}
	for (int i = 0; i < Q; i++){
		scanf("%d%d", &u, &v);
		for (int j = 0; j < N; j++)
			used[j] = 1e100;
		//fprintf(stderr,"uv=%d %d %d\n", u,v,N);
		fflush(stderr);
		u--;v--;
		memset(vst, 0, sizeof(vst));
		vst[u] = true;
		printf("%f ", dfs(u,0 ));
	}
	puts("");
}

int main(){
	freopen("C.in", "r", stdin);
	int Tcase; scanf("%d", &Tcase);
	FILE *flog = fopen("C.log", "w");
	for (T = 1; T <= Tcase; T++){
		//fprintf(stderr, "%d\n", T);
		fflush(stderr);
		printf("Case #%d: ", T);
		work();
	}
}