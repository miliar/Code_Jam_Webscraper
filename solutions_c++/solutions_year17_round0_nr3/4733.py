#include <bits/stdc++.h>

using namespace std;

#define ll long long int
#define sd(x) scanf("%d",&x)
#define sc(x) scanf("%c",&x)
#define slld(x) scanf("%lld",&x)
#define ss(x) scanf("%s",x)
#define mod 1000000007
#define pb push_back
#define vint vector<int>

struct acompare{
	bool operator()(pair<int,int> p1, pair<int,int> p2){
		if(p1.second-p1.first==p2.second-p2.first)
			return p1.first>p2.first;
		return p1.second-p1.first < p2.second-p2.first;
	}
};

int main()
{
	freopen("input.txt" , "r", stdin);
	freopen("output.txt", "w", stdout);
	int t,n,m,i,j,k,l,x,y,mid;
	sd(t);
	pair <int,int> p1,p2;
	for(x=1;x<=t;x++){
		priority_queue < pair <int,int>, vector < pair <int,int> >, acompare > pq;
		sd(n);sd(k);
		p1=make_pair(1,n);
		pq.push(p1);
		while(k--){
			p1 = pq.top();
			pq.pop();
			mid=(p1.second+p1.first)/2 ;
			if(p1.first!=mid){
				p2=make_pair(p1.first,mid-1);
				pq.push(p2);
			}
			if(p1.second!=mid){
				p2=make_pair(mid+1,p1.second);
				pq.push(p2);
			}
		}
		printf("Case #%d: %d %d\n",x,max(mid-p1.first,p1.second-mid),min(mid-p1.first,p1.second-mid));

	}
	return 0;
}