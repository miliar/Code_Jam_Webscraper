#include<bits/stdc++.h>
using namespace std;
const int INF = 200000000;
#define FOR(i,n) for(int i=0,_n=n; i<_n; ++i)

int flips(int a[], int M, int N, int want) {
  int s[M]; FOR(i,M) s[i] = 0;
  int sum=0, ans=0;
  FOR(i,M) {
    s[i] = (a[i]+sum)%2 != want;
    sum += s[i] - (i>=N-1?s[i-N+1]:0);
    ans += s[i];
    if(i>M-N and s[i]!=0) return INF;
  }
  return ans;
}
int main() {
	FILE *fp,*fp1;
	fp=fopen("A-large.in","r");
	fp1=fopen("A-large-attempOut.in","w");
	int t;
	fscanf(fp,"%d",&t);
	for(int j=1;j<=t;j++){
		char str[1000];
		fscanf(fp,"%s",str);
		int M=strlen(str);
		int N;
		fscanf(fp,"%d",&N);
		int a[M];
		for(int i=0;i<M;i++){
			if(str[i]=='-')
				a[i]=0;
			else
				a[i]=1;
		}
		int flips1=flips(a,M,N,1);
		if(flips1>=200000000){
			fprintf(fp1,"Case #%d: IMPOSSIBLE\n",j);
		}
		else{
			fprintf(fp1,"Case #%d: %d\n",j,flips1);
		}
	}
}
