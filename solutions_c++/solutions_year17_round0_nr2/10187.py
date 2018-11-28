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
freopen("B-small-attempt0.in","r",stdin);
freopen("SOLUTION_GOOGLE_JAM_Q1.txt","w",stdout);
int t ;
cin >> t;
for ( int j = 0 ; j < t ; ++ j ){
    string s;
    cin >> s;
    int z = s.length() ;
    for ( int i = 1 ; i < z   ; ++ i ){
            if ( i <= 0 ) i = 1 ;
           // cout << s[i] << " " << s[i-1] << endl;
            if ( (s[i]-'0') < (s[i-1]-'0')  ) {
                s[i-1] = ( (s[i-1]-'0') - 1 ) + '0' ;
                for ( int k = i ; k < z ; ++k ){
                  //  cout << s << endl;
                    s[k] = '9' ;
                }
                z = i ;
                i-= 2;
            }

    }
    if (s[0] == '0')  {
        s[0] = '9' ;
    s.pop_back();

    }

    printf ("Case #%d: " , j+1 );
    cout << s << endl;
    }
}
