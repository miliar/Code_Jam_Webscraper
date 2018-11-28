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
		int N, R, O,Y, G,B,V;
		vector<pair<int,char> > S(3),D(3);
		cin>>N>>S[0].first>>D[0].first>>S[1].first>>D[1].first>>S[2].first>>D[2].first;
		S[0].second='R';
		S[1].second='Y';
		S[2].second='B';
		sort(all(S));
		int diff1= S[1].first-S[0].first;
		int diff2= S[2].first-S[1].first;
		vector<char> ans;
		//cout<<diff1<<" "<<diff2<<"\n";
		for(int i =0; i <S[0].first;i++)
		{
			ans.pb(S[0].second);
			//cout<<S[0].second;
			while(diff1>0)
			{
				ans.pb(S[2].second);
				ans.pb(S[1].second);
				//cout<<S[2].second<<S[1].second<<diff1;
				diff1--;
			}
			ans.pb(S[2].second);
			ans.pb(S[1].second);
			//cout<<S[2].second<<S[1].second;
			if(diff2>0)
			{
				ans.pb(S[2].second);
				//cout<<S[2].second;
				diff2--;
			}
		}
		if(S[0].first==0)
		{
			while(diff1>0)
			{
				ans.pb(S[2].second);
				ans.pb(S[1].second);
				//cout<<S[2].second<<S[1].second<<diff1;
				diff1--;
			}
			if(S[1].first==0)
				ans.pb(S[2].second);
		}


		cout <<"Case #"<<tc<<": ";
		if(sz(ans)!=N)
			cout<<"IMPOSSIBLE\n";
		else
		{
			for(int i =0;i<N;i++)
				cout<<ans[i];
			cout<<"\n";
		}






	}
}
		



