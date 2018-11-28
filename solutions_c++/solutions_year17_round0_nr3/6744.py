#include <bits/stdc++.h>

using namespace std;

#define all(v)              ((v).begin()), ((v).end())
#define sz(v)               ((int)((v).size()))
#define cin_int(x)			scanf("%d",&x)
#define cin_char(x)			scanf("%c",&x)
#define cout_int(x)			printf("%d",x)
#define cout_int_ln(x)		printf("%d\n",x)
#define cout_char(x)		printf("%c",x)
#define cout_char_ln(x)		printf("%c\n",x)
#define clr(v, d)           memset(v, d, sizeof(v))
#define rep(i, v)       for(int i=0;i<sz(v);++i)
#define lp(i, n)        for(int i=0;i<(int)(n);++i)
#define lpi(i, j, n)    for(int i=(j);i<(int)(n);++i)
#define lpd(i, j, n)    for(int i=(j);i>=(int)(n);--i)

typedef long long         ll;
const ll OO = 1e8;

#define pb                  push_back
#define MP                  make_pair
#define P(x)                cout<<#x<<" = { "<<x<<" }\n"
typedef long double       ld;
typedef vector<int>       vi;
typedef vector<double>    vd;
typedef vector< vi >      vvi;
typedef vector< vd >      vvd;
typedef vector<string>    vs;

int main() {

    #ifndef ONLINE_JUDGE
        freopen("C-small-1-attempt1.in", "rt", stdin);
        freopen("output4.txt", "wt", stdout);
    #endif // ONLINE_JUDGE

    priority_queue<int> q;
	int n,k,T;
	int a,b;
	cin >> T;
	for (int x = 0; x < T; ++x)
	{
		cin >> n;
	q.push(n);
	cin >> k;
	while(k--) {
		if(!(n&1)) // even
	   		a = n/2,b = (n/2)-1;
		else
	   		a = b = n/2;

	    q.pop();
	    q.push(a),q.push(b);
	    n = q.top();
	}
	q = priority_queue <int>(); // reset
	cout << "Case #" << x+1 << ": " << max(a,b) << " " << min(a,b) << endl;
	}

	/*#ifndef ONLINE_JUDGE
	cout << "\n\n\n" << fixed << "TIME: " << clock() / (CLOCKS_PER_SEC*1.0) << " s" << endl;
    #endif //Time*/

return 0;
}
