/**
*	
*	BY : Rajan Parmar
*/
#include <iostream>
#include <string>
#include <cmath>
#include <time.h>
#include <cstdio>
#include <iomanip>
#include <vector>
#include <map>
#include <algorithm>
#include <memory.h>
#include <stack>
#include <queue>
using namespace std;
//#pragma warning(disable:4996)
//#define N 30000
#define fi first
#define se second
#define mp make_pair
#define gc getchar_unlocked
#define mod 1000000007

typedef long long int ll;
typedef pair<ll, ll > pi;
typedef pair<ll, pi > pii;


int main() {


	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int t, tc;
    ll  d, n, k, s;
    long double tm, temp, ans;
	tc = 1;
	cin >> t;
	while(t--)  {
	    
	        cin >> d >> n;
	        tm = 0.0;
	        while(n--)  {
	         
	            cin >> k >> s;
	            temp = ( (d - k) * 1.0 ) / s ; 
	            tm = max(tm, temp);
	            
	        }
	        ans = d / tm;
	        cout << "Case #"<< tc++ <<": " << fixed <<setprecision(6)<< ans << "\n";
	}
	
	return 0;
}
