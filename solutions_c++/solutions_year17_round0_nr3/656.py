#include<bits/stdc++.h>
using namespace std;
typedef long long LL;
struct sta{
	int l,r;
	int len()const{return r-l+1;}

	bool operator<(const sta &oth)const{
		return len()!=oth.len()?len()<oth.len():l>oth.l;
	}
};
void solve(){
	int n,k;
	cin>>n>>k;
	priority_queue<sta>q;
	q.push((sta){1,n});
	int ans1,ans2;
	map<pair<int,int>,int>M;
	while(k--){
		sta u=q.top();q.pop();
		int l=u.l,r=u.r;
		int m=(l+r)>>1;
//		cerr<<l<<" "<<r<<" "<<m<<endl;
		ans1=max(m-l,r-m);
		ans2=min(m-l,r-m);
		M[{ans2,ans1}]++;
//		cerr<<ans2<<" "<<ans1<<endl;
		if(l<=m-1)q.push((sta){l,m-1});
		if(m+1<=r)q.push((sta){m+1,r});
	}
	for(auto x:M)
		cerr<<x.first.first<<" "<<x.first.second<<" "<<x.second<<endl;
	printf("%d %d\n",ans1,ans2);
}

map<LL,map<pair<LL,LL>,LL> >H;
map<pair<LL,LL>,LL>calc(LL n){
	if(H.count(n))
		return H[n];
	map<pair<LL,LL>,LL>m;
	if(n==1){
		m[{0,0}]=1;
		return m;
	}
	if(n==2){
		m[{0,1}]++;
		m[{0,0}]++;
		return m;
	}
	if(n%2==0){
		m=calc((n-1)/2);
		map<pair<LL,LL>,LL>m2=calc(n/2);
		for(auto x:m2)
			m[x.first]+=x.second;
		m[{(n-1)/2,n/2}]++;
		return H[n]=m;
	}else{
		m=calc(n/2);
		for(auto &x:m)
			x.second*=2;
		m[{n/2,n/2}]++;
		return H[n]=m;
	}
}

void solve2(){
	LL n,k;
	cin>>n>>k;
	map<pair<LL,LL>,LL>m=calc(n);
	vector<tuple<LL,LL,LL> >vec;
	for(auto x:m){
		vec.emplace_back(x.first.first,x.first.second,x.second);
	}
	reverse(vec.begin(),vec.end());
	for(int i=0;i<vec.size();i++){
		k-=get<2>(vec[i]);
		if(k<=0){
			printf("%lld %lld\n",get<1>(vec[i]),get<0>(vec[i]));
			return ;
		}
	}
}

int main(){
//	solve();
//	solve2();
//	return 0;
	int T;
	cin>>T;
	for(int t=1;t<=T;t++){
		cerr<<t<<endl;
		printf("Case #%d: ",t);
		solve2();
	}
	return 0;
}
