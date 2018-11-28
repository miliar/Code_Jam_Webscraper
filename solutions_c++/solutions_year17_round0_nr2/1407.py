#include <bits/stdc++.h>
#define fori(_i,_x) for (int _i = 0; _i < _x; ++_i)
#define fora(_i,_a,_b) for (int _i = _a; _i <= _b; ++_i)
#define forb(_i,_b,_a) for (int _i = _b; _i >= _a; --_i)
#define ll long long
#define inf 1000000000
#define vi vector<int>
#define vvi vector<vector<int> >
#define vl vector<long long>
#define pi pair<int,int>
#define vpi vector<pair<int,int> >
#define vpl vector<pair<long long, long long> >
#define pl pair<long long, long long>
#define fi first
#define sc second
#define pb push_back

using namespace std;

int t;
string s;

int main() {
    
    cin >> t;
    fora(testcase,1,t) {
        
        cin >> s;
        int n = s.size();
        
        cout << "Case #" << testcase << ": ";
        
        int k = 0;
        while (k < n-1 && s[k+1] >= s[k]) ++k;
        
        if (k == n-1) {
            cout << s << endl;
            continue;
        }
        
        while (k > 0 && s[k-1] == s[k]) --k;
        
        if (k == 0 && s[0] == '1') {
            fora(i,1,n-1) cout << '9';
            cout << endl;
            continue;
        }
        
        fori(i,k) cout << s[i];
        cout << (char)(s[k]-1);
        fora(i,k+1,n-1) cout << '9';    
        cout << endl;
    }
    
	return 0;
}

