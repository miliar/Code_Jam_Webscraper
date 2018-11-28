#include <bits/stdc++.h>
using namespace std;
int a[5];
const int N = 200;
int a4[][3] = {{4,0,0},{2,1,0},{2,0,2},
	{1,0,1},{0,2,0},{0,1,2},{0,0,4}};

int f4[N][N][N];
int data[233];	
inline void maxx(int &a, int b){
	if (a<b) a = b;
}
void init4() {
	memset(f4,0,sizeof(f4));
	int M = 160;
	for(int i = 0; i < M; i ++)
		for (int j = 0 ;j < M; j++)
			for(int k = 0 ; k < M; k++){
				for (int w = 0 ; w < 7; w ++){
					maxx(f4[ i+a4[w][0] ] [ j+a4[w][1] ][ k+a4[w][2] ], f4[i][j][k]+1);
				}
				maxx(f4[i+1][j][k], f4[i][j][k]);
				maxx(f4[i][j+1][k], f4[i][j][k]);
				maxx(f4[i][j][k+1], f4[i][j][k]);
			}
}

int solve4(int a, int b, int c){
	 return f4[a][b][c] + ((a+2*b+3*c) % 4 != 0);

}

int main(){
	freopen("A-large.in", "r",stdin);
	freopen("A-large.out", "w",stdout);
	init4();
	int T, n, p;
	scanf("%d",&T);
	while (T--){
		static int cas = 1;
		printf("Case #%d: ", cas++);
		scanf("%d%d",&n,&p);
		int s = 0 ;
		if(p==4) {
			int b[4] = {0,0,0,0};
			for (int i = 0 ; i < n; i++) {
				int x;scanf("%d", &x);
				b[x%4]++;
			}
			printf("%d\n", b[0] + solve4(b[1], b[2], b[3]));
		}
		else {
			for(int i=0;i<n;++i) {
				scanf("%d",data+i);
				data[i] %= p;
			}
			
			int ans = 0; 
			if(p==2) {
				int tmp = 0;
				for(int i=0;i<n;++i) {
					if (data[i] == 0) 
						++ans;
					else ++tmp;
				}
				ans += (tmp+1) / 2 ;
			}
			else if(p==3) {
				int one = 0, two = 0;
				for(int i=0;i<n;++i) {
					if(data[i] == 0) 
						++ans;
					else if(data[i] == 1) 
						++one;
					else ++two;
				}
				ans += min(one, two);
				ans += (max(one, two) - min(one, two) +2) / 3 ;
			}
			printf("%d\n", ans);
		}
	}
	fclose(stdout);
	return 0;
}
