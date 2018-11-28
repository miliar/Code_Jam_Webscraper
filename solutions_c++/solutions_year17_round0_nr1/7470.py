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

bool isValid(string str){
    int i;
    fi(0,str.size()) if(str[i] == '-') return false;
    return true;
}

int main(){ 
    ll t,ti,n,k,i,j,ans,flag,imFlag = 0;
    SLL(t);
    for(ti = 1; ti <= t; ti++){
        imFlag = 0;
        string str,temp;
        ans = 0;
        flag = 1;
        cin>>str>>k;
        map<string,int> mp;
        mp[str] = 1;
        while(!isValid(str)){
            for(i = 0; i < str.size(); i++){
                if(str[i] == '-' && i + k <= str.size()){
                    temp = "";
                    for(j = 0; j < i; j++){
                        temp += str[j];  
                    }
                    for(j = i; j < (i + k); j++){
                        if(str[j] == '+') temp += '-';
                        else if(str[j] == '-') temp += '+';
                    }
                    for(j = (i+k); j < str.size(); j++){
                        temp += str[j];
                    }
                    str = temp;
                    ans++;
                }
            }
            if(mp.find(str) != mp.end()){
                imFlag = 1;
                break;
            }else{
                mp[str] = 1;
            }
        }
        if(imFlag) cout<<"Case #"<<ti<<": "<<"IMPOSSIBLE"<<endl;
        else cout<<"Case #"<<ti<<": "<<ans<<endl;
        
    }
    return 0;
}