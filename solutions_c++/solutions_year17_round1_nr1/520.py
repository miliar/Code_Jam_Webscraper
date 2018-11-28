#include<stdio.h>
#include<algorithm>
#include<math.h>
#include<string.h>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<time.h>
#include<assert.h>
#include<iostream>
using namespace std;
typedef long long LL;
typedef pair<int,int>pi;
int n,m;
char s[33][33];
bool done[33][33];
int check(int sx,int sy,int ex,int ey){
	int ret=-1;
	for(int ni=sx;ni<=ex;ni++){
		for(int nj=sy;nj<=ey;nj++){
			if(s[ni][nj]!='?'){
				if(ret>=0)return -1;
				ret=s[ni][nj]-'A';
			}
		}
	}
	return ret;
}
int main(){
	freopen("A-large.in.txt","r",stdin);
	freopen("A-large.out.txt","w",stdout);
	int cas=1;
	int _;scanf("%d",&_);
	while(_--){
		scanf("%d%d",&n,&m);
		memset(done,0,sizeof done);
		for(int i=0;i<n;i++)scanf("%s",s[i]);
		for(int i=0;i<n;i++){
			for(int j=0;j<m;j++){
				if(done[i][j])continue;
				pi cs=pi(0,0);
				int cha=0;
				for(int ni=i;ni<n;ni++){
					for(int nj=j;nj<m;nj++){
						int tmp=check(i,j,ni,nj);
						if(tmp>=0){
							cs=pi(ni,nj);
							cha=tmp;
						}
					}
				}
				for(int ni=i;ni<=cs.first;ni++){
					for(int nj=j;nj<=cs.second;nj++){
						s[ni][nj]=cha+'A';
						done[ni][nj]=1;
					}
				}
			}
		}
		printf("Case #%d:\n",cas++);
		for(int i=0;i<n;i++)printf("%s\n",s[i]);
	}
	return 0;
}
