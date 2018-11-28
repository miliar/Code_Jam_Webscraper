#include <bits/stdc++.h>
using namespace std;


#define LL long long
#define F first
#define S second
#define mp make_pair
#define PII pair<LL,LL>
#define PIII pair<LL,PII >

int main(){


  ios_base::sync_with_stdio(false);
  #ifndef ONLINE_JUDGE
  freopen("input.in","r",stdin);
  freopen("output.out","w",stdout);
  #endif

  int t,test = 1;
  cin>>t;
  while(t--){
  	LL k,n;
  	cin>>n>>k;

  	if(n == k){
  		cout<<"Case #"<<test++<<": 0 0"<<endl;
  		continue;
  	}
  	priority_queue<PIII,vector<PIII>,greater<PIII> > Q;
  	LL mid,minS,maxS;
  	mid = (n+1)/2;
  	minS = min(mid-1,n-mid);
  	maxS = max(mid-1,n-mid);

  	Q.push(mp(-(mid-1),mp(1,mid-1)));
  	Q.push(mp(-(n-mid),mp(mid+1,n)));

  	while(--k > 0 && !Q.empty()){
  		PIII top = Q.top();
  		Q.pop();
  		mid = (top.S.F + (top.S.S - top.S.F)/2);
  		minS = min(mid - top.S.F,top.S.S - mid);
  		maxS = max(mid - top.S.F,top.S.S - mid);

  		//cout<<"minS is "<<minS<<" maxS is "<<maxS<<" top.S.F is "<<top.S.F<<" top.S.S is "<<top.S.S<<" mid is "<<mid<<endl;
  		if(top.S.F <= mid-1)
  			Q.push(mp(-(mid - top.S.F),mp(top.S.F,mid-1)));
  		if(mid+1 <= top.S.S)
  			Q.push(mp(-(top.S.S - mid),mp(mid+1,top.S.S)));
  	}
  	cout<<"Case #"<<test++<<": "<<maxS<<" "<<minS<<endl;
  }
  return 0;
}