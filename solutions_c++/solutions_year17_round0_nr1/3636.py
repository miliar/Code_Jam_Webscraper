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
#define N 30000
#define fi first
#define se second
#define mp make_pair
#define gc getchar_unlocked
#define mod 1000000007

typedef long long int ll;
typedef pair<ll, ll > pi;
typedef pair<ll, pi > pii;

int find(string s)  {
    
    for(int i = 0 ; i < s.length() ; i++)   {
        if(s[i] == '-')
            return i;
    }
    return -1;
}

int main() {


	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	
	int t, k, f, tc, turn;
	string s;
	
	cin >> t;
	tc = 1;
	
	while(t--)  {
	    
	    cin >> s >> k;
	    int idx = find(s);
	    turn = 0;
	    f = 1;
	    
	    while(idx != -1)    {
	        
	        if(idx + k > s.length())
	        {
	            f = 0;
	            break;
	        }
	            
	        
	        for(int i = idx ; i < idx + k && i < s.length() ; i++)    {
	            
	            if(s[i] == '-') s[i] = '+';
	            else            s[i] = '-';
	        }
	        turn++;
	        idx = find(s);
	        
	    }
	    cout << "Case #"<< tc++ << ": ";
	    if(f)
	        cout << turn << "\n";
	    else
	        cout << "IMPOSSIBLE\n";
	    
	    
	}
	
	return 0;
}
