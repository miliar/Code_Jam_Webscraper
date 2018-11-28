/*************************************************************************
 > File Name: B.cpp
 > Author: makeecat
 > Created Time: 2017年04月08日 星期六 11时13分44秒
 ************************************************************************/

#include<cstdio>
#include<algorithm>
#include<cstring>
#include<cmath>
using namespace std;
int T;
long long x;
bool check(long long n){
	int t = n%10;
	n/=10;
	while (n){
		if (n%10>t) return false;
		t = n%10;
		n/=10;
	}
	return true;
}
int a[20];
int main(){
	scanf("%d",&T);
	for (int i=1;i<=T;i++){
		scanf("%lld",&x);
		printf("Case #%d: ",i);
		int cnt = 0;
		while (x){
			a[cnt++] = x%10;
			x/=10;
		}
		if (cnt==1) {printf("%d\n",a[0]);continue;} 
		for (int j=1;j<cnt;j++){
			if (a[j]>a[j-1]) {
				a[j]--;
				for (int k=j-1;k>=0;k--)a[k]=9;
			}
		}
		while (cnt>0 && a[--cnt]==0);
		for (int j=cnt;j>=0;j--) printf("%d",a[j]);
		puts("");
	}
	return 0;
}
