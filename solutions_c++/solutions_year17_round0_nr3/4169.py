#include<bits/stdc++.h>
using namespace std;

static const int MOD = 1000000007;

#define ll long long
#define ull unsigned long long

//DEBUG
bool debug=false;
#define DEB(x) if(debug==true){clog<<#x<<" = "<<x<<endl;}
#define DEB2(x,y) if(debug==true){clog<<#x<<" = "<<x<<"; "<<#y<<" = "<<y<<endl;}


int main(int argc,char *argv[])
{
	std::ios_base::sync_with_stdio(false);
	if(argc>1&&string(argv[1])=="-d") debug=true;
	priority_queue<ll> heaper; 
	int t,m,case_no=0;
	ll n,k,x,y,z,i,j;
	cin>>t;
	while(t--)
	{
		heaper = priority_queue<ll>();
		cin>>n>>k;
		heaper.push(n);
		for(i=0;i<k;i++)
		{
			x=heaper.top();
			x--;
			heaper.pop();
			y=x/2;
			z=x-y;
			heaper.push(y);
			heaper.push(z);
		}
		cout<<"Case #"<<(++case_no)<<": "<<max(y,z)<<" "<<min(y,z)<<endl;
	}
	return 0;
}