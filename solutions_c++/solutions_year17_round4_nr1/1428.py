#include<bits/stdc++.h>

using namespace std;
typedef long long ll;
typedef double db;

const int N = 104;
const int INF = 1000000000;

int a[N];
int b[N][N][N][N];
const int M = 7;
int ch[][4]={
	{1,0,0,0},
	{0,1,0,1},
	{0,0,2,0},
	{0,2,1,0},
	{0,4,0,0},
	{0,0,1,2},
	{0,0,0,4},
};

void update(int &r,int v) {
	if(v>r) r=v;
}

int main(){
	freopen("A-large(1).in","r",stdin);
	freopen("A-large(1).out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int ca=1;ca<=T;ca++) {
		int n,p;
		scanf("%d%d",&n,&p);
		for(int i=1;i<=n;i++) scanf("%d",&a[i]), a[i]%=p;
		int cnt[4] = {0,0,0,0};
		for(int i=1;i<=n;i++) {
			cnt[a[i]] ++;
		}
		int res(0);
		if(p==2) {
			res = cnt[0] + (cnt[1] + 1)/2;
		}else if(p==3) {
			int mi = min(cnt[1], cnt[2]);
			res = cnt[0] + mi;
			for(int i=1;i<=2;i++) 
				res += (cnt[i] - mi + 2)/3;
		}else {
			for(int i=0;i<=cnt[0];i++) 
				for(int j=0;j<=cnt[1];j++) 
					for(int l=0;l<=cnt[2];l++) 
						for(int r=0;r<=cnt[3];r++) 
							b[i][j][l][r] = 0;
			for(int i=0;i<=cnt[0];i++) {
				for(int j=0;j<=cnt[1];j++) {
					for(int l=0;l<=cnt[2];l++) {
						for(int r=0;r<=cnt[3];r++) {
							for(int k=0;k<M;k++) {
								int ii = i+ch[k][0];
								int jj = j+ch[k][1];
								int l1 = l+ch[k][2];
								int r1 = r+ch[k][3];
								if(ii<=cnt[0]&&jj<=cnt[1]&&l1<=cnt[2]&&r1<=cnt[3])
									update(b[ii][jj][l1][r1], b[i][j][l][r]+1);
							}
						}
					}
				}
			}
			for(int i=0;i<=cnt[0];i++) 
				for(int j=0;j<=cnt[1];j++) 
					for(int l=0;l<=cnt[2];l++) 
						for(int r=0;r<=cnt[3];r++) {
							int c(0);
							if(i<cnt[0]||j<cnt[1]||l<cnt[2]||r<cnt[3]) c=1;
							res = max(res, b[i][j][l][r]+c);
						}

		}
		printf("Case #%d: %d\n",ca, res);
	}
	return 0;
}