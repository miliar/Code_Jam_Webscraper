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


	freopen("C-small-2-attempt0.in", "r", stdin);
	freopen("C-small-2-attempt0.out", "w", stdout);
	
	int t, tc, idx, N;
	ll n, k, tp, f, s;
	stack <ll> st;
	priority_queue<ll> pq;
	
	cin >> t;
	tc = 1;
	
	while(t--)  {
	    pq = priority_queue <ll>();
	    cin >> n >> k;
	    pq.push(n);
	    for(int i = 0 ; i < k ; i++){
	       tp =  pq.top();
	       pq.pop();
	       
	       if(tp&1){
	           pq.push(tp/2);
	           pq.push(tp/2);
	           f = s = tp / 2;
	       }
	       else{
	           pq.push(tp/2);
	           pq.push(tp/2 - 1);
	           f = tp / 2;
	           s = tp/2 - 1;
	       }
	        
	    }
	     
	    ll cmp = 0;
	    
	    
	        cout << "Case #"<< tc++ <<": " << f << " " << s<< "\n";
	    
	    
	}
	
	return 0;
}
