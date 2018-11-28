#include<bits/stdc++.h>
#define N 111
using namespace std;

int f[N][N][5] , g[N][N][N][5] , c[5] , n , p;
void maximize(int &a,int b){
	if(a < b)	a = b;
}

int solve2(){
	return n - c[1] / 2;
}

int solve3(){
	for(int i = 0 ; i <= n ; i++)
		for(int n1 = 0 ; n1 <= c[1] ; n1++)
			for(int s = 0 ; s < 3 ; s++)
				f[i][n1][s] = -1e9;
	f[c[0]][0][0] = c[0] + (c[0] != n);
	for(int i = c[0] ; i < n ; i++)
		for(int n1 = 0 ; n1 <= c[1] ; n1++)
			for(int s = 0 ; s < 3 ; s++){
			if(f[i][n1][s] == -1e9)	continue;
			int n2 = i - c[0] - n1;
			int ns , add;
			/*chon 1*/
			if(n1 < c[1]){
				int add = 0;
				ns = (s + 1)%3;
				if(ns == 0 && (i + 1) != n)	add = 1;
				maximize(f[i + 1][n1 + 1][ns] , f[i][n1][s] + add);
			}
			/*chon 2*/
			if(n2 < c[2]){
				int add = 0;
				ns = (s + 2)%3;
				if(ns == 0 && (i + 1) != n)	add = 1;
				maximize(f[i + 1][n1][ns] , f[i][n1][s] + add);
			}
		}
	return f[n][c[1]][(c[1] + 2*c[2])%3];
}

int solve4(){
	for(int i = 0 ; i <= n ; i++)
		for(int n1 = 0 ; n1 <= c[1] ; n1++)
			for(int n2 = 0 ; n2 <= c[2] ; n2++)
				for(int s = 0 ; s < 4 ; s++)
					g[i][n1][n2][s] = -1e9;
	g[c[0]][0][0][0] = c[0] + (c[0] != n);
	for(int i = c[0] ; i < n ; i++)
		for(int n1 = 0 ; n1 <= c[1] ; n1++)
			for(int n2 = 0 ; n2 <= c[2] ; n2++)
				for(int s = 0 ; s < 4 ; s++){
					if(g[i][n1][n2][s] == -1e9)	continue;
					int n3 = i - n1 - n2 - c[0];
					int ns;
					/*chon 1*/
					if(n1 < c[1]){
						int add = 0;
						ns = (s + 1)%4;
						if(ns == 0 && (i + 1) != n)	add = 1;
						maximize(g[i + 1][n1 + 1][n2][ns] , g[i][n1][n2][s] + add);
					}
					/*chon 2*/
					if(n2 < c[2]){
						int add = 0;
						ns = (s + 2)%4;
						if(ns == 0 && (i + 1) != n)	add = 1;
						maximize(g[i + 1][n1][n2 + 1][ns] , g[i][n1][n2][s] + add);
					}
					/*chon 3*/
					if(n3 < c[3]){
						int add = 0;
						ns = (s + 3)%4;
						if(ns == 0 && (i + 1) != n)	add = 1;
						maximize(g[i + 1][n1][n2][ns] , g[i][n1][n2][s] + add);
					}
				}
	return g[n][c[1]][c[2]][(c[1] + 2*c[2] + 3*c[3])%4];
}

void solve(int Tc){
	scanf("%d %d",&n,&p);
	memset(c , 0 , sizeof c);
	for(int i = 1 ; i <= n ; i++){
		int x;
		scanf("%d",&x);
		c[x%p]++;
	}
	printf("Case #%d: ",Tc);
	if(p == 2)	printf("%d\n",solve2());
	else if(p == 3)	printf("%d\n",solve3());
	else printf("%d\n",solve4());
}

int main(){
	freopen("A-l.inp","r",stdin);	
	freopen("A-l.out","w",stdout);
	int Tc;
	scanf("%d",&Tc);
	for(int i = 1 ; i <= Tc ; i++)	solve(i);
}

