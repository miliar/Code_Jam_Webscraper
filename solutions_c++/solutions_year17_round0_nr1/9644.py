#include<stdio.h>
#include<iostream>
using namespace std;

int flipping ( int A[], int k, int i ) {
	for ( int j=i; j<i+k; j++ ) A[j] *= -1;	
}

int find ( int A[], int size, int k ) {
	int li = size-k;
	
	int xx = 0;
	 for(int hh=0; hh<li; hh++){
		if(A[hh]!=1) {
			flipping(A, k, hh);
			xx += 1;
		}
	}
	
	bool temp = true;
	for ( int i=li; temp && i<size; i++ ) {
		if ( A[i]==-1 ) temp = false;
	}
	
	if ( temp ) return xx;
	for ( int i=li; !temp && i<size; i++ ) {
		if ( A[i]==1 ) temp = true;
	}
	
	if ( !temp ) return xx+1;
	else return -1;
}
int main ( ) {
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("output.out", "w", stdout);
	
	int qq; scanf("%d", &qq);
	for(int tt=1;tt<qq+1; tt++) {
		string str; cin >> str;
		
		int A[str.size()];
		for(int i=0; i<str.size(); i++) {
			if(str[i]=='-') A[i] = -1;
			else A[i] = 1;
		}
		
		int size; scanf("%d", &size);
		
		int final = find(A, str.size(), size);
		printf("Case #%d: ", tt);
		final==-1? printf("IMPOSSIBLE\n") : printf("%d\n", final);
	}
}
