//editor: Jan Tang
//problem:
#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <map>
#include <stack>
#include <queue>
#include <set>
#include <cstdlib>
using namespace std;
#define set0(a) memset(a,0,sizeof(a));
#define CIN(a,n) for(int i=1;i<=n;i++) cin>>a[i];
typedef long long ll;
typedef unsigned long long ull;
const int Mod = 1e9+7;
const int maxn = 100005;
const int inf = 0x3f3f3f3f;
int num[22],ans[20];
long long n;
/*==============================head==========================*/
int main(){
		freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);	
	int t,kt=0;
	scanf("%d", &t);
	while(t--){
		scanf("%lld",&n);
		int knt = 0;
		while(n){
			num[++knt] = n%10;
			n /= 10;
		}
		for(int i=knt;i>=1;i--){
//			cout<<num[i]<<endl;
			int f=1;
			for(int j=i-1;j>=1;j--){
				if(num[j]<num[i])f=0;
			}
			if(f||num[i-1]>num[i])ans[i]=num[i];
			else if(num[i-1]<=num[i]){
				ans[i]=num[i]-1;
				for(int j = i-1;j>=1;j--) ans[j]=9;
				break;
			}
		}
		long long tp=1,anss=0;
		for(int i=1;i<=knt;i++){
//			cout<<i<<"  "<<ans[i]<<endl;
			anss+=1ll*ans[i]*tp;
			tp*=10;
		}
		printf("Case #%d: %lld\n", ++kt, anss);
	}
	return 0;
}