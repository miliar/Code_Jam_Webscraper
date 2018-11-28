#include<bits/stdc++.h>

using namespace std;

int a[1009];
char cad[1009];
int k, n;

int solve(){
	int sum, ans=0;
	for(int i=0; i<=n-k; i++){
		sum=0;
		if(a[i]==0){
			ans++;
			for(int j=i; j<i+k; j++){
				a[j]=1-a[j];
			}
		}
	}
	for(int i=0; i<n; i++){
		sum+=a[i];
	}
	if(sum==n)	return ans;
	return -1;
}

int main(){
	int test, ans;
	freopen("a2.in", "r", stdin);
	freopen("a2_out.txt", "w", stdout);
	scanf("%d", &test);
	for(int tt=1; tt<=test; tt++){
		scanf("%s %d", &cad, &k);
		n=strlen(cad);
		for(int i=0; i<n; i++){
			if(cad[i]=='+'){
				a[i]=1;
			}
			else a[i]=0;
		}
		ans=solve();
		printf("Case #%d: ", tt);
		if(ans==-1)	printf("IMPOSSIBLE\n");
		else	printf("%d\n",  ans);
	}
	return 0;
}
