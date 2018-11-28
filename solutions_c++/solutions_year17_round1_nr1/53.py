#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define fst first
#define snd second
#define fore(i,a,b) for(int i=a,ThxDem=b;i<ThxDem;++i)
using namespace std;
typedef long long ll;

int n,m;
char b[32][32];

int main(){
	int tn;
	scanf("%d",&tn);
	fore(tc,1,tn+1){
		printf("Case #%d:\n",tc);
		scanf("%d%d",&n,&m);
		fore(i,0,n)scanf("%s",b[i]);
		fore(i,0,n){
			int k=-1;
			fore(j,0,m)if(b[i][j]!='?'){k=j;break;}
			if(k<0)continue;
			fore(j,0,m){
				if(b[i][j]=='?')b[i][j]=b[i][k];
				else k=j;
			}
		}
		int k=-1;
		fore(i,0,n)if(b[i][0]!='?'){k=i;break;}
		assert(k>=0);
		fore(i,0,n){
			if(b[i][0]=='?')fore(j,0,m)b[i][j]=b[k][j];
			else k=i;
		}
		fore(i,0,n)puts(b[i]);
	}
	return 0;
}
