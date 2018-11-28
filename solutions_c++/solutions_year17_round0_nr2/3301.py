/*input
4
132
1000
7
111111111111111110
*/
#include <bits/stdc++.h>

using namespace std;

#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define all(v) (v).begin(), (v).end()
#define uniq(v) (v).erase(unique(all(v)), v.end())
#define IOS ios::sync_with_stdio(0);
#define sz(v) (v).size()
#define fr(a, b, c) for(int (a) = (b); (a) < (c); ++(a))
#define rp(a, b) fr(a,0,b)
#define cl(a, b) memset((a), (b), sizeof(a))
#define sc(a) scanf("%d", &a)
#define sc2(a, b) scanf("%d %d", &a, &b)
#define sc3(a, b, c) scanf("%d %d %d", &a, &b, &c)
#define pr(a) printf("%d\n", a);
#define pr2(a, b) printf("%d %d\n", a, b)
#define pr3(a, b, c) printf("%d %d %d\n", a, b, c)
#define IOS ios::sync_with_stdio(0);

typedef unsigned long long ull;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef pair<ll, ll> pll;

string solve(string& num)
{
	int start = num[sz(num) - 1] - '0';
	for(int i = sz(num)-2; i >= 0; --i)
	{
		int dig = num[i] - '0';
		if(dig > start)
		{
			dig = dig - 1;
			num[i] = '0' + dig;
			for(int j = i+1; j < sz(num); ++j)
				num[j] = '9';
		}
		start = dig;
	}
	return num;
}
int main()
{
	ifstream in; in.open("bin.txt"); 
	ofstream out; out.open("bout2.txt");
	int t;
	in >> t;
	fr(T, 0, t)
	{
		ull x;
		in >> x;
		//out << x << " ";
		if(x < 10)
		{
			out << "Case #" << T+1 << ": " << x << endl;
			continue;
		}
		string num = to_string(x);
		string tmp;
		rp(i, sz(num))
			tmp += "1";
		ull low = stoull(tmp);
		
		if(x < low)
		{
			string resp;
			rp(i, sz(num)-1)resp += "9";
			out << "Case #" << T+1 << ": " << resp << endl;
			continue;
		}
		else out << "Case #" << T+1 << ": " << solve(num) << endl;
	}
	out.close();
	in.close();
	return 0;
}
