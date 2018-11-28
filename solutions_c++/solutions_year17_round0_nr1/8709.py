//----------------------JUGNU:LET YOUR LIGHT SHINE---------------------------//
#include <bits/stdc++.h>
#define ll long long int
#define ld long double
#define pb push_back
#define pf push_front
#define sz size
#define mk make_pair
#define ln length
#define fr(i,a,b) for(i=a;i<b;i++)
#define fre(i,a,b) for(i=a;i<=b;i++)
#define frr(i,a,b) for(i=a;i>=b;i--)
#define sc(a) scanf("%d", &a)
#define sm(a, b) scanf("%d%d", &a, &b)
#define pr(a) printf("%d\n", a)
#define pm(a, b) printf("%d %d\n", a, b)
#define isset(x,i) ((x>>i)&1)
#define MAXN 100005
#define MOD 1000000007LL
#define fastScan ios_base::sync_with_stdio(0); cin.tie(NULL);

#define trace1(x)       cerr << #x << " : " << x << endl;
#define trace2(x, y)    cerr << #x << " : " << x << " | " << #y << " : " << y << endl;
#define trace3(x, y, z) cerr << #x << " : " << x << " | " << #y << " : " << y << " | " << #z << " : " << z << endl;
#define cline cout << "----------------------" << endl;
using namespace std;

string S;

int getFirstIdx(int start){
	for(int i = start; i < S.ln(); i++) if(S[i] == '-') return i;
	return -1;
}

int updateString(int start, int end){
	if(end > ((int)S.ln() - 1)) return 0;
	for(int i = start; i <= end; i++){
		if(S[i] == '+') S[i] = '-';
		else if(S[i] == '-') S[i] = '+';
	}
	return 1;
}


int main()
{
	int i, j, t, n, m, k, l, r, temp, mini, maxi, flag, cnt, test, result = 0;
	fastScan;
	cin >> t;
	fre(test, 1, t){
		cin >> S >> k;
		result = 0;
		n = S.ln();
		temp = getFirstIdx(0);
		while(temp != -1){
			result += updateString(temp, temp + k - 1);
			temp = getFirstIdx(temp + 1);
		} 
		temp = getFirstIdx(0);
		if(temp == -1) cout << "Case #" << test << ": " << result << endl;
		else cout << "Case #" << test << ": " << "IMPOSSIBLE" << endl;
	}

return 0;
}