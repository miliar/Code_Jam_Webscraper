#include <bits/stdc++.h>
#define pb push_back
#define fio ios_base::sync_with_stdio(false)
#define ll long long
# define cc cin.tie(NULL)
#define vecs vector<string>
#define veci vector<int >
#define mp make_pair
#define ss second
#define ff first
using namespace std;
int main(){
	long long int d,n,T,x=1;
	cin>>T;
	for(x;x<=T;x++){
		double time=0;
		cout<<"Case #"<<x<<": ";
		vector <pair<long long int,long long int>> v;
		cin>>d>>n;
		for(int i=0;i<n;i++){
			long long int sp,pos;
			cin>>pos>>sp;
			v.pb(mp(pos,sp));
		}
		sort(v.begin(),v.end());
		for(int i=n-1;i>=0;i--){
			double time1=double(d-v[i].ff)/double(v[i].ss);
			time=max(time,time1); 
		}
		double speed=double(d)/time;
		printf("%.6f\n",speed);
	}
} 