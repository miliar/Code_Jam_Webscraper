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
//string s;
//global end


int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);

	int t;
	cin>>t;
	for(int id = 1; id<=t; id++){
		string s;
		int k;
		cin>>s>>k;
		vb pan;
		for(auto i:s)
			pan.pb(i=='+' ? 1:0);

		int p=-1,ans=0;
		bool valid=true;
		while(++p + k <= s.length()){
			if(pan[p])
				continue;
			ans++;
			for(int i=p; i<p+k; i++)
				pan[i]=!pan[i];
		}
		for(;p<s.length();p++)
			if(!pan[p])
				valid=false;
		if(valid)
			cout<<"Case #"<<id<<": "<<ans<<"\n";
		else
			cout<<"Case #"<<id<<": "<<"IMPOSSIBLE"<<"\n";
	}

	return 0;
}