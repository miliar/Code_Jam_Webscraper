#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <cmath>

using namespace std;

int f[1500][750][2][2];
int Case, n, m, index[1500];

int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&Case);
	for (int CASE=1; CASE<=Case; CASE++){
		scanf("%d%d",&n,&m);
		memset(index, 0, sizeof(index));
		for (int i=0; i<n; i++){
			int s, t;
			scanf("%d%d",&s,&t);
			for (int j=s; j<t; j++)
				index[j] = 1;
		}
		for (int i=0; i<m; i++){
			int s, t;
			scanf("%d%d",&s,&t);
			for (int j=s; j<t; j++)
				index[j] = 2;
		}
		memset(f, 63, sizeof(f));
		if (index[0] == 0){
			f[0][1][0][1] = 0;
			f[0][0][1][0] = 0;
		} else
		if (index[0] == 1){
			f[0][0][1][0] = 0;
		} else
		if (index[0] == 2){
			f[0][1][0][1] = 0;
		}
		for (int i=1; i<1440; i++)
			for (int j=0; (j<=i+1)&&(j<=720); j++){
				if (index[i] == 0){
					if (j>0){
						f[i][j][0][1] = min(f[i][j][0][1], f[i-1][j-1][0][1]);
						f[i][j][0][1] = min(f[i][j][0][1], f[i-1][j-1][0][0]+1);
					
						f[i][j][1][1] = min(f[i][j][1][1], f[i-1][j-1][1][1]);
						f[i][j][1][1] = min(f[i][j][1][1], f[i-1][j-1][1][0]+1);
					}
					
					if (j<=i){
						f[i][j][0][0] = min(f[i][j][0][0], f[i-1][j][0][0]);
						f[i][j][0][0] = min(f[i][j][0][0], f[i-1][j][0][1]+1);
					
						f[i][j][1][0] = min(f[i][j][1][0], f[i-1][j][1][0]);
						f[i][j][1][0] = min(f[i][j][1][0], f[i-1][j][1][1]+1);
					}
				} else
				if (index[i] == 1){
					if (j<=i){
						f[i][j][0][0] = min(f[i][j][0][0], f[i-1][j][0][0]);
						f[i][j][0][0] = min(f[i][j][0][0], f[i-1][j][0][1]+1);
						f[i][j][1][0] = min(f[i][j][1][0], f[i-1][j][1][0]);
						f[i][j][1][0] = min(f[i][j][1][0], f[i-1][j][1][1]+1);
					}
				}else
				if (index[i] == 2){
					if (j>0){
						f[i][j][0][1] = min(f[i][j][0][1], f[i-1][j-1][0][1]);
						f[i][j][0][1] = min(f[i][j][0][1], f[i-1][j-1][0][0]+1);
						f[i][j][1][1] = min(f[i][j][1][1], f[i-1][j-1][1][1]);
						f[i][j][1][1] = min(f[i][j][1][1], f[i-1][j-1][1][0]+1);
					}
				}
			}
		f[1439][720][0][0]++;
		f[1439][720][1][1]++;
		int ans = 1<<30;
		for (int i=0; i<2; i++)
			for (int j=0; j<2; j++)
				ans = min(ans, f[1439][720][i][j]);
		printf("Case #%d: %d\n",CASE, ans);
	}
	return 0;
}
