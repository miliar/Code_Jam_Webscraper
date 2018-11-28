#include <bits/stdc++.h>

using namespace std;

#define uniq(x)  x.erase(unique(x.begin(),x.end()), x.end()) //Unique value find from vector
#define upper(arr,n,fixed) upper_bound(arr,arr+n,fixed)-arr  //Upper value search;
#define lower(arr,n,fixed) upper_bound(arr,arr+n,fixed)-arr  //Lower value search;
#define FOR(i,a,n) for(int i=a; i<(int)n; i++)
#define FORI(i,a,n) for(int i=a; i>=(int)n; i--)
#define pii pair<int,int>
#define vpii vector<pii>
#define mp make_pair
#define fi first
#define se second
#define pb push_back
#define sz(a) int((a).size())
#define fastIO() ios_base::sync_with_stdio(false); cin.tie(0)
#define endl "\n"
#define all(a) a.begin(), a.end()
#define MEMSET(p,i) memset(p,i,sizeof(p))
#define SSTR(x) static_cast< std::ostringstream & >( \
		( std::ostringstream() << std::dec << x ) ).str()


bool sorted(int n)
{
	string s = SSTR(n);
	string t = s;
	sort(all(t));
	return s == t;
}

bool check(string &s)
{
	FOR(i,0,sz(s)-1)
		if(s[i] > s[i+1])
			return false;
	return true;
}
void op(string &s)
{
	FOR(i,0,sz(s)-1){
		if(s[i] > s[i+1]){
			s[i] = s[i]-1;
			FOR(j,i+1,sz(s))
				s[j] = '9';
			return;
		}
	}
}

int main(void)
{
	
	fastIO();

	// int n = 12349876;
	// while(!sorted(n)){
	// 	n--;
	// }
	// cout << n << endl;

	// FOR(i,1,1000)
	// 	if(sorted(i))
	// 		cout << i << endl;


	int n;
	cin >> n;
	FOR(c,0,n){
		string s;
		cin >> s;
		while(!check(s)){
			op(s);
		}
		int i = 0;
		while(s[i] == '0')i++;

		cout << "Case #" << c+1 << ": ";
		cout << s.substr(i,sz(s)) << endl;
	}
	
	return 0;
}