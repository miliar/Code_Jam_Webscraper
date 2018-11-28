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
    freopen("/Users/ashish/Desktop/C-small-2-attempt0.in.txt", "r", stdin);
    freopen("/Users/ashish/Desktop/A-large-practice.out.txt", "w", stdout);

    int t;
    cin >> t;
    for (int k1 = 1; k1 <= t; k1++) {
        priority_queue<int>q1;
        int n,k,x,mx=0,mn=0;
        cin>>n>>k;
        q1.push(n);
        for(int i=0;i<k;i++){
            x=q1.top();
            q1.pop();
            if(x==0){
                mx=0;
                mn=0;
                break;
            }
            q1.push((int)floor((double)(x-1)/2));
            q1.push((int)ceil((double)(x-1)/2));
            mx=(int)ceil((double)(x-1)/2);
            mn=(int)floor((double)(x-1)/2);
        }
        cout<<"Case #"<<k1<<": "<<mx<<" "<<mn<<endl;
    }

    
    
    

    return 0;
}
