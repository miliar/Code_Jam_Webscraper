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
string str;
 
bool flip1(int start,int k,int len){
    if(start+k > len)
        return false;
    fl(i,start,start+k){
        if(str[i] == '-')
            str[i] = '+' ;
        else
            str[i] = '-' ;
    }
    return true ;
}
 
int main(){
    c_false ;
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
   // std::cout << std::fixed << std::showpoint;
  //  std::cout << std::setprecision(6);
    int t ;
    cin >> t ;
    while(t--){
        pcase ;
        int k ;
        cin >> str >> k ;
        int len = str.length() ;
        int ans = 0 ;
        fl(i,0,len){
            if(str[i] == '-'){
                ++ans ;
                bool check = flip1(i+1,k-1,len) ;
                if(!check){
                    ans = nmax ;
                    break;
                }
            }
        }
        if(ans == nmax)
            cout << "IMPOSSIBLE\n" ;
        else
            cout << ans << "\n";
    }
    return 0;
}