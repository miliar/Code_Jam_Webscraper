#include <bits/stdc++.h>
#include<bitset>
using namespace std;
#define bye return 0
#define oo 2139062143 // 127
#define all(x) x.begin(),x.end()
#define sz(x) (int)x.size()
#define F  first
#define S  second
#define EPS 1e-15
#define khod push_back
#define mod 1000000007
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<pii> vpii;
typedef vector<pll> vpll;
typedef vector<string> vs;
typedef map<int, int> mpii;
typedef map<ll, ll> mpll;
int dx[] = { 0, 1, -1, 0 };
int dy[] = { 1, 0, 0, -1 };
ld PI = 3.14159265358979323846264338327950;
const int N = 50005;
int val(char c)
{
    if (c >= '0' && c <= '9')
        return (int)c - '0';
    else
        return (int)c - 'A' + 10;
}
ll toDeci(string str, int base)
{
    ll len = sz(str);
    ll power = 1;
    ll num = 0;
    ll i;
    for (i = len - 1; i >= 0; i--)
    {
        if (val(str[i]) >= base)
        {
           printf("Invalid Number");
           return -1;
        }

        num += val(str[i]) * power;
        power = power * base;
    }

    return num;
}
int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	freopen("B-small-attempt0.in", "r", stdin);
	freopen("b.txt", "w", stdout);
	int tc;
	cin >> tc;
	int t = 0 ;
	while (tc--) {
		cout<<"Case #"<<++t<<": ";
		int x ;
		cin>>x;
		for(int i = x ; i>= 1 ; i--){
			stringstream ss ;
			string s ;
			ss<<i;ss>>s;ss.clear();
			ll y =toDeci(s,10);
			string xx ;
			ss<<y;ss>>xx;ss.clear();
			string yy = xx ;
			sort(all(yy));
			if(yy==xx){cout<<i<<"\n";break;}
		}

	}
	bye;
}
