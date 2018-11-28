#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
FILE *fin, *fout;
int  N, R, O, Y, G, B, V;
void solve(){
	fscanf(fin, "%d %d %d %d %d %d %d", &N, &R, &O, &Y, &G, &B, &V);
	char s[1001];
	/*if(G>=R || V>=Y || O>=B){
	 	//printf("%d %d %d %d %d %d %d", N, R, O, Y, G, B, V);
		printf("IMPOSSIBLE1\n");
		fprintf(fout, "IMPOSSIBLE\n");
		return;
	}
	R -= G;
	Y -= V; 
	B -= O;
	*/
	if(R>N/2 || Y>N/2 || B>N/2){
	 	//printf("%d %d %d", R, Y, B);
		//printf("IMPOSSIBLE\n");
		fprintf(fout, "IMPOSSIBLE\n");
		return;
	}
	int ll[3];
	int aa[3];
	if(R>B && R >Y){
		ll[0]='R';
		aa[0]=R;
		if(B>Y){
			ll[1]='B';
			aa[1]=B;
			ll[2]='Y';
			aa[2]=Y;
		}else{
			ll[1]='Y';
			aa[1]=Y;
			ll[2]='B';
			aa[2]=B;
		}
	}else if(B>Y && B>R){
		ll[0]='B';
		aa[0]=B;
		if(R>Y){
			ll[1]='R';
			aa[1]=R;
			ll[2]='Y';
			aa[2]=Y;
		}else{
			ll[1]='Y';
			aa[1]=Y;
			ll[2]='R';
			aa[2]=R;
		}
	}else {
		ll[0]='Y';
		aa[0]=Y;
		if(R>B){
			ll[1]='R';
			aa[1]=R;
			ll[2]='B';
			aa[2]=B;
		}else{
			ll[1]='B';
			aa[1]=B;
			ll[2]='R';
			aa[2]=R;
		}
	}
	if(ll[0]==1||ll[1]==1||ll[2]==1) printf("AQUI");
	for(int i = 0; i<1001; i++) s[i] = '\0';
	for(int i = 0; i<N; i++) s[i] = ' ';
	for(int i = 0; i<aa[0]; i++){
		s[2*i] = ll[0];
	}
	for(int i = 0; i<aa[1]; i++){
		if(s[N-1-2*i] != ' ') s[N-1-2*i-1] = ll[1];
		else s[N-1-2*i] = ll[1];
	}
	for(int i = 0; i<N; i++){
		if(s[i]==' '){
			s[i] = ll[2];
		}
	}
	if(strlen(s)!= N) printf("ERROR %d %d\n\n", strlen(s), N);
	//printf("%s\n", s);
	fprintf(fout, "%s\n", s);

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
			solve();
		}
		fclose(fin);
		fclose(fout);
	}
	return 0;
}