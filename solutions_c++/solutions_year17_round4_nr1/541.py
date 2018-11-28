#include <bits/stdc++.h>
int n, p, bu[11];
void Main(){
	scanf("%d%d", &n, &p);
	memset(bu, 0, sizeof bu);
	for (int i = 0; i < n; i ++ ){
		int t;
		scanf("%d", &t);
		bu[t % p] ++ ;
	}
	int ans = bu[0];
	for (int i = 1; i < p; i ++ ){
		int j = p - i;
		if (i != j) for (; bu[i] && bu[j]; bu[i] -- , bu[j] -- , ans ++ );
		else for (; bu[i] > 1; bu[i] -= 2, ans ++ );
	}
	//printf("%d %d %d %d %d\n", ans, bu[1], bu[2], bu[3], bu[4]);
	if (p == 4){
		bu[1] += bu[3];
		bu[3] = 0;
		for (; bu[1] > 1 && bu[2]; bu[1] -= 2, bu[2] -- , ans ++ );
		for (; bu[1] > 3; bu[1] -= 4, ans ++ );
	}
	else{
		bu[1] += bu[2];
		bu[2] = 0;
		for (; bu[1] >= p; bu[1] -= p, ans ++ );
	}
	if (bu[1] || bu[2] || bu[3]) ans ++ ;
	printf("%d\n", ans);
}
int main(){
	freopen("t.in","r",stdin);
	freopen("t.out","w",stdout);
	int _;
	scanf("%d", &_);
	for (int i = 1; i <= _; i ++ ){
		printf("Case #%d: ", i);
		Main();
	}
}
