#include<bits/stdc++.h>
using namespace std;

int TCs, TC;
int N, P;
int A[10];
int i, x, y, ans;

int Compute(){
	if (P==2) return A[0]+(A[1]+1)/2;
	
	if (P==3){
		ans = A[0];
		ans += min(A[1], A[2]);
		ans += (max(A[1], A[2])-min(A[1], A[2])+2)/3;
		return ans;
	}
	
}

int main(){
	scanf("%d", &TCs);
	for (TC=1; TC<=TCs; TC++){
		printf("Case #%d: ", TC);
		
		memset(A, 0, sizeof(A));
		ans = 0;
		scanf("%d%d", &N, &P);
		for (i=0; i<N; i++){
			scanf("%d", &x);
			A[x%P]++;
		}
		
		printf("%d\n", Compute());
	}
	
	return 0;
}


