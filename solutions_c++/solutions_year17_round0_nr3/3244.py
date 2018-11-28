#include <bits/stdc++.h>

using namespace std;
int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	#define int long long
	int tc;
	cin>>tc;
	int kas=1;
	while(tc-->0){
		int n,k;
		cin>>n>>k;
		cout<<"Case #"<<kas++<<": ";
		priority_queue<int>bfs;
		map<int,int>gapcnt,enq;
		bfs.push(n);
		gapcnt[n]=1;
		int lastgap=-1;
		while(!bfs.empty()){
			int now=bfs.top();
			int cnt=gapcnt[now];
			bfs.pop();
			if(cnt>=k){
				lastgap=now;
				break;
			}
			if(now%2==0){
				gapcnt[now/2-1]+=cnt;
				gapcnt[now/2]+=cnt;
				if(enq[now/2-1]!=1)bfs.push(now/2-1),enq[now/2-1]=1;
				if(enq[now/2]!=1)bfs.push(now/2),enq[now/2]=1;
			}else{
				gapcnt[now/2]+=2*cnt;
				if(enq[now/2]!=1)bfs.push(now/2),enq[now/2]=1;
			}
			k-=cnt;
		}
		if(lastgap%2==0)cout<<lastgap/2<<' '<<lastgap/2-1<<endl;
		else cout<<lastgap/2<<' '<<lastgap/2<<endl;
	}
	return 0;
}
