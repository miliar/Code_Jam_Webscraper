#include<bits/stdc++.h>
using namespace std;
int main(){
	freopen("in1.txt","r",stdin);
	freopen("out1.txt","w",stdout);
	int testcase;
	scanf("%d",&testcase);
	int cnt=1;
	while(testcase--){
		int n,k;
		scanf("%d%d",&n,&k);
		priority_queue<int> pq;
		int ans1=-1,ans2=-1;
		pq.push(n);
		while(k--){
			int t=pq.top();
			pq.pop();
			if(t%2==0){
				ans1=t/2;
				ans2= ans1-1;
			}
			else{
				ans1=t/2;
				ans2=ans1;
			}

			pq.push(ans1);
			pq.push(ans2);
		}
		printf("Case #%d: %d %d\n",cnt++,ans1,ans2);
	}
}