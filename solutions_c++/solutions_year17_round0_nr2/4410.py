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

vector<int>v;

lli digicount(lli n)
{
	lli count=0;
	while(n!=0)
	{
		count++;
		n/=10;
	}
	return count;
}

int check(int y){
	for(int i=2;i<=y;i++){
		if(v[i]<v[i-1])
			return 0;
	}
	return 1;
}


int main()
{
	lli t,r,sum,n;
	cin>>t;
	r=t;

	while(t--){

		cin>>n;
		v.clear();

		int digi=digicount(n);
		for(int i=1;i<=digi;i++){
			v.push_back(n%10);
			n=n/10;
		}
		v.push_back(0);
		
		reverse(v.begin(),v.end());
		int j=digi;
		while(check(digi)!=1){

			v[j]=9;
			v[j-1]--;
			j--;


		}

		lli sum=0;

		for(int i=1;i<=digi;i++){
			sum=sum*10+v[i];
		}
		cout<<"Case #"<<r-t<<": "<<sum<<endl;
	}

	return 0;
}