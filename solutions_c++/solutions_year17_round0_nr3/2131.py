#include<bits/stdc++.h>

# define ini(c) int c; scanf("%d",&(c))
# define outi(c) printf("%d \n",(c)) 
# define rf freopen("input.txt","r",stdin)
# define wf freopen("output.txt","w",stdout)
# define pb(c) push_back(c)
# define mp(c,d) make_pair(c,d)
# define all(c) (c).begin(),(c).end()
# define tr(c,i) for(typeof((c).begin()) i=(c).begin();i!=(c).end();i++)
# define test(c) ini(c);while(c--)

using namespace std;

typedef vector< int > vi;
typedef vector< vi > vvi;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<vii> vvii;
typedef long long ll;

int main()
{
	rf;
	wf;
	int t;
	cin>>t;
	ll k,n;
	ll count=1;
	ll total=0;
	ll current;
	ll r,g;
	ll a,b;
	for(int it=1;it<=t;it++)
	{
		count=1;
		total=0;
		cin>>n>>k;
		current=k;
		while(current>count){
			total=total+count;
			current=current-count;
			count=2*count;
			

		}
		ll flag=0;
	//	cout<<current<<" "<<count<<" "<<total<<endl;
		n=n-total;
		r=n/count;
		if(r==0){
			a=0;b=0;
			flag=1;
		}
		else if(r==1){
			g=n-count;
		}
		else{
		g=(n-r*count);}
	//	cout<<current<<" "<<count<<" "<<total<<" "<<r<<" "<<g<<endl;
		
		if(flag==0){
		if(current<=g){
			a=r+1;
			if(a%2==0){
				a=a/2-1;
				b=a+1;
			}
			else{
				a=a/2;
				b=a;
			}
		}
		else{
			a=r;
			if(a%2==0){
				a=a/2-1;
				b=a+1;
			}
			else{
				a=a/2;
				b=a;
			}
		}
		}
		cout<<"Case #"<<it<<": "<<b<<" "<<a<<endl;

	}
	
}
