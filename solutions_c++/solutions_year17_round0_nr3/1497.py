#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <chrono> //1e+9で割る auto end= chrono::system_clock::now()-st;  cout<<end.count()%1e+9<<endl;
using namespace std;
typedef long long ll;
typedef pair<ll,ll> P;
typedef long double db;

#define fr first
#define sc second
#define pb push_back
#define rep(i,x) for(ll i=0;i<x;i++)
#define rep1(i,x) for(ll i=1;i<=x;i++)
#define rrep(i,x) for(ll i=x-1;i>=0;i--)
#define rrep1(i,x) for(ll i=x;i>0;i--)

ll T;
ll N,K;
map<ll,ll> mp;
priority_queue<ll> q;

int main()
{
	cin>>T;
	rep1(cnt,T){
		cout<<"Case #"<<cnt<<": ";
		mp.clear();
		while(!q.empty()) q.pop();
		cin>>N>>K;
		q.push(N);
		mp[N]=1;
		ll now=0,x,kosu;
		while(1){
			x=q.top();
			q.pop();
			kosu=mp[x];
			now+=kosu;
			if(x%2==0){
				if(mp.find(x/2)==mp.end()){
					mp[x/2]=kosu;
					q.push(x/2);
				}
				else mp[x/2]+=kosu;
				if(mp.find(x/2-1)==mp.end()){
					mp[x/2-1]=kosu;
					q.push(x/2-1);
				}
				else mp[x/2-1]+=kosu;
			}
			else{
				if(mp.find(x/2)==mp.end()){
					mp[x/2]=kosu*2;
					q.push(x/2);
				}
				else mp[x/2]+=kosu*2;
			}
			if(now>=K){
				break;
			}
		}
		P ans=P(x/2,(x%2==1)?x/2:x/2-1LL);
		cout<<ans.fr<<" "<<ans.sc<<endl;
	}
}
