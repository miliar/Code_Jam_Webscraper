#include<bits/stdc++.h>
#define x first
#define y second
using namespace std;
int t,n;
int R,O,Y,G,B,V;
struct P{
	char c,x;
	int s;
	bool operator<(const P&p)const {
		return s>p.s;
	}
}s[6];
int main(){
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	scanf("%d",&t);
	for(int _=1;_<=t;++_){
		scanf("%d%d%d%d%d%d%d",&n,&R,&O,&Y,&G,&B,&V);
		s[0]={'R','R',R};
		s[1]={'Y','Y',Y};
		s[2]={'B','B',B};
		printf("Case #%d: ",_);
		sort(s,s+3);
		if(s[0].s>n/2){
			printf("IMPOSSIBLE\n");
			continue;
		}
		vector<char> res(n,0);
		int ma=s[0].s;
		for(int i=0;s[0].s--;i+=2){
			res[i]=s[0].c;
		}
		ma=s[1].s-s[2].s;
		for(int i=0,j=0;j<ma;i++){
			if(res[i]==0){
				res[i]=s[1].c;
				++j;
			}
		}
		for(int i=0,flag=0,j=0;j<s[2].s*2;i++){
			if(res[i]==0){
				if(flag)res[i]=s[1].c;
				else res[i]=s[2].c;
				flag^=1;
				++j;
			}
		}
		for(size_t i=0;i<res.size()&&res[i];++i){
			putchar(res[i]);
		}puts("");
	}
	return 0;
}

