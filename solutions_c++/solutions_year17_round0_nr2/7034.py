#include <bits/stdc++.h>

#define nl cout << "\n" 
#define pb(a) push_back(a)
#define mp(a,b) make_pair(a,b)
#define ll long long
#define fi first
#define se second

#define fl(i,a,b) for(int i=a;i<b;++i)
#define flr(i,a,b) for(int i=a;i>=b;--i)
#define all(a) a.begin(),a.end()

#define pii pair<int,int> 
#define vi vector<int> 
#define vll vector<ll>
#define vb vector<bool>
#define vpii vector<pair<int,int> > 
#define vpib vector<pair<int,bool> >
#define vvi vector<vector<int> >

#define DEBUG(x) cout << "value of " << #x << " is " << x << "\n"
#define DEBUG2(x,y) cout << "value of " << #x << " is " << x << "\tvalue of " << #y << " is " << y << "\n"
#define DEBUG3(x,y,z) cout << "value of " << #x << " is " << x << "\tvalue of " << #y << " is " << y << "\tvalue of " << #z << " is " << z << "\n"
#define c_false ios_base::sync_with_stdio(false); cin.tie(0)

//  apac macros section 
int tcase = 1 ;
#define pcase cout << "Case #" << tcase++ << ": " 

const int mod = 1000000007;
const ll lmod = 1000000000000000007 ;
const int nmax = INT_MAX;
const int nmin = INT_MIN;


using namespace std;

int main(){
    c_false ;
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
   // std::cout << std::fixed << std::showpoint;
  //  std::cout << std::setprecision(6);
    // srand ( time(NULL) );
    int t ;
    cin >> t ;
    while(t--){
        pcase ;
        string str ;
        cin >> str ;
        int len = str.length() ;
        int last = len ;
        for(int i= len-1;i>0;--i) {
            if(str[i] < str[i-1]){
                --str[i-1];
                last = i ;
            }
        }
        fl(i,last,len)
            str[i] = '9' ;
        if(str[0] == '0')
            str = str.substr(1) ;
        cout << str << "\n" ;
       }
    return 0;
}
