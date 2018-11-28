#include<bits/stdc++.h>
using namespace std;

map<int,int>mp;
map<int,int>::iterator ii;

int main(){
	freopen("inp.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t,n,k,tt;
	scanf("%d",&t);
	for(tt=1;tt<=t;++tt){
		scanf("%d %d",&n,&k);
		mp.insert(make_pair(n,1));
		int cnt=0,ans1,ans2;
		while(cnt<k){
			ii=mp.end(); --ii;
			int length=ii->first;
			int current_cnt=ii->second;
			mp.erase(ii);
			if(cnt+current_cnt>=k){
				cnt=cnt+current_cnt;
				if(length%2!=0){
					ans1=length/2;
					ans2=length/2;
				}
				else{
					ans1=length/2;
					ans2=ans1-1;
				}
			}
			else{
				cnt=cnt+current_cnt;
				if(length%2!=0){
					int temp=length/2;
					ii=mp.find(temp);
					if(ii!=mp.end())
						ii->second+=(current_cnt*2);
					else
						mp.insert(make_pair(temp,(current_cnt*2)));
				}
				else{
					int temp=length/2;
					ii=mp.find(temp);
					if(ii!=mp.end())
						ii->second+=(current_cnt);
					else
						mp.insert(make_pair(temp,(current_cnt)));
					temp=temp-1;
					ii=mp.find(temp);
					if(ii!=mp.end())
						ii->second+=(current_cnt);
					else
						mp.insert(make_pair(temp,(current_cnt)));
				}
			}
		}
		printf("Case #%d: ",tt);
		printf("%d %d\n",ans1,ans2);
		mp.clear();
	}
	return 0;
}
