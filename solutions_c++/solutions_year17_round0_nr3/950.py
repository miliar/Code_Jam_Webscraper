#include<iostream>
#include<queue>
#include<map>
#define ull unsigned long long
using namespace std;
int main(){
	int test;
	cin>>test;
	for(int tt=1;tt<=test;tt++){
		ull mmax=0,mmin=0;
		ull n,k;
		cin>>n>>k;
		ull pro=0;
		priority_queue<pair<ull,ull> > pq;
		pq.push(make_pair(n,1));
		while(1){
			map<ull,ull> mp;
			while(!pq.empty()){
				pair<ull,ull> tp=pq.top();
				pq.pop();
				pro+=tp.second;
				tp.first--;
				ull lo=tp.first/2;
				ull hi=tp.first-lo;
				if(pro>=k){
					mmax=hi;
					mmin=lo;
					break;
				}
				mp[lo]+=tp.second;
				mp[hi]+=tp.second;
			}
			if(pro>=k){
				break;
			}
			for(auto x:mp){
				if(x.first!=0){
					pq.push(make_pair(x.first,x.second));
				}
			}
		}
		cout<<"Case #"<<tt<<": "<<mmax<<" "<<mmin<<endl;
	}
	return 0;
}
