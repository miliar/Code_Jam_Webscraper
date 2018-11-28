#include<bits/stdc++.h>
using namespace std;
struct mypair{
	int high; int low;
};
struct myarr{
	mypair elem[100]; 
};

int T,N,P,req[100],pack[100][100],pt[100],ans;
myarr pac[100];

bool cmp(mypair a, mypair b){
	if (a.low==b.low) return a.high<b.high;
	return a.low<b.low;
}
bool finished(){
	for (int i=0;i<N;i++){
		if (pt[i]>=P) return true;
	}
	return false;
}
int main(){
	freopen("rata.in","r",stdin);
	freopen("rata.out","w",stdout);
	scanf("%d",&T);
	for (int i=1; i<=T;i++){
		scanf("%d%d",&N, &P);
		for (int j=0;j<N;j++) {
			scanf("%d",&req[j]); req[j]*=10;
		}
		for (int j=0;j<N;j++){
			for (int k=0;k<P;k++){
				scanf("%d",&pack[j][k]); pack[j][k]*=10;
			}
		}
		for (int j=0;j<N;j++){
			for (int k=0;k<P;k++){
				pac[j].elem[k].low=pack[j][k]/(req[j]/10*11);
				pac[j].elem[k].high=pack[j][k]/(req[j]/10*9);
				//printf("%d %d, ",pack[j][k], req[j]/10*11);
				if (pack[j][k]%(req[j]/10*11)!=0){
					if (pack[j][k]/(pac[j].elem[k].low+1)<(req[j]/10*9)) {
						pac[j].elem[k].low=0;
						pac[j].elem[k].high=0;
					} else pac[j].elem[k].low++;
				}
				//printf("%d %d, ",pac[j].elem[k].low, pac[j].elem[k].high);
			}
			sort(pac[j].elem,pac[j].elem+P,cmp);
		}
	/*	for (int j=0;j<N;j++){
			for (int k=0;k<P; k++) printf("%d %d, ",pac[j].elem[k].low, pac[j].elem[k].high);
			printf("\n");
		}*/
		
		for (int j=0;j<N;j++) {
			pt[j]=0; while (pac[j].elem[pt[j]].low==0) pt[j]++;	
		}
		ans=0;
		while (!finished()){
			int lo=pac[0].elem[pt[0]].low;
			int hi=pac[0].elem[pt[0]].high;
			for (int j=1;j<N;j++){
				if (pac[j].elem[pt[j]].low>lo) lo=pac[j].elem[pt[j]].low;
				if (pac[j].elem[pt[j]].high<hi) hi=pac[j].elem[pt[j]].high;
			}
			if (lo<=hi){
				ans++;
				for (int j=0;j<N;j++) pt[j]++;
			} else {
				int pointer=0;
				for (int j=1;j<N;j++){
					if (pac[j].elem[pt[j]].high<pac[pointer].elem[pt[pointer]].high) pointer=j;
				}
				pt[pointer]++;
			}
		}
		printf("Case #%d: %d\n",i, ans);
	}
}
