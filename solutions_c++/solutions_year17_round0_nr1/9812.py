using namespace std;
#include <bits/stdc++.h>
#define PI 3.14159265
typedef long long ll;
typedef pair<int, int> ii; // pair ii
typedef vector<ii> vii;  // vector of pairs of ii
typedef vector<int> vi; //vector
typedef long long ll;
#define INF 1000000000

int main(){
freopen("A-small-attempt0.in","r",stdin);
freopen("SOLUTION_GOOGLE_JAM_Q2.txt","w",stdout);
int t ;
cin >> t;
for ( int j = 0 ; j < t ; ++ j ){
    string s;
    cin  >> s;
    int n ;
    cin >> n ;
    int cc = 0 ;
    int imp = 0 ;
    for ( int i = 0 ; i < s.length() ; ++i ){
           // cout << i << " " << s << endl;
        if (s[i] == '-'){
            if ( (s.length()-i) >= n ) {
                for ( int k = 0  ; k < n ; ++ k ){
                    if (s[i+k] == '+') s[k+i] = '-' ;
                    else s[i+k] = '+';
                    //cout << s << endl;
                    }
                cc ++ ;
            }
            else {imp = 1;}
        }
    }
    if (imp) cout << "Case #"<<  j+1 << ": IMPOSSIBLE" << endl;
    else cout << "Case #"<<  j+1 << ": " << cc << endl;
}
}
