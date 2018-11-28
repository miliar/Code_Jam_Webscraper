#include <cstdio>
#include <cstring>
#include <vector>
#include <queue>
#include <string>
#include <algorithm>
#include <iostream>
#include <string>
#include <map>
#include <set>
#include <functional>
#include <iostream>
#define MOD 1000000007LL
using namespace std;
typedef long long ll;
typedef pair<int,int> P;

int n,p;
int r[61];
int q[61][61];
int now[61];
int nr[61];

void solve(int ta){
	for(int i=0;i<n;i++){
		sort(q[i],q[i]+p);
	}
	for(int i=0;i<n;i++){
		now[i]=0;
	}
	int cnt=0;
	for(int i=1;i<=1000000;i++){
		bool flag2=true;
		for(int j=0;j<n;j++){
			nr[j]=r[j]*i;
			if(nr[j]>5100000)flag2=false;
		}
		if(!flag2)break;
		for(int j=0;j<n;j++){
			while(now[j]<p && q[j][now[j]]*100<nr[j]*90){
				now[j]++;
			}
		}
		bool flag=true;
		for(int j=0;j<n;j++){
			if(now[j]==p || q[j][now[j]]*100>nr[j]*110){
				flag=false;
			}
		}
		if(flag){
			for(int j=0;j<n;j++){
				now[j]++;
			}
			cnt++;
			i--;
		}
	}
	printf("Case #%d: %d\n",ta,cnt);
}

int main(void){
	int t;
	scanf("%d",&t);
	for(int i=0;i<t;i++){
		scanf("%d%d",&n,&p);
		for(int j=0;j<n;j++){
			scanf("%d",&r[j]);
		}
		for(int j=0;j<n;j++){
			for(int k=0;k<p;k++){
				scanf("%d",&q[j][k]);
			}
		}
		solve(i+1);
	}
	return 0;
}
