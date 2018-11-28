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
const double PI  =3.141592653589793;
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
		int N,K;
		cin>>N>>K;
		vector<pair<double,double> > arr(N);
		for(int i=0;i<N;i++)
		{
			double r,h;
			cin >> r>>h;
			arr[i] = {2*PI*r*h,r};
		}
		double ans =0;
		for(int i=0;i<N;i++)
		{
			vector<pair<double,double> > arr1(N-1);
			int index =0;
			for(int j=0; j <N;j++)
			{
				if (i==j)
					continue;
				else
					arr1[index++] = arr[j];
			}
			sort(all(arr1));
			double maxr =0;
			for(int j =N-K; j <N-1;j++)
				maxr = max(maxr,arr1[j].second);
			if((arr[i].second)<maxr)
				continue;
			double tans =0;
			for(int j = N-K; j<N-1;j++)
				tans += arr1[j].first;
			tans+= arr[i].first + PI*arr[i].second*arr[i].second;
			ans = max(ans,tans);
		}



		

		printf ("Case #%d: %.9f\n", tc,ans);
		//cout <<fixed<<setprecision(9)<<"Case #"<<tc<<": "<<ans<<"\n";
		






	}
}
		



