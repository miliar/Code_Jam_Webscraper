#include<bits/stdc++.h>
#define LL long long
using namespace std;

LL N;
int cnt;
int arr[20];

LL cek(){
	LL ret=N;
	int bef=cnt;
	for(int i=cnt-1;i>0;i--){
		if(arr[i]<arr[i-1]) bef=i;
		else if(arr[i]>arr[i-1]){
			ret=0;
			for(int j=cnt-1;j>bef-1;j--){
				ret=ret*10+arr[j];
			}
			ret=ret*10+arr[bef-1]-1;
			for(int j=bef-2;j>=0;j--){
				ret=ret*10+9;
			}
			return ret;
		}
	}
	return ret;
}

int main(){
	FILE *fout = fopen("output_b.txt","w");
	int t;
	scanf("%d",&t);
	for(int tc=1;tc<=t;tc++){
		scanf("%lld",&N);
		LL M=N; cnt=0;
		while(M>0){
			arr[cnt]=M%10;
			cnt++;
			M/=10;
		}
		LL ans=cek();
		printf("Case #%d: %lld\n",tc,ans);
		fprintf(fout,"Case #%d: %lld\n",tc,ans);
	}
	return 0;
}
