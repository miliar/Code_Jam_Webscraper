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
ll d;
string s;
ll num[19];
vector<ll> ans;
int main()
{
	cin>>T;
	rep1(cnt,T){
		cout<<"Case #"<<cnt<<": ";
		ans.clear();
		cin>>s;
		ll L=s.size();
		rep(i,L){
			num[i]=s[i]-'0';
		}
		ll id=0;
		while(id<L-1&&num[id]<=num[id+1]) id++;
		if(id==L-1){
			rep(i,L){
				cout<<num[i];
			}
			goto next;
		}
		while(id>=0&&num[id]>num[id+1]){
			num[id]--;
			id--;
		}
		id++;
		rep(i,L){
			if(i==0&&num[0]==0) continue;
			if(i<=id) cout<<num[i];
			else cout<<"9";		
		}	
		next: ;
		cout<<endl;
	}
}
