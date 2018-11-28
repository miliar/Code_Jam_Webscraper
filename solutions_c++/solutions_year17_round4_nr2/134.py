#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define fst first
#define snd second
#define fore(i,a,b) for(int i=a,ThxDem=b;i<ThxDem;++i)
using namespace std;
typedef long long ll;


int n,c,m;
int qc[1024],qf[1024];

bool can(int k){
	int s=0;
	fore(i,0,n){
		fore(j,0,qf[i]){
			if(s/k>i)return false;
			s++;
		}
	}
	return true;
}

int main(){
	int tn;
	scanf("%d",&tn);
	fore(tc,1,tn+1){
		printf("Case #%d: ",tc);
		scanf("%d%d%d",&n,&c,&m);
		memset(qc,0,sizeof(qc));
		memset(qf,0,sizeof(qf));
		fore(i,0,m){
			int p,b;
			scanf("%d%d",&p,&b);p--;b--;
			qc[b]++;qf[p]++;
		}
		int a=1;
		fore(i,0,c)a=max(a,qc[i]);
		int s=a,e=1024;
		while(e-s>1){
			int m=(s+e)/2;
			if(can(m-1))e=m;
			else s=m;
		}
		int r1=0;
		fore(i,0,n)r1+=max(qf[i]-s,0);
		printf("%d %d\n",s,r1);
	}
	return 0;
}
