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
        string a , lop;

        llu o , len;        
        cin >> a >> o;
        len = a.length();

        llu ans = 0 , q;
        
        while (count(all(a) , '+') < len)
        {
            q = a.find("-");
            if (q > len - o)
            {
                cout << "Case #"<<testTrack<<": IMPOSSIBLE"<< endl;
                break;
            }
            lop = "";
            ans++;
            for (llu i = q; i < q+o; i += 1)
            {
                lop += (a[i] == '-') ? '+' : '-';
            }
            a = a.substr(0,q) + lop + a.substr(q+o);         
        }
        if(count(all(a) , '+') == len)
        {
            cout << "Case #"<<testTrack<<": " <<ans<<endl;
        }

    }
    return 0;
}

















