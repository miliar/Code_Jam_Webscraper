#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int,int> PII;

#define MAX_N 1005

int T;
ll N;
int a[25];
int len;

int main(){
	freopen("B-large.in","r",stdin);
	freopen("ansB1.txt","w",stdout);

	scanf("%d",&T);
	//precal();

	for(int ts=1;ts<=T;++ts){
		scanf("%lld",&N);

		ll x=N;
		for(int i=0;x>0;++i){
			a[i]=x%10;
			x/=10;
			if(x==0){
				len=i+1; // [0,i) -> [0,i-1]
			}
		}

		for(int i=1;i<len;++i){
			if(a[i]<=a[i-1])continue;
			if(a[i]==0){ // not necessary
				a[i+1]--;
				a[i]=a[i-1]=9;
			}
			else if(a[i]==1){
				a[i]=0;
				for(int j=i-1;j>=0;--j){
					a[j]=9;
				}
			}
			else {
				a[i]--;
				for(int j=i-1;j>=0;--j){
					a[j]=9;
				}
			}
		}

		printf("Case #%d: ",ts);
		while(a[len-1]==0){
			--len;
		}
		for(int i=len-1;i>=0;--i){
			printf("%d",a[i]);
		}
		puts("");
	}


	fclose(stdin);
	fclose(stdout);

	return 0;
}
