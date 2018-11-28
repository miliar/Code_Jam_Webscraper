#include<bits/stdc++.h>
#define LIM 1111


using namespace std;

int k[LIM] , s[LIM] , n , D;

double cal(int id){
	long long num = 1ll*D*s[id];
	long long dem = D - k[id];
	return (double) (num) / (double) (dem);
}

void solve(int Tc){
	scanf("%d %d",&D,&n);
	for(int i = 1 ; i <= n ; i++)	scanf("%d %d",&k[i],&s[i]);
	double ans = cal(1);
	for(int i = 2 ; i <= n ; i++)	ans = min(ans , cal(i));
	printf("Case #%d: %.10lf\n",Tc,ans);
}

int main(){
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int i = 1 ; i <= T ; i++)	solve(i);
}

