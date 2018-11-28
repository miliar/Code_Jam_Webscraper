/* In the Name of God */
#include <bits/stdc++.h> 
#define F first
#define S second
#define mod 1000000007

using namespace std;
typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;
typedef pair<int,char> pic;

const int maxn = 100000+10;

ofstream fout("out.out");

int main()
{
	int t ,test = 1 ;
	cin>>t;
	while(t)
	{
		int n , r , o , y , g , b , ban ;
		cin>>n>>r>>o>>y>>g>>b>>ban;
		
		string ans = "";
		vector<pic>v;
		v.push_back(pic(r , 'R'));
		v.push_back(pic(b , 'B'));
		v.push_back(pic(y , 'Y'));

		sort(v.begin() , v.end() );
		int p = 1 ;

		if(v[2].F <= v[1].F + v[0].F)
		{

			for( int i = 0 ; i < v[2].F ; i ++ )
			{
				if( v[1].F == 0 )
					p = 0 ;
				ans+=v[2].S;
				ans+=v[p].S;
				v[p].F--;
			}
			for(int i = 0 ; i < v[0].F  ; i ++ )
			{
				for (int j = 1 ; j < ans.size() ; j ++ )
					if(ans[j-1] !=v[0].S && ans[j]!= v[0].S)
					{
						ans.insert(ans.begin()+j , 1 , v[0].S);
						break;
					}
			}
			fout<<"Case #"<<test<<": "<<ans<<endl;
			
		}
		else
			fout<<"Case #"<<test<<": "<<"IMPOSSIBLE"<<endl;
		
		t--;
		test ++ ;
	}	
}	
