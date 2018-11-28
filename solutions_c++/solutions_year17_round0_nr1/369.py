#include<bits/stdc++.h>
#define LIM 5555
using namespace std;
string s;
int a[LIM] , k , n;

void solve(int Tc){
	printf("Case #%d: ",Tc);
	int ans = 0;
	cin>>s>>k;
	n = s.size();
	for(int i = 1 ; i <= n ; i++)	a[i] = (s[i - 1] == '+' ? 1 : 0);
	for(int i = 1 ; i <= n - k + 1 ; i++){
		if(a[i] == 1)	continue;
		ans++;
		for(int j = i ; j <= i + k - 1 ; j++)	a[j] ^= 1;
	}
	for(int i = 1 ; i <= n ; i++)
		if(a[i] == 0){
			printf("IMPOSSIBLE\n");
			return ;
		}
	printf("%d\n",ans);
}

int main(){
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int i = 1 ; i <= T ; i++)	solve(i);
	return 0;
}
