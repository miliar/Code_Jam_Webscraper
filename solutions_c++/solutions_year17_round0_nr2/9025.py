#include<bits/stdc++.h>
#define endl '\n'
#define MAXN 1e9
#define int long long
using namespace std;
int check(int k){
	int t=k;
	vector<int> v;v.clear();
	while(t) v.push_back(t%10),t/=10;
	int cmp=v[0],p=0;bool state=true;
	for(int i=1;i<v.size();i++){
		if(v[i]>cmp){
			p=i,state=false;break;
		}
		cmp=v[i];
	}
	if(state) return 1e9;
	else return p;
}
int divide(int k){
	int p=check(k);
	if(p==1e9) return k;
	vector<int> v;v.clear();int t=k;
	while(t) v.push_back(t%10),t/=10;
	for(int i=p-1;i>=0;i--) v[i]=9;
	int borrow=1;
	while(borrow && p<v.size()){
		v[p]-=1;
		if(v[p]<0) v[p]=9;
		else borrow--;
		p++;
	}
	int sz=v.size();
	if(borrow) sz-=1;
	int res=0;
	for(int i=sz-1;i>=0;i--)
		res=res*10+v[i];
	return divide(res);
}
main(){
freopen("B-large.in","r",stdin);
freopen("out.txt","w",stdout);
	int n;cin>>n;
	for(int i=1;i<=n;i++){
		int k;cin>>k;
		cout<<"Case #"<<i<<": ";
		cout<<divide(k)<<endl;
	}
	return 0;
}

