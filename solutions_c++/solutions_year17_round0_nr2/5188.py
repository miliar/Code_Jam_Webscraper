/******************************************************************************************/
/*                               Harsh Agarwal                                            */                       
/*                   Template taken from Adarsh Pugalia                                   */
/*     https://github.com/adarshpugalia/Competitive-Programming/blob/master/template.cpp  */
/******************************************************************************************/
#include <bits/stdc++.h>

#define ll long long int
#define llu long long int unsigned
#define vi vector <int>
#define vl vector <ll> 
#define pii pair<int, int>
#define pll pair<ll, ll>
#define vpii vector <pii >
#define vpll vector <pll >
 
#define f first
#define s second
#define pb push_back
#define pob pop_back
#define mp make_pair
#define sz(n) (int)n.size()-1
#define all(n) n.begin(), n.end()
#define has(it,s) if(it!=s.end())

#define rep(i,j,k) for(ll i=j; i<=k; i++)
#define repd(i,j,k) for(ll i=j; i>=k; i--)
#define iter(it, s) for(auto it=s.begin(); it!=s.end(); it++)
using namespace std;

int main (int argc, char const* argv[]){
    llu testCases;
    cin>>testCases;
    llu testTrack = 0;
    while((++testTrack) <= testCases){
        string a;
        cin >> a;
        llu len = sz(a) + 1;
        
        if (len == 1)
        {
            cout << "Case #" << testTrack << ": " << a<<endl;
            continue;
        }
        string ans = "";
        ll x = len-1 , y = len-2;
        
        
        
        while(y>=0)
        {
            if(a[x] < a[y]) {
                if (a[y] == '1')
                {
                    if (y == 0)
                        a = string(len-y-1 , '9');
                    else 
                        a =  a.substr(0,y-1) + to_string((a[y-1]-'0')-1) + string(len-y , '9');
                }
                else
                {
                    a = a.substr(0,y) + to_string((a[y]-'0')-1) + string(len-y-1 , '9');    
                }
            }
                x--;
                y--;
        }
        cout << "Case #" << testTrack << ": " << a.substr(a.find_first_not_of("0"))<<endl;
    }
    return 0;
}

















