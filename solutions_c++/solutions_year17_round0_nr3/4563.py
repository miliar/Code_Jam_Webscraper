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
	lli t,n,r,k;
	cin>>t;
	r=t;
	while(t--){
		
		cin>>n>>k;
		priority_queue<lli>w;
		w.push(n);
		for(lli i=1;i<=k-1;i++){
			lli ww=w.top();
			lli n=ww/2;
			w.pop();
			if(ww%2==0){
				w.push(n-1);
				w.push(n);
			}
			else{
				w.push(n);
				w.push(n);

			}
			
		}

		lli ww=w.top();
		n=ww/2;
		if(ww%2==0)
			cout<<"Case #"<<r-t<<": "<<n<<" "<<n-1<<endl;
		else
			cout<<"Case #"<<r-t<<": "<<n<<" "<<n<<endl;
	}

	return 0;
}	