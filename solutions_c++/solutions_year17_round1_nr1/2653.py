#include <bits/stdc++.h>
using namespace std;
int M[50][50];
int  pos[50][2],cnt = 0;
int R = 0,C = 0;
bool judge(int a1,int b1,int a2,int b2) {
	for(int i = a1;i <= a2;++ i) {
		for(int j = b1;j <= b2;++ j) {
			if(M[i][j] != '?') return false;
		}
	}	
	return true;
}
void work(int a1,int b1,int a2,int b2,char ch) {
	for(int i = a1;i <= a2;++ i) {
		for(int j = b1;j <= b2;++ j) {
			M[i][j] = ch;
		}
	}
}
inline void dfs(int a1,int b1,int a2,int b2) {
	//printf("%d %d %d %d\n",a1,b1,a2,b2);
	if(a1 > R || b1 > C || a2 > R || b2 > C) return;
	int lim1 = a1+b1, lim2 = a2+b2;
	int p1 = 0,p2 = 0;
	for(int k = lim1;k <= lim2;++ k) {
		if(p1+p2 != 0) break;
		for(int i = a1;i <= a2;++ i) {
			if(p1+p2 != 0) break;
			for(int j = b1;j <= b2;++ j) {
				if(i+j == k && M[i][j] != '?') {
					p1 = i; p2 = j; break;
				}
			}
		}
	}
	if(p1 + p2 == 0) return;
	//printf("a1 = %d && a2 = %d p1 = %d p2 = %d %c\n",a1,a2,p1,p2,M[p1][p2]);
	for(int i = a1;i <= p1;++ i) {
		for(int j = b1;j <= p2;++ j) {
			//printf("i = %d j = %d\n",i,j);
			M[i][j] = M[p1][p2];
		}
	}
	
	int pos1 = p1,pos2 = p2;
	bool v1 = 0,v2 = 0;
	for(int k = 1;k <= 25;++ k) {
		if(!v1) {
			if(p2+k <= b2 && judge(a1,p2+k,p1,p2+k)) work(a1,p2+k,p1,p2+k,M[p1][p2]),pos2 ++;
			else v1 = 1;
		}		
		if(!v2) {
			if(!v1) {
				if(p1+k <= a2 && p2+k <= b2 &&  judge(p1+k,b1,p1+k,pos2)) {
					work(p1+k,b1,p1+k,pos2,M[p1][p2]) , pos1 ++;
				} else v2 = 1;
			} else {
				if(p1+k <= a2 && judge(p1+k,b1,p1+k,pos2)) {
					work(p1+k,b1,p1+k,pos2,M[p1][p2]) , pos1 ++;
				} else v2 = 1;
			}
		}
		if(v1 && v2) break;
	}
	//printf("pos1 = %d pos2 = %d\n",pos1,pos2);
	dfs(pos1+1,b1,a2,pos2);
	dfs(a1,pos2+1,a2,b2);
	//dfs(pos1+1,pos2+1,a2,b2);
} 
int main() {
	freopen("A-small-attempt6.in","r",stdin);
	freopen("A.out","w",stdout);
	int T = 0;
	scanf("%d",&T);
	for(int t = 1;t <= T;++ t) {
		scanf("%d%d",&R,&C);
		char tmp[50];
		for(int i = 1;i <= R;++ i) {
			scanf("%s",tmp + 1);
			for(int j = 1;j <= C;++ j) {
				M[i][j] = tmp[j];
				pos[++ cnt][0] = i; pos[cnt][1] = j;
			}
		}
		dfs(1,1,R,C);
		printf("Case #%d:\n",t);
		for(int i = 1;i <= R;++ i) {
			for(int j = 1;j <= C;++ j) {
				printf("%c",M[i][j]);
			}
			printf("\n");
		}
	} 
	return 0;
}
