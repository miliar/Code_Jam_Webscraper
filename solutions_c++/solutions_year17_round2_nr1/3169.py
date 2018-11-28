#include<bits/stdc++.h>

typedef long long int ll;
typedef unsigned long long int ull;

#define fast ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)
#define endl '\n'
#define pb push_back
#define mp make_pair
#define full(a) a.begin(),a.end()
#define mem(a,x) memset(a,x,sizeof(a))
#define test int t;cin>>t; while(t--)
#define MOD 1000000007

using namespace std ;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout); 
    int t;
    cin>>t;
    int hmm = 0;
    while(t--)
    {
    	int start , n;
    	cin>>start>>n ;
    	cout<<"Case #"<<++hmm<<": ";
    	vector< pair<int,int> > v(n); 
    	for(int i=0;i<n;i++) cin>>v[i].first>>v[i].second ; //start , speed
    	sort(v.begin(), v.end()) ;
    	double maxi = -1;
    	for(int i=0;i<n;i++)
    	{
    		maxi = max(maxi , (start - v[i].first )/(double)(v[i].second ) );
		}
		double ans = (double)(start)/maxi ;
		cout<<fixed<<showpoint;
		cout<<setprecision(10)<<ans<<endl;
	}
}
