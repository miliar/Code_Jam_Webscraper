#include <bits/stdc++.h>
using namespace std;
int a[1000005];
int main()
{
  freopen("C-small-2-attempt0.in","r",stdin);
  freopen("csmall2.out","w",stdout);
  int t;
  cin>>t;
  for(int i=1;i<=t;i++){
  	int n,k;
  	cin>>n>>k;
  	 a[n+2];
  	for(int j=0;j<n+2;j++)
  	    a[j]=0;
  	a[0]=-1;
  	a[n+1]=-1;
  	priority_queue<pair<int,pair<int ,int> > >pq;
  	pair<int,pair<int,int> >p1;
  	pair<int,int>p2;
  	p2.first=-1;
  	p2.second=-n;
  	p1.first=n;
  	p1.second=p2;
  	pq.push(p1);
  	int mid;
  	while(k--){
  		p1=pq.top();
  		pq.pop();
  		int space=p1.first;
  		p2=p1.second;
  		int x=p2.first;
  		int y=p2.second;
  		x=-x;
  		y=-y;
  		 mid=(x+y)/2;
  		a[mid]=-1;
  		if(y>x){
  			if(mid-1>=x){
  			p2.first=-x;
  			p2.second=-(mid-1);
  			p1.first=mid-x;
  			p1.second=p2;
  			pq.push(p1);
  		   }
  			if(y>=mid+1){
  				p2.first=-(mid+1);
  				p2.second=-y;
  				p1.first=y-mid;
  				p1.second=p2;
  				pq.push(p1);
  			}
  		}
  	}
  	int i1=mid-1,i2=mid+1;
  	int ls=0,rs=0;
  	while(a[i1]!=-1&&i1>=0){
  		ls++;
  		i1--;
  	}
  	while(a[i2]!=-1&&i2<=n+1){
  		rs++;
  		i2++;
  	}
  	cout<<"Case #"<<i<<": "<<max(ls,rs)<<" "<<min(ls,rs)<<endl;
  }
	return 0;
}

