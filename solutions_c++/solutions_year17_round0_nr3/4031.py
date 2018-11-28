#include <iostream>
#include <stdio.h>
#include <queue>
#include <map>
#include <vector>
#include <algorithm>
#include <sstream>
#include <utility>
using namespace std;

typedef pair<long long ,long long> ii;
vector <ii> a(1000001);
long long x,n,k,y,z;

int main(){
	int T;
	ios_base::sync_with_stdio(0);
	freopen("C-small-2-attempt0.in","r",stdin);
	freopen("C-small2.out","w",stdout);
//	freopen("C-large.in","r",stdin);
//	freopen("C-large.out","w",stdout);
	cin>>T;
	a[0]=make_pair(0,0); a[1]=make_pair(0,0);
	for(int i=2;i<=1000000;i++){
		if(i%2==0) a[i]=make_pair(a[i-1].first+1,a[i-1].second);
		else a[i]=make_pair(a[i-1].first,a[i-1].second+1);
	}
	for(int t=1;t<=T;t++){
		priority_queue<long long> q;
		cin>>n>>k;
		q.push(n);
		y=a[n].first; z=a[n].second;
		while(k){
			x=q.top();
			q.pop();
			q.push(a[x].first);
			q.push(a[x].second);
			y=a[x].first; z=a[x].second;
			k--;
		}
		cout<<"Case #"<<t<<": "<<y<<" "<<z<<endl;
	}
	
}

