#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define ll long long
#define MOD 1e9 + 7
#define ull unsigned long long
#define iloop(a,b) for(ll i = a; i < b; ++i)
#define jloop(a,b) for(ll j = a; j < b; ++j)
using namespace std;
typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef pair<int,int> ii; 
#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define tr(c,i) for(typeof((c).begin() i = (c).begin(); i != (c).end(); i++) 
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end()) 
#define p(a) cout << a << "\n";
vector<string> vec;
int number = 18 ;
void permutation(int a, string s, int x)
{
	if(x == 0)
	{
		vec.pb(s);
		return;
	}
	for(int i = a; i <= 9; ++i)
	{
		string temp = s + to_string(i);
		permutation(i,temp,x-1);
	}
}
ll search(ll num)
{
	ll len = vec.size();
	for(ll i = 0; i < len; ++i)
	{
		ll temp = stoll(vec[i]);
		if(temp > num)
		{
			return i-1;
		}
	}
	return len-1;
}
void solve()
{
	ll n,t;
	scanf("%lld",&t);
	ll index,ans;
	string s = "";
	bool flag;
	permutation(0,s,number);
	for(ll i = 1; i <= t; ++i)
	{	
		cin >> n;
		ans = search(n);
		flag = true;
		for(int i = 0; i < vec[ans].size(); ++i)
		{
			if(flag && vec[ans][i] != '0')
			{
				flag = false;
				index = i;
			}
		}
		cout << "Case #" << i << ": "; 
		for(int i = index; i < vec[ans].size(); ++i)
		{
			cout << vec[ans][i];
		}
		cout << "\n";
	}
}
int main()
{
	bool testing = true;
	/*std::ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);*/
	if(testing)
	{
		freopen("B-large.in","rt",stdin);
		freopen("output.txt","wt",stdout);
		int start = clock();
		solve();
		int end = clock();
		//cout << "time: " << (end - start)/(double)(CLOCKS_PER_SEC)*1000 << " milliseconds\n";
	}
	else
	{
		solve();
	}
}