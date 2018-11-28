#include<bits/stdc++.h>
using namespace std;
const int N = 111;
const int NONE = -100000;
int f[N][N][N][10], n, p, a[N], b[N];
void update(int &a, int b){
	a = max(a,b);
}
int main(){
	freopen("aa.in","r", stdin);
	freopen("aa.out","w",  stdout);
	int T;
	cin>>T;
	for(int ii = 1; ii <= T; ii++){
		cin>>n>>p;
		int ans = 0;
		b[0] = b[1] = b[2] = b[3] = 0;
		for(int i = 1; i <= n; i++){
			scanf("%d", &a[i]);
			a[i] = a[i] % p;
			b[a[i]]++;
		}
		for(int i = 0; i < N; i++)
			for(int j = 0; j < N; j++)
				for(int k = 0; k < N; k++)
					for(int l = 0; l < p; l++)
						f[i][j][k][l] = NONE;
		f[b[1]][b[2]][b[3]][0] = 0;
		for(int i = b[1]; i >= 0; i--)
			for(int j = b[2]; j >= 0; j--)
				for(int k = b[3]; k >= 0; k--)
					for(int l = 0; l < p; l++)
					if(f[i][j][k][l] != NONE){
						if(i){
							update(f[i - 1][j][k][(l + 1) % p], f[i][j][k][l] + (l == 0));
						}
						if(j){
							update(f[i][j - 1][k][(l + 2) % p], f[i][j][k][l] + (l == 0));
						}
						if(k){
							update(f[i][j][k - 1][(l + 3) % p], f[i][j][k][l] + (l == 0));
						}
						//cout<<i<<' '<<j<<' '<<k<<' '<<l<<' '<<f[i][j][k][l]<<endl;
					}
		for(int l = 0; l < p; l++)
			ans = max(ans, b[0] + f[0][0][0][l]);
		printf("Case #%d: %d\n",ii,ans);
	}
}