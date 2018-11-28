#include<bits/stdc++.h>
#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define tr(c,i) for(auto i = (c).begin(); i != (c).end(); i++) 
#define F(i,n) for(int i=0;i<n;i++)
#define VE(i,v) for(int i = 0;i < sz(v);i++)
using namespace std;
typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef long long ll;
typedef unsigned int ui;
const double PI  =3.141592;
struct Compare
{
    bool operator ()( const std::pair<int,pair<int, int> > &p1, 
                      const std::pair<int,pair<int, int> > &p2 ) const
    {
        if(p1.first!=p2.first)
		return p1.first>p2.first;
	else 
		return p1.second.first < p2.second.first;
    }
};
int main()
{
//std::ios::sync_with_stdio(false);
	cin.tie(NULL);
	int T;
	cin >> T;
	for(int tc= 1; tc<= T; tc++)
	{
		ll N,K;
		cin>> N>>K;
		ll pow2= (ll) 1;
		int po = 0;
		ll cnt = 0;
		while(cnt+pow2<=K)
		{
			cnt = cnt+pow2;
			po+= 1;
			pow2 = ((ll)1)<<po;
		}
		ll diff = K-cnt;
		if(diff==0)
		{
			po--;
			pow2 = ((ll)1)<<po;
		}
		ll len = N/pow2;
		ll x = N-cnt-(pow2)*(len-1);
		//cout<<cnt<<" "<<pow2<<" "<<len<<" "<<x<<"\n";
		if(diff>x)
			len--;
		ll ma = len/2;
		ll mi;
		if(len%2==1)
			mi = len/2;
		else
			mi = len/2-1;
		if(len<=1)
			mi = 0;

		cout <<"Case #"<<tc<<": "<<ma<<" "<<mi<<"\n";




	}
}
		



