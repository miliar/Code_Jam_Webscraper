/**
*	
*	BY : Rajan Parmar
*/
#include <iostream>
#include <string>
#include <cmath>
#include <time.h>
#include <cstdio>
#include <vector>
#include <map>
#include <algorithm>
#include <memory.h>
using namespace std;
#pragma warning(disable:4996)
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


	freopen("B-large (2).in", "r", stdin);
	freopen("B-large (2).out", "w", stdout);
	
	int t, k, f, tc, idx, N;
	int dig[21];
	ll n, ans;
	string s;
	
	cin >> t;
	tc = 1;
	
	while(t--)  {
	    
	    cin >> n;
	    memset(dig, 0 , sizeof(dig));
	    idx = 20;
	    N = 0;
	    while(n)    {
	        dig[idx--] = n % 10;
	        n /= 10;
	        N++;
	    }
	    idx = 19;
	    for(int i = 1 ; i < N ; i++, idx--)    {
	        
	        if(dig[idx + 1] < dig[idx]) {
	            dig[idx + 1] = 9;
	            dig[idx]--; 
	            
	            for(int j = idx + 1 ; j < 20 ; j++){
	                if(dig[j + 1] <  dig[j])
	                    dig[j + 1] = dig[j];
	            }
	        }
	        
	    }
	    
	    ll mul = 10;
	    ans = 0;
	    for(int i = 0 ; i < 21 ; i++)   {
	        ans = (ans * mul + dig[i]);
	    }
	    
	    cout << "Case #"<< tc++ << ": " << ans << "\n";
	    
	}
	
	return 0;
}
