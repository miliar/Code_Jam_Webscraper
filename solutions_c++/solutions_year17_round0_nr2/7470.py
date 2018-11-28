/******************************************************************************************************************
    Author: Saurabh Banore(sierra_bravo)
******************************************************************************************************************/

#include <algorithm>
#include <iostream>
#include <iterator>
#include <numeric>
#include <sstream>
#include <fstream>
#include <cassert>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cstdio>
#include <vector>
#include <bitset>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <map>
#include <set>
using namespace std;
typedef long long ll;
typedef pair<int,int> ii;
typedef pair<ll,ll> pll;
typedef pair<string,int> si;
typedef pair<int,ii> iii;
typedef vector <si> vsi;
typedef vector <ii> vii;
typedef vector <int> vi;
typedef vector <ll> vll;
typedef vector <char> vc;
typedef vector <string> vs;
typedef map <string,vs> msvs;
typedef map <string,int> msi;
typedef map <string,string> mss;
#define SLL(a) scanf("%lld",&a)
#define PLL(a) printf("%lld\n",a)
#define MAX(a,b) (a > b) ? a : b
#define MIN(a,b) (a < b) ? a : b
#define fi(a,b) for(i = a;i < b;i++)
#define fi2(a,b) for(j = a;j < b;j++)
#define fd(a,b) for(i = a;i >= b; i--)
#define pb push_back
#define mp make_pair
#define INF 1000000000
template<typename T> inline T lcm(T a, T b){ return (a*b)/gcd(a,b);}
template<typename T> inline T gcd(T a,T b){ if(a < b) return (b,a); T r = a % b; if(r == 0) return b; return gcd(r,b);}

/*=======================================================================================================
//The matrix stuff
bool isValid(ll x,ll y,ll n, ll m){
    return (x >= 0 && x < n) && (y >= 0 && y < m);
}
int dx[] = {-1,-1,-1,0,0,1,1,1};
int dy[] = {-1,0,1,-1,1,-1,0,1};
===========================================================================================================*/  

 

int main(){
    ll t,n,k,i,j,ti,flag,temp;
    SLL(t);
    for(ti = 1; ti <= t; ti++){
        SLL(n);
        flag = 1;
        string s = to_string(n);
        while(flag){
            flag = 0;
            temp = 1;
            for(i = s.size()-1; i > 0 && s.size() > 1; i--){
                if(s[i] < s[i-1]){
                    n = (n - (n % static_cast<long long> (pow(10,temp)))) - 1;
                    s = to_string(n);
                    flag++;
                }
                temp++;
            }
        }
        cout<<"Case #"<<ti<<": "<<s<<endl;
    }
    return 0;
}