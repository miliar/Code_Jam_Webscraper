/** O poor unthinking human heart ! Error will not go away logic and reason are slow to penetrate.
	We cling with both arms to false hopes , refusing to give way to the wieghtest proofs against it.
	Embracing it with all our strength.
	In the end it goes,ripping our veins and draining our heart's blood,until regaining consiousness
	we fall into snares of delusion all over again 
	*/
 
 
#include<bits/stdc++.h>
#define rep(i,n) for( int (i)=0;(i)<(int)(n);(i)++)
#define sz(v) (int)((v).size())
#define FOR(i,k,n) for(int i=(k);i<(int)(n);i++)
#define VI vector<int>
#define VS vector <string>
#define SORT(c) sort((c).begin(),(c).end())
#define pb push_back
#define gc getchar_unlocked
#define Q queue<int> 
#define s(n) scanf("%d",&n)
#define sll(n) scanf("%lld",&n)
#define p(n) printf("%d",n)
#define pll(n) printf("%lld",n)
#define mem(s,v) memset(s,v,sizeof s)
#define pp pair<int,int> 
#define pp1 pair<int,pair<int,int> > 
#define INF 999999
#define VP vector<pp> 
#define QP queue<pp>
#define endl '\n'
typedef long long ll;
using namespace std;
int main()
{
	ios_base::sync_with_stdio(false);cin.tie(NULL);
 
		#ifndef ONLINE_JUDGE
    	freopen("in.txt", "r", stdin);
		#endif


		int t;
		cin>>t;int ca=1;
		while(t--){

			string s;cin>>s;
			int n;cin>>n;
			int ans=0;
			for(int i=0;i<s.size();i++){

					if(s[i]=='-'){
							if(i+n>s.size())
									break;
							ans++;

							rep(j,n){
										s[i+j]=(s[i+j]=='+')?'-':'+';
							}
					}



			}

			rep(i,s.size()){
					if(s[i]=='-'){
							ans=-1;
							break;
					}
			}
			cout<<"Case #"<<ca<<": ";
			ans==-1?cout<<"IMPOSSIBLE"<<endl:cout<<ans<<endl;
			ca++;



		}
	}