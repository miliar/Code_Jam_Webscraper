#include<stdio.h>
#include<iostream>
#define repn(i,a,b) for(int i=a; i<b; i++)
using namespace std;

int flip ( int A[], int k, int i ) {
	for ( int j=i; j<i+k; j++ ) A[j] *= -1;	
}

int solve ( int A[], int size, int k ) {
	int li = size-k;
	
	int tmp = 0;
	repn(i,0,li) {
		if(A[i]!=1) {
			flip(A, k, i);
			tmp += 1;
		}
	}
	
	bool positive = true;
	for ( int i=li; positive && i<size; i++ ) {
		if ( A[i]==-1 ) positive = false;
	}
	
	if ( positive ) return tmp;
	for ( int i=li; !positive && i<size; i++ ) {
		if ( A[i]==1 ) positive = true;
	}
	
	if ( !positive ) return tmp+1;
	else return -1;
}

int main ( ) {
	freopen("A-large.in", "r", stdin);
	freopen("A-large-output.out", "w", stdout);
	
	int qq; scanf("%d", &qq);
	repn(tt,1,qq+1) {
		string str; cin >> str;
		
		int A[str.size()];
		repn(i,0,str.size()) {
			if(str[i]=='-') A[i] = -1;
			else A[i] = 1;
		}
		
		int size; scanf("%d", &size);
		
		int score = solve(A, str.size(), size);
		printf("Case #%d: ", tt);
		score==-1? printf("IMPOSSIBLE\n") : printf("%d\n", score);
	}
}
