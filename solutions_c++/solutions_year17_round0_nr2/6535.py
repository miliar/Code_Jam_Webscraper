
//In the name of Allah
#include <bits/stdc++.h>
using namespace std; 


long long solve() { 
    string s;
    cin >> s; 
    int n = s.size();
    long long ret = 0; 
    for( int i = 0 ; i < n ; i++ ) { 
        if( i + 1 < n && s[i] > s[i+1] ) { 
            long long num = 0; 
            int j;
            for( j = 0 ; j < i && s[j] < s[i] ; j++ ) 
                num = num * 10 + s[j] - '0';
            num = num * 10 + s[j] - '0' - 1;
            j++; 
            for(  ; j < n ; j++ ) 
                num = num * 10 + 9;
            return num;
        }
        ret = ret * 10 + s[i] - '0';
    }

    return ret;
}

int main() { 
    int t; 
    cin >> t;
    for( int i = 1 ; i <= t ; i++ ) { 
        long long ret = solve(); 
        cout << "Case #" << i << ": " << ret << endl;
    }

}
