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

ll left(vector<bool> stall , ll index)
{
    for (ll i = index; i >= 0; i -= 1)
    {
        if(stall[i] == true)
            return i;
    }
    return 0;
}


ll right(vector<bool> stall , ll index , ll size)
{
    for (ll i = index; i < size; i += 1)
    {
        if(stall[i] == true)
            return i;
    }
    return 0;
}
int main (int argc, char const* argv[]){
    llu testCases;
    cin>>testCases;
    llu testTrack = 0;
    while((++testTrack) <= testCases)
    {
        int n , k;
        cin >> n >> k;
        vector<bool> stall (n+2 , false);
        
        stall[0] = true;
        stall[n+1] = true;
        
        int templs , temprs , ls , rs;
        rep(j , 1 , k)
        {
                vector <int> minterm(n+2 , INT_MIN);
                vector <int> maxterm(n+2 , INT_MAX);
                
                rep(i , 1 , n)
                {
                    if(stall[i] == false)
                    {
                        templs = i - left(stall , i-1) - 1;
                        temprs = right(stall , i+1 , n+2) - i - 1;
                        minterm[i] = min(templs , temprs);
                        maxterm[i] = max(templs , temprs);
                    }
                }

                auto minty = max_element(all(minterm));
                ls = *minty;
                
                if(count(all(minterm) , *minty) == 1)
                {
                    stall[minty-minterm.begin()] = true;
                    rs = maxterm[minty-minterm.begin()];
                }
                else
                {
                    int temp = minty-minterm.begin();
                    rep(i , 1 , n)
                    {
                        if(minterm[i] == *(minty))
                        {
                            if(maxterm[temp] < maxterm[i])
                                temp = i;
                        }
                    }
                    stall[temp] = true;
                    rs = maxterm[temp];
                }
            }
        cout << "Case #"<<testTrack<< ": " << max(ls,rs) << " " << min(ls,rs) << endl;
        
    }
    return 0;
}

















