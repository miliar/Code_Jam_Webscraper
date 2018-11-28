#include<bits/stdc++.h>
using namespace std;
 
#define ll long long
#define dbg(x)  cout<<#x<<"="<<x<<endl
#define N 2001025
#define MOD  786433
#define pb push_back
#define iosbase  ios_base::sync_with_stdio(false)
#define dbg(x)  cout<<#x<<"="<<x<<endl



struct node
{
	ll len;
	node(ll l){
		len=l;
	}
	bool operator < (const node &other)const{
		return len > other.len;
	}
};
map< node,ll >mp,ans;
int main(){

	int tc;
	cin>>tc;
	ll n,k,ans1,ans2,l,r,flag;
	ll temp;
	for(int ca=1;ca<=tc;ca++){
		
		cin>>n>>k;
		mp[node(n)]++;
		flag=0;

		while(mp.size()>0){
			temp=mp.begin()->first.len;
			
			ans[node(temp)]+=mp.begin()->second;
			temp--;
			l=(temp/2);
			r=temp-l;
			if(l!=0)
				mp[node(l)]+=mp.begin()->second;
			if(r!=0)
				mp[node(r)]+=mp.begin()->second;
			
			 mp.erase(mp.begin());
			
		}

		for(auto it=ans.begin();it!=ans.end();it++){
			
			if(k>it->second)
				k-=it->second;
			else{
				flag=it->first.len;
				break;
			}
		}
		flag--;
		printf("Case #%d: %lld %lld\n",ca,flag-(flag/2),flag/2);
		mp.clear();
		ans.clear();
		

	}
}