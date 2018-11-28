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
const  long double PI  =3.141592;
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
		int N, Q;
		cin>>N>>Q;

		vector<pair<long double,long double> > H(N);
		for(int i =0; i <N;i++)
		{
			cin>>H[i].first>>H[i].second;
			//cout<<H[i].first<<H[i].second<<"\n";
		}
		vector<vector<long double>> dist(N+1,vector<long double>(N+1,-1));
		for(int i =1; i<=N;i++)
			for(int j =1; j <=N;j++)
				cin>>dist[i][j];
		int S, D;
		cin>> S>>D;
		vector<long double> ans(N+1,100000000001.0);
		ans[1]=0;
		for(int i =1; i < N;i++)
		{
			 long double dis = 0;

			for(int j =i+1; j<=N;j++)
			{
				dis +=dist[j-1][j];
				
				if(H[i-1].first>=dis)
					ans[j]= min(ans[j],ans[i]+dis/H[i-1].second);
				//cout<<i<<" "<<j<<" "<<ans[j]<<" "<<H[i-1].second<<"\n";
			}
		}




		cout<<fixed <<"Case #"<<tc<<": "<<ans[N]<<"\n";
	






	}
}
		



