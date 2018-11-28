#include<bits/stdc++.h>
using namespace std;

int TCs, TC;
char N[100];
int i, x, L;

int Check(){
	if (N[0]=='0'){
		L--;
		for (i=0; i<L; i++) N[i] = N[i+1];
		N[L] = 0;
	}
	
	for (i=1; i<L; i++) if (N[i]<N[i-1]) break;
	if (i==L) return 1;
	
	N[i-1]--;
	for ( ; i<L; i++) N[i] = '9';
	return 0;
}

int main(){
	scanf("%d", &TCs);
	for (TC=1; TC<=TCs; TC++){
		printf("Case #%d: ", TC);
		scanf("%s", &N);
		L = strlen(N);
		while(!Check());
		
		puts(N);
	}
	
	return 0;
}


