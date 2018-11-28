#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define mp make_pair
#define sz(x) (int)(x).size()
#define all(x) (x).begin(),(x).end()
#define pb push_back
#define ii pair<int,int>
#define INF 1000000100
#define INFLL 3000000000000000010ll
#define UQ(x) (x).resize(distance((x).begin(),unique(all((x)))))
#define mid(x,y) (((x)+(y))>>1)
int n,p;
namespace p2 {
	int c[2];
	void work(int kk) {
		int x;
		memset(c,0,sizeof(c));
		for (int i=0;i<n;i++) {
			scanf("%d",&x);
			c[x%2]++;
		}
		printf("Case #%d: %d\n", kk,c[0]+(c[1]+1)/2);
	}
};
namespace p3 {
	int mem[105][105][3];
	int rec(int i,int j,int c) {
		if (i<0 || j<0) return -INF;
		if (i==0 && j==0) {
			return 0;
		}
		if (mem[i][j][c]!=-1) return mem[i][j][c];
		int m=0;
		if (c==0) {
			m=max(m,rec(i-1,j,(c+1)%3)+1);
			m=max(m,rec(i,j-1,(c+2)%3)+1);
		} else {
			m=max(m,rec(i-1,j,(c+1)%3));
			m=max(m,rec(i,j-1,(c+2)%3));
		}
		return mem[i][j][c]=m;
	}
	int c[3];
	void work(int kk) {
		int x;
		memset(mem,-1,sizeof(mem));
		memset(c,0,sizeof(c));
		for (int i=0;i<n;i++) {
			scanf("%d",&x);
			c[x%3]++;
		}
		printf("Case #%d: %d\n", kk,c[0]+rec(c[1],c[2],0));
	}
};
namespace p4 {
	int mem[105][105][3];
	int rec(int i,int j,int c) {
		if (i==0 && j==0) {
			return 0;
		}
		if (i<0 || j<0) return -INF;
		if (mem[i][j][c]!=-1) return mem[i][j][c];
		int m=0;
		if (c==0) {
			m=max(m,rec(i-1,j,(c+1)%3)+1);
			m=max(m,rec(i,j-1,(c+2)%3)+1);
		} else {
			m=max(m,rec(i-1,j,(c+1)%3));
			m=max(m,rec(i,j-1,(c+2)%3));
		}
		return mem[i][j][c]=m;
	}
	int c[3];
	void work(int kk) {
		/*
		int x;
		memset(mem,-1,sizeof(mem));
		for (int i=0;i<n;i++) {
			scanf("%d",&x);
			c[x%2]++;
		}
		printf("Case #%d: %d\n", kk,c[0]+rec(c[1],c[2],0));*/
	}
};
int main() {
	int tc;
	scanf("%d",&tc);
	for (int kk=1;kk<=tc;kk++) {
		scanf("%d%d",&n,&p);
		if (p==2) p2::work(kk);
		else if (p==3) p3::work(kk);
		else if (p==4) p4::work(kk);
		else assert(0);
	}
}