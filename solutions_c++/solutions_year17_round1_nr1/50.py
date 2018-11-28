#include<stdio.h>
#include<string.h>

int N, M; char mp[33][33];

void test(int tn){
	scanf("%d%d\n", &N, &M);
	for(int i=0; i<N; i++){
		gets(mp[i]);
		char chr=0;
		for(int j=0; j<M; j++){
			if(mp[i][j] != '?')chr = mp[i][j];
			if(chr)mp[i][j] = chr;
		}
		chr=0;
		for(int j=M-1; j>=0; j--){
			if(mp[i][j] != '?')chr = mp[i][j];
			if(chr)mp[i][j] = chr;
		}
	}
	bool fl=1;
	for(int i=0; i<N; i++){
		if(mp[i][0] != '?')fl=0;
		else if(!fl)strcpy(mp[i], mp[i-1]);
	}
	fl=1;
	for(int i=N-1; i>=0; i--){
		if(mp[i][0] != '?')fl=0;
		else if(!fl)strcpy(mp[i], mp[i+1]);
	}
	printf("Case #%d:\n", tn);
	for(int i=0; i<N; i++)puts(mp[i]);
}

int main(){
	int i, tn;
	freopen("A-large.in","r",stdin); freopen("output.txt","w",stdout);
	scanf("%d", &tn);
	for(int i=1; i<=tn; i++)test(i);
	return 0;
}
