#include <bits/stdc++.h>
#include <ext/pb_ds/tree_policy.hpp>
using namespace std;
#define fastScan ios_base::sync_with_stdio(0); cin.tie(NULL);
#define ABS(x) ((x) < 0 ? -1*(x) : (x))
#define MAX(x,y) ((x) > (y) ? (x) : (y))
#define MIN(x,y) ((x) < (y) ? (x) : (y))
#define mp make_pair
#define pb push_back
#define MOD 1000000007
#define INF 2000000000
#define BINF 20000000000000000LL
#define trace(x)                 cerr << #x << ": " << x << endl;
#define trace1(x)                cerr << #x << ": " << x << endl;
#define trace2(x, y)             cerr << #x << ": " << x << " | " << #y << ": " << y << endl;
#define trace3(x, y, z)          cerr << #x << ": " << x << " | " << #y << ": " << y << " | " << #z << ": " << z << endl;
#define trace4(a, b, c, d)       cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << endl;
#define trace5(a, b, c, d, e)    cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << endl;
#define trace6(a, b, c, d, e, f) cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << " | " << #f << ": " << f << endl;
typedef long long ll;
typedef long double ld;
typedef pair<ll,ll> pl;
const ld PI = acos(-1.0);

string ans;
set<pair<int, char>> countChars;
int counts[256];

bool fillRemaining(char c, int cnt)
{
	for(int i = 0; i < ans.size()-1; ++i)
	{
		int ni = i+1;
		if(ans[i] != c && ans[i+1] != c)
		{
			if(cnt)
			{
				--cnt;
				ans = ans.substr(0,i+1) + c + ans.substr(i+1,ans.size()-i-1);
				if(cnt == 0)
					break;
				//++i;
			}
			else
				break;
		}
	}
	if(cnt)
	{
		if(ans[0] != c && ans[ans.size()-1] != c)
		{
			ans += c;
			--cnt;
		}
	}

	if(cnt)
		return false;

	return true;
}

int main()
{
	fastScan;
	int T,N,i,l,R,O,Y,G,B,V;
	cin >> T;
	for(l = 1; l <= T; ++l)
	{
		cin >> N >> R >> O >> Y >> G >> B >> V;
		countChars.insert(mp(R,'R'));
		//countChars.insert(mp(O,'O'));
		countChars.insert(mp(Y,'Y'));
		//countChars.insert(mp(G,'G'));
		countChars.insert(mp(B,'B'));
		//countChars.insert(mp(V,'V'));
		counts['R'] = R;
		counts['O'] = O;
		counts['Y'] = Y;
		counts['G'] = G;
		counts['B'] = B;
		counts['V'] = V;

		int sind = 2500, eind = 2500;
		char cmax,cmed,cmin;
		cmin = countChars.begin()->second;
		countChars.erase(countChars.begin());
		cmed = countChars.begin()->second;
		countChars.erase(countChars.begin());
		cmax = countChars.begin()->second;
		countChars.erase(countChars.begin());

		//trace3(cmax,cmed,cmin);

		ans = "";
		while(counts[cmin])
		{
			ans += cmax;
			ans += cmin;
			counts[cmax]--;
			counts[cmin]--;
		}

		while(counts[cmax] && counts[cmed])
		{
			ans = cmed+ans;
			ans = cmax+ans;
			counts[cmed]--;
			counts[cmax]--;
		}

		if(counts[cmax])
		{
			cout << "Case #" << l << ": " << "IMPOSSIBLE" << endl;
			continue;
		}
		//trace3(ans, cmed, counts[cmed]);
		if(fillRemaining(cmed, counts[cmed]))
			cout << "Case #" << l << ": " << ans << endl;
		else
			cout << "Case #" << l << ": " << "IMPOSSIBLE" << endl;
	}
	
	return 0;
}