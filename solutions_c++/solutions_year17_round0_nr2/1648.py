#include<bits/stdc++.h>
using namespace std;

int T, arr[30],len;
long long num;

int main(){
	freopen("tidy.in","r",stdin);
	freopen("tidy.out","w",stdout);
	
	scanf("%d",&T);
	for (int i=1;i<=T;i++){
		scanf("%lld",&num);
		len=0;
		while (num>0){
			len++;
			arr[len]=num%10;
			num/=10;
		}
		int j=len;
		while (j>1 && arr[j]<=arr[j-1]) j--;
		if (j>1){
			arr[j]--;
			for (int k=1;k<j;k++) arr[k]=9;
			j++;
			while (j<=len && arr[j]>arr[j-1]) {
				arr[j]--;
				arr[j-1]=9;
				j++;
			}			
		}
		printf("Case #%d: ",i);
		if (arr[len]>0) printf("%d",arr[len]);
		for (int j=len-1;j>0;j--) printf("%d",arr[j]); printf("\n");
	}
	return 0;
}
