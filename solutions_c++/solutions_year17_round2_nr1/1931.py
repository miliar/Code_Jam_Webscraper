#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
FILE *fin, *fout;

long long D, N;
long long K[1000];
long long S[1000];

void solve(){
	fscanf(fin, "%lld %lld", &D, &N);
	for(int i = 0; i<N; i++){
		fscanf(fin, "%lld %lld",&K[i], &S[i]);
	}
	double max = 0;
	for(int i = 0; i<N; i++){
		double t = (double)(D-K[i])/(double)S[i];
		if(t>max) max = t;
	/*	double t = ((double)(K[i]-K[0]))/((double)(S[0]-S[i]));
		if(t*S[0]+K[0] > D) continue;
		else{
			S[0] = S[i];
			K[0] = K[0] + t*S[0]+K[0];
		}
		tt +=t;*/
	}
	fprintf(fout, "%lf\n", (double)D/max);


}

int main(int argc, char *argv[]){
	char kk;
	int total, i;

	fin=fopen(argv[1], "r");
	fout=fopen("out", "w");
	if (fin==NULL || fout == NULL)
	{
		printf("Fitxer out.\n");
	}
	else 
	{
		fscanf(fin, "%d", &total);
		fscanf(fin, "%c", &kk);
		for (i = 0; i<total; i++)
		{
			fprintf(fout, "Case #%d: ", i+1);
			printf("Case #%d: ", i+1);
			solve();
		}
		fclose(fin);
		fclose(fout);
	}
	return 0;
}