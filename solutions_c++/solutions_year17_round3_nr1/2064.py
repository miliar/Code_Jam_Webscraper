#include<bits/stdc++.h>
using namespace std;
#define fori(a,b) for(lli (i)=(lli)(a);(i)<=(lli)(b);(i)++)
#define forj(a,b) for(lli (j)=(lli)(a);(j)<=(lli)(b);(j)++)
#define fork(a,b) for(lli (k)=(lli)(a);(k)<=(lli)(b);(k)++)
#define pb push_back
#define mp make_pair
#define f first
#define s second
#define inf 1000000007
#define pi 3.14159265359
#define fastio ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define sz(a) (lli)(a).size()
#define iter(a) typeof((a).begin())
typedef long long int lli;
typedef vector< lli > vlli;
typedef pair<lli,lli> plli;
typedef set<lli> slli;
typedef map<lli,lli> mlli;


int main()
{
	lli t,n,r,ri,k,hi;
	cin>>t;
	r=t;
	while(t--){
		
		cin>>n>>k;
		
		vector< pair< pair<double,double>,double> >v;
		

		fori(1,n){
			cin>>ri>>hi;
			v.push_back({{ri,hi},2*M_PI*ri*hi});
			
		}

		sort(v.begin(),v.end());
		reverse(v.begin(),v.end());

		double max=-1;
		fori(0,n-k){

			double sum=M_PI*v[i].f.f*v[i].f.f+2*M_PI*v[i].f.f*v[i].f.s;
			vector<double>d;
			forj(i+1,n-1){

				d.push_back(2*M_PI*v[j].f.f*v[j].f.s);
				//cout<<2*M_PI*v[j].f.f*v[j].f.s<<"d"<<endl;
			}
			//cout<<sum<<" sum"<<endl;
			sort(d.begin(),d.end());
			reverse(d.begin(),d.end());
			for(int y=0;y<=(lli)(k-2);y++){
				sum+=d[y];
				//cout<<sum<<" sum"<<endl;
			}

			if(sum>max){
				max=sum;
			}
		}
			cout.precision(17);
			cout<<"Case #"<<r-t<<": "<<max<<endl;
	}

	return 0;
}	