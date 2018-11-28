#include <iostream>
#include <cstdio>
#include <cstring>
#define maxn 1009
using namespace std;
int n;
int a[100];
bool check(int n){
	int tot = 0;
	while(n){
		a[tot++] = n % 10;
		n /= 10;
	}
	for(int i = tot - 1; i > 0; i--){
		if(a[i] > a[i - 1])
			return 0;
	}
	return 1;
}
int main(){
	freopen("D:\\a.in","r",stdin);
    freopen("D:\\a.out","w",stdout); 
	int tt, cot = 1;
	scanf("%d", &tt);
	while(tt--){
		scanf("%d", &n);
		int ans = 0;
		for(int i = n; i >= 1; i--){
			if(check(i)){
				ans = i;
				break;
			}
		}
		printf("Case #%d: %d\n", cot++, ans);
	}
	return 0;
}
