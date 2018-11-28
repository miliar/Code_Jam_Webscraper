#include <cstdio>

using namespace std;

int main(){
	int num;
	scanf("%d",&num);
	for(int i=0;i<num;++i){
		int N;
		double dis;
		scanf(" %lf %d",&dis, &N);
		double ki[N];
		double si[N];
		for(int j=0;j<N;++j)
			scanf(" %lf %lf",&ki[j],&si[j]);
		double max = 0, tmp, troad, ans;
		for(int j=0;j<N;++j){
			troad = dis - ki[j];
			tmp = troad / si[j];
			if(tmp > max) max = tmp;
		}
		ans = dis / max;
		printf("Case #%d: %.6lf\n",i+1,ans);
	}
	return 0;
}
