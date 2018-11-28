#include <bits/stdc++.h>
 
using namespace std;
 
typedef long long ll;
typedef vector<int> vi;
typedef vector<long long> vii;
typedef vector<vector<int> > vvi;
typedef vector<vector<long long> > vvii;

 
#define boost std::ios::sync_with_stdio(false);cin.tie(0);cout.tie(0)
#define FOR(i,a,b) for(i= (a) ; i<(b); ++i)
#define pb push_back
#define mp make_pair
#define all(x) (x).rbegin() , (x).rend()
#define out(x) cout<<x<<"\n"
#define sz(x)  (x).size()
#define nl cout<<"\n"
#define INF 500001
#define F first
#define S second
 
int main()
{
	boost;
	int t,cnt=1;
	cin>>t;
	while(t--)
	{
		string s;
		cin>>s;
		int n = s.length();
		int i =n-1, j;
		while(i>0){
			if(s[i-1]>s[i]){
				s[i-1]--;
				FOR(j,i,n) 
					s[j]='9';
			}
			i--;
		}
		i=0;
		while(s[i]=='0')
			i++;
		cout<<"Case #"<<cnt++<<": "<<s.substr(i); nl;
	}
	return 0;
} 