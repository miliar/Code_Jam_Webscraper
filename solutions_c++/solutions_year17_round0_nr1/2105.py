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

int main()
{
//std::ios::sync_with_stdio(false);
	cin.tie(NULL);
	int T;
	cin >> T;
	for(int tc= 1; tc<= T; tc++)
	{
		string S;
		cin>> S;
		int N;
		cin>>N;
		vector<char> cS(all(S));
		vi bcs(sz(cS),0);
		VE(i,cS)
			if(cS[i]=='+')
				bcs[i]=1;		
		int i = 0;
		int ans = 0;
		while(i<sz(cS))
		{
			while((bcs[i]==1)&&(i<sz(cS)))
				i++;
			if((i<sz(cS)) && (i>sz(cS)-N))
			{
				ans=-1;
				//cout<<i<<" "<<sz(cS)<<":::\n";
				break;
			}
			if(i<=sz(cS)-N)
			{
				for(int j = i; j < i +N;j++)
					if(bcs[j]==1)
						bcs[j]=0;
					else
						bcs[j]=1;
				ans++;
				i++;
				//cout<<i<<" "<<ans<<"\n";
			}
			/*for(int k =0; k <sz(cS);k++)
				cout<<bcs[k]<<" ";
			cout<<"\n";*/
		}
		if(ans==-1)
			cout <<"Case #"<<tc<<": "<<"IMPOSSIBLE\n";
		else
			cout <<"Case #"<<tc<<": "<<ans<<"\n";




	}
}
		



