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


int findmax(int ar[], int idx){
    
    int mx = 0;
    int rt;
    
    for(int i = 0 ; i < 6 ; i++){
        if(i == idx)
            continue;
        if(ar[i] > mx){
            mx = ar[i];
            rt = i;
        }
    }
    return rt;
}

int main() {


	freopen("B-small-attempt1 (1).in", "r", stdin);
	freopen("B-small-attempt1 (1).out", "w", stdout);
	int t, tc, idx;
	int uni[10]; // R, O, Y, G, B, and V.
	char ch[] = {'R' , 'O' , 'Y' , 'G', 'B', 'V'};
    ll  d, n, k, s;
    string ans;
    
	tc = 1;
	cin >> t;
	while(t--)  {
	    
	        cin >> n;
	        for(int i = 0 ; i < 6 ; i++){
	            cin >> uni[i];
	        }
	        ans = "";
	        
	        idx = findmax(uni, -1);
	        
	        if(uni[idx] > n / 2)
	        {
	            cout << "Case #"<< tc++ <<": " << "IMPOSSIBLE" << "\n";
	            continue;
	        }
	        
	        ans = ans + ch[idx];
	        uni[idx]--;
	        
	        for(int i = 1 ; i < n; i++){
	            //cout << "idx :" << idx << "\n";
	            idx = findmax(uni, -1);
	            if(ans[i - 1] == ch[idx] ){
	                idx = findmax(uni, idx);
	            }
	            ans = ans + ch[idx];
	            uni[idx]--;
	        }
			
			if(ans[0] == ans[n - 1]){
				char tmp;
				tmp = ans[n - 1];
				ans[n - 1] = ans[n - 2];
				ans[n - 2] = tmp;
			}
	        
	        cout << "Case #"<< tc++ <<": "<< ans << "\n";
	}
	
	return 0;
}
