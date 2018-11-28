#include<stdio.h>
#include<algorithm>
#include<cmath>
using namespace std;

int N, P; double ing[55], ba[55][55];

void test(int tn){
	scanf("%d%d", &N, &P);
	for(int i=0; i<N; i++)scanf("%lf", &ing[i]);
	for(int i=0; i<N; i++){
		for(int j=0; j<P; j++)scanf("%lf", &ba[i][j]), ba[i][j] /= ing[i];
		sort(ba[i], ba[i]+P);
	}

	int dap=0, idx[55]={0,};
	while(1){
		int lmx = -1, rmi = 1000000000, mix = 0;
		for(int i=0; i<N; i++){
			int lv = int(ceil(ba[i][idx[i]] / 1.1) + 1e-3);
			int rv = int(floor(ba[i][idx[i]] / 0.9) + 1e-3);
			if(lmx < lv)lmx = lv;
			if(rmi > rv)rmi = rv;
			if(ba[i][idx[i]] < ba[mix][idx[mix]]) mix=i;
		}
		if(lmx <= rmi){
			dap++;
			int i;
			for(i=0; i<N; i++){
				idx[i]++;
				if(idx[i] >= P)break;
			}
			if(idx[i] >= P)break;
		}
		else{
			idx[mix]++;
			if(idx[mix] >= P)break;
		}
	}

	printf("Case #%d: %d\n", tn, dap);
}

int main(){
	int i, tn;
	freopen("B-large.in","r",stdin); freopen("output.txt","w",stdout);
	scanf("%d", &tn);
	for(int i=1; i<=tn; i++)test(i);
	return 0;
}
