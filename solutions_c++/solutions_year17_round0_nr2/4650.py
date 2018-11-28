// In the name of Allah

#include <set>
#include <map>
#include <cmath>
#include <queue>
#include <stack>
#include <vector>
#include <bitset>
#include <iomanip>
#include <stdio.h>
#include <fstream>
#include <sstream>
#include <complex>
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;

#define dbg(x) cerr << #x << " = " << (x) << endl;
#define FOR(i,a,b) for (int i = (a); i < (b); i ++)
#define rep(i,n) for (int i = 0; i < (n); i ++)
#define repd(i,n) for (int i = (n); i >= 0; i --)
#define PI 3.14159265358979323846
#define pb push_back
#define mp make_pair
#define X first
#define Y second

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;

ofstream fout ("B.out");
const int max_n = 18+2;
string dp [max_n][2];

ll str2int (string s)
{
	stringstream ss;
	ss << s;
	ll res;
	ss >> res;
	return res;
}

string smax (string a, string b)
{
	return (str2int(a) > str2int(b) ? a : b);
}

int main ()
{
    int t;
    cin >> t;
    rep (tt, t)
    {
    	rep (i, max_n)
    		dp [i][0] = dp [i][1] = "-1";

    	string n;
    	cin >> n;

    	dp [0][0] = n[0];
    	dp [0][1] = char(n[0]-1);

    	rep (i, n.size()-1)
    	{
    		if ( dp[i][0] != "-1" )
    		{
	    		if ( n[i] <= n[i+1] )
	    			dp [i+1][0] = dp[i][0] + char(n[i+1]);
	    		if ( n[i] < n[i+1])
	    			dp [i+1][1] = smax (dp[i][0]+char(n[i+1]-1), dp[i+1][1]);

	    	}
	    	if ( dp[i][1] != "-1" )
	    		dp [i+1][1] = smax (dp[i][1]+'9', dp[i+1][1]);
    	}

    	ll ans = str2int (smax(dp[n.size()-1][0], dp[n.size()-1][1]));
    	
    	fout << "Case #" << tt+1 << ": " << ans << endl;
    	//cout << "Case #" << tt+1 << ": " << ans << endl;
    }
    
	return 0;
}