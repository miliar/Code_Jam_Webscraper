#include <bits/stdc++.h>
using namespace std;
// for( auto i :Templatename) // use dot notation
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
typedef pair<int,ii> iii;
typedef vector<ii> vii;
typedef vector<vii> vvii;
typedef vector< iii > viii;
typedef long long ll;
typedef vector<bool> vb;

#define PQ priority_queue
#define eb emplace_back
#define pb push_back
#define eps 10e-9;
#define PI 3.14159265359
#define MOD 1000000007
#define INF MOD
#define fi first
#define se second
#define FOR(i,n) for(int i=0;i<n;i++)
#define scani(n) scanf("%d",&n)


//global variable
// strtoll()
//global end
string create(char s0,int n){
	string s;
	while(n--)
		s+= s0;
	return s;
}

void rlw(string &s){
	int i=0;
	while(i < s.length() && s[i]=='0')
		i++;
	s= s.substr(i);
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);

	int t;
	cin>>t;
	for(int id = 1; id<=t; id++){
		string s,ans;
		cin>>s;
		for(int i=0; i< s.length(); i++){
			//cerr<<stoll( create(s[i],s.length()-i) )<<"  ";
			//cerr<<stoll( s.substr(i))<<"\n";
			if(stoll( create(s[i],s.length()-i) ) <= stoll( s.substr(i)) )
				ans+= s[i];
			else{
				ans+= (s[i] - 1);
				string tmp= create( '9', max(0UL, s.length() - i-1));
				ans+= tmp;
				break;
			}
		}
		rlw(ans);
		cout<<"Case #"<<id<<": "<<ans<<"\n";
	}

	return 0;
}