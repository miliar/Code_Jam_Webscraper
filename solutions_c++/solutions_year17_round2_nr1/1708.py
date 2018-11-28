//Aditya Agrawal
// DTU


#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
#include <list>
#include <utility>
#include <iterator>
#include <map>
#include <stack>
#include <queue>
#include <set>
#include <deque>
#include <bitset>
#include <complex>
//#include <unordered_set>
//#include <unordered_map>


#define mod 1000000007
#define ima 1000000004
#define imi -1000000004
#define llma 1000000000000000004
#define llmi -1000000000000000004
#define lp(i,n) for(i=0;i<n;i++)
#define li(i,n) for(i=n-1;i>=0;i--)
#define tree vector<list<int > >
#define ll long long int
#define ld long double
#define f first
#define s second
#define pa pair<ll,ll>
#define pad pair<double ,double>
#define pai pair<int,int>
#define mp make_pair
#define nn 500005
#define pi 3.1415926535898
#define inf 1e35
#define diff 1e-7
#define md 359999
#define it ::iterator
#define pb push_back
#define sync ios::sync_with_stdio(false);cout.tie(0);cin.tie(0);

using namespace std;

typedef complex<double> base;



int main()
{
    sync
    int t;
    cin>>t;
    double s,time;
    ll k,d;
    int n,i;
    int j=0;
    while(t--)
    {
        cin>>d>>n;
        j++;
        time=0;
        for(i=0;i<n;i++)
        {
            cin>>k>>s;
            time=max(time,(d-k)/s);
        }
        cout<<"Case #"<<j<<": ";
        printf("%.7lf\n",d/time);
        
    }
    
}

