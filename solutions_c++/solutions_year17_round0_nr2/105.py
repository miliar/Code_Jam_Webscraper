#include <cstdio>
#include <cstring>
using namespace std;
int a[105];
long long build(int a[], int len, int x){
	long long ret = 0;
	int i;
	for(i=0;i<=x;i++){
		ret *= 10;
		ret +=a[i];
	}
	for(;i<len;i++){
		ret *= 10;
		ret += 9;
	}
	return ret;
}
int main(){
	int T,tt=0,i,j,k,l,len;
	long long n,ans;
	scanf("%d",&T);
	while(T--){
		tt++;
		scanf("%I64d",&n);
		ans = 0;
		len = 0;
		while(n){
			a[len] = (int)(n%10);
			n/=10;
			len++;
		}
		for(i=0,j=len-1;i<j;i++,j--){
			k=a[i];a[i]=a[j];a[j]=k;
		}
		for(i=len-1; i>=0; i--){
			for(j=0;j<i;j++){
				if(a[j]>a[j+1])break;
			}
			if(j>=i){
				if(i==len-1){ans = build(a,len,i);break;}
				if(i>0&&a[i]>a[i-1]){
					a[i]--;
					ans = build(a,len,i);
					break;
				}
				if(i==0&&a[i]>1){
					a[i]--;
					ans = build(a,len,i);
					break;
				}
			}
		}
		if(i<0){
			ans = build(a,len-1,-1);
		}
		printf("Case #%d: %I64d\n",tt,ans);
	}
	return 0;
}
