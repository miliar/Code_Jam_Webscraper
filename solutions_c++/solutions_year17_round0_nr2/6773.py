//Jai Shree Krishna
#include <vector>
#include <list>
#include <map>
#include <set>
#include "queue"
#include <deque>
#include <stack>
#include <numeric>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <complex>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <climits>
#include <cassert>
#include <iostream>
#include "fstream"
using namespace std;
#define PI acos(-1)
#define MOD (ll)1000000007
#define pii pair<long long ,long long >
#define ll  long long int
#define loop(i,n) for(ll i=0;i<n;i++)
#define loop2(i,n) for(ll i = 1;i<=n;i+=1)
#define pb push_back
#define mp make_pair
#define EPS 1e-8
void display(vector<int> v1){loop(i,v1.size()){cout<<v1[i]<<" ";}cout<<endl;}
ll dx[8] = {0,1,0,-1,1,1,-1,-1};
ll dy[8] = {1,0,-1,0,1,-1,1,-1};

//Never giving in, fighting to the end
bool check(ll x)
{
    string s;
    s = to_string(x);
    for(ll j = 1;j<s.length();j+=1)
    {
        if(s[j]<s[j-1])
            return false;
    }
    return true;
}



int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    freopen("/Users/ashish/Desktop/B-small-attempt0.in.txt", "r", stdin);
    freopen("/Users/ashish/Desktop/A-large-practice.out.txt", "w", stdout);

    
    ll t;
    cin>>t;
    loop2(y, t){
        cout<<"Case #"<<y<<": ";
        
        ll n;
        cin>>n;
        ll ans = -1;
        for(ll j = n;j>=1;j-=1)
        {
            if(check(j))
            {
                ans = j;
                break;
            }
        }
        cout<<ans<<endl;
    }
    
    
    
    

    return 0;
}
