#include <bits/stdc++.h>
using namespace std;
#define lli long long int
#define lD long double
#define fio ios_base::sync_with_stdio(0)
#define mp(x,y) make_pair(x,y)
#define pb(x) push_back(x)
#define ii pair<int,int>
#define vB vector<bool>
#define vC vector<char>
#define vlD vector<lD>a
#define vvC vector<vC>
#define vi vector<int>
#define vvi vector<vi >
#define vii vector<ii >
#define vvii vector<vii >
#define ll pair<lli,lli>
#define vl vector<lli>
#define vvl vector<vl >
#define vll vector<ll >
#define vvll vector<vll >
#define M_PI 3.14159265358979323846
#define MOD 1000000007
#define MAX 200005
#define EPS 1e-4
#define NINF LONG_MIN
#define INF LONG_MAX
//cout<<"Case #"<<tc<<": ";

lD solv(vector<pair<lD,lD> > &A){
	//cout<<"YO\n";
	A.push_back(mp(0,0));
	sort(A.begin(),A.end());
	/*for(int i=0;i<A.size();i++){
		cout<<A[i].first<<" "<<A[i].second<<"\n";
	}*/
	lD ans=0;
	for(int i=A.size()-1;i>0;i--){
		ans=ans+M_PI*(A[i].first*A[i].first-A[i-1].first*A[i-1].first);
	}
	for(int i=0;i<A.size();i++){
		ans=ans+2*M_PI*A[i].first*A[i].second;
	}
	return ans;
}
lD solve(vector<pair<lD,lD> > &A,lli n,lli k){
	lli poww=pow(2,n);
	lD ans=NINF;
	for(int i=0;i<poww;i++){
		vector<pair<lD,lD> > V;
		for(int j=0;j<n;j++){
			if(i & (1<<j)){
				V.pb(A[j]);
			}
		}
		if(V.size()==k){
			ans=max(ans,solv(V));
		}
	}
	return ans;
}
int main(){
	lli t,tc=1;
	cin>>t;
	while(t--){
		lli n,k;
		cin>>n>>k;
		vector<pair<lD,lD> > A(n);
		for(int i=0;i<n;i++){
			cin>>A[i].first>>A[i].second;
		}
		cout<<"Case #"<<tc<<": ";
		//cout<<"\n";
		lD xxx=solve(A,n,k);
		cout<<fixed<<setprecision(10)<<xxx<<"\n";
		tc++;
	}
	return 0;
}