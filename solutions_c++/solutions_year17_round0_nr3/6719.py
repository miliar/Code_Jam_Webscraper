// ============================================================================
// Name        : Test.cpp
// Author      : Taha Mostafa
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
// ============================================================================

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
 
const double EPS = (1e-7);
int dcmp(double x, double y) {  return fabs(x-y) <= EPS ? 0 : x < y ? -1 : 1; }
 
#define pb                  push_back
#define MP                  make_pair
#define P(x)                cout<<#x<<" = { "<<x<<" }\n"
typedef long double       ld;
typedef vector<int>       vi;
typedef vector<double>    vd;
typedef vector< vi >      vvi;
typedef vector< vd >      vvd;
typedef vector<string>    vs;

int n,k;
// int dis[22][22],x[22],y[22];
// int memo[11][1 << 11];
// int shops[10004];
// int memo[10004];

// bool valid(int x)
// {
// 	return (x >= 0  && x < n );
// }
// int solve(int x,int start)
// {
// 	if(!valid(x))
// 		return 50007;
// 	memo[x] = 1;
// 	if(x == n-1)
// 		return 0;
			
// 	if(memo[x] != -1)
// 		return 50007;
//  	cout << x+shops[x] << " " << x-shops[x] << endl;
// 	return  1+ min(solve(x+shops[x],start),solve(x-shops[x],start));
	 
// }
// int tsp(int pos,int bm)
// {
// 	int &m = memo[pos][bm];
// 	if( bm == (1 << n+1)-1 ) // in the end pos 
// 	return dis[pos][0];  // return to the first node
// 	if(m != -1)
// 		return m;
// 	int ans = INT_MAX;
// 	for (int nxt = 0; nxt <= n; nxt++)
// 	if(nxt != pos && !(bm &(1<<nxt)))
// 		ans = min(ans,dis[pos][nxt]+tsp(nxt,bm | (1<<nxt)));
// 	return m = ans;

// }


int main() {

	
	freopen("input_here.in", "rt", stdin);
	freopen("output_here.out", "wt", stdout);
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
	
	// int T;
	// cin >> T;
	// while(T--) {
	//    cin >> n;
	//    memset(memo,-1,sizeof memo);
	//    for (int i = 0; i < n; ++i)
	//    {

	//    	cin >> shops[i];
	//    	// if(valid(i,i+shops[i]))
	//    	//  	maze[i][i+shops[i]] = 1;
	//    	// if(valid(i,abs(i-shops[i])))
	//    	// 	maze[i][abs(i-shops[i])] = 1;
	   	
	//    }
	   
	//    	cout << solve(0,0) << endl;
	   
	// }

return 0;
}
