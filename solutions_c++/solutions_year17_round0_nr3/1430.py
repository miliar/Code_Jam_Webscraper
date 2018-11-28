#include<bits/stdc++.h>
using namespace std;
int main(){
	ifstream in("C-large.in.txt");
	ofstream out("output.txt");
	int t;
	in>>t;
	for(int i=1;i<=t;++i){
		long long n,k;
		in>>n>>k;
		vector<map<long long,long long>> x;
		x.push_back({{n,1}});
		int count=0;
		while(true){
			map<long long,long long> cur;
			if(x[count].size()==1 && x[count].begin()->first==1)
				break;
			for(auto j:x[count]){
				if(j.first==1)
					continue;
				else if(j.first==2)
					cur[1]+=j.second;
				else if(j.first%2)
					cur[j.first/2]+=j.second*2;
				else{
					cur[j.first/2]+=j.second;
					cur[j.first/2-1]+=j.second;
				}
			}
			x.push_back(cur);
			++count;
		}
		long long cnt,ind=0;
		auto &cur=--x[ind].end();
		cnt=cur->second;
		while(true){
			if(cnt<k){
				if(cur==x[ind].begin()){
					++ind;
					cur=--x[ind].end();
				}
				else
					--cur;
				cnt+=cur->second;
			}
			else
				break;
		}
		long long ans=cur->first,ans1=ans/2,ans2=ans1;
		if(ans%2==0)
			ans2-=1;
		out<<"Case #"<<i<<": "<<ans1<<' '<<ans2<<endl;
	}
}
