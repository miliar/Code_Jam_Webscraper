#include <iostream>
#include <algorithm>
#include <fstream>
#include <vector>
#include <deque>
#include <assert.h>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <stdio.h>
#include <string.h>
#include <utility>
#include <math.h>
#include <bitset>
#include <iomanip>

using namespace std;

#define F(i , a , b) for(int (i) = (a) ; (i) <= (b) ; (i)++)
#define pb push_back
#define ll long long
#define E(a) cerr << #a << " = " << a << '\n'
#define X first
#define Y second
#define INF 10000000000000
#define int long long
#define PI acos(-1)
const int MAX_N = 1000 + 10 , mod = 1000000007;

void solve(){
	pair<pair<int,int>,int> p[MAX_N];
	int n , k , mx=0;
	cin>>n>>k;
	for(int i =0 ;i<n ;i++){
		cin >> p[i].Y >> p[i].X.Y ; //   X=H , Y=R
		p[i].X.X = p[i].Y * p[i].X.Y;
	}
	sort(p,p+n);
	int ans = 0 , tmp , tmp2 , ss =-10000000000000000;
	for(int i = n-1,j=1 ; j <=k-1 ; j++,i--){
		ans += 2*p[i].X.Y*p[i].Y;
		mx = max(mx,p[i].Y);
	}
	ans +=  mx * mx;
	for(int i =0 ; i<=n-k  ; i++){
		tmp = 2*p[i].X.Y*p[i].Y;
		ss = max(ss ,tmp + max(mx,p[i].Y)*max(mx,p[i].Y)- mx*mx);
	}
	ans += ss;
	cout<< (long double)1.0 * ans*PI << endl;

}
void clr(){

}

int32_t main(){
    
       freopen("input.txt" , "r" , stdin);
      freopen("output.txt" , "w" , stdout);
        cout << setprecision(6) << fixed;
    ios::sync_with_stdio(0); cin.tie() ; cout.tie();

    int T ; cin >> T;
    for(int _ = 1 ; _ <= T ; _++){
    	clr();
    	cout << "Case #" << _ << ": ";
    	solve();
    }
    
    
    return 0;
}
