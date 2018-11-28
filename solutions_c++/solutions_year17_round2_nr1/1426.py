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
		double D;
		int N;
		cin>>D>>N;
		vector<pair<double, double> > arr(N);
		for(int i=0;i < N;i++)
			cin>> arr[i].first>>arr[i].second;
		sort(all(arr));
		double tt = 0;
		for(int i = 0; i <N;i++)
			tt = max(tt,(D-arr[i].first)/arr[i].second);
		double ans = D/tt;

		cout <<fixed<<setprecision(6)<<"Case #"<<tc<<": "<<ans<<"\n";




	}
}
		



