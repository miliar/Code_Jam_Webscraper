#include <bits/stdc++.h>

#define lli long long int

using namespace::std;

int main(){
	int t;
	cin>>t;
	int x=0;
	while(t--){
		x++;
		lli n,k;
		cin>>n>>k;
		pair<lli,lli> p,pnew;
		priority_queue<pair<lli,lli> > q;
		p.first=n/2;
		p.second=(n-1)-(n/2);
		q.push(p);
		k--;
		while(k--){
			p=q.top();
			q.pop();
			pnew.first=p.first/2;
			pnew.second=(p.first-1)-(pnew.first);
			q.push(pnew);
			pnew.first=p.second/2;
			pnew.second=(p.second-1)-(pnew.first);
			q.push(pnew);
		}
		p=q.top();

		cout<<"Case #"<<x<<": "<<p.first<<" "<<p.second<<endl;
	}
	return 0;
}