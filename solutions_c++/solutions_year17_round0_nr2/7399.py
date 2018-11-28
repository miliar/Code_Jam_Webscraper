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
#include <unordered_set>
#include <unordered_map>


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
#define nn 100005
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
    int t;
    cin>>t;
    string n;
    int l;
    int f=0;
    int i;
    int j;
    int flag;
    while(t--)
    {
        f++;
        cin>>n;
        cout<<"Case #"<<f<<": ";
        l=n.length();
        flag=0;
        for(i=0;i<l-1;i++)
        {
            if(n[i+1]<n[i])
            {
                while(n[i]-1<n[i-1] && i>=0)
                    i--;
                
                if(i==0 && n[i]=='1')
                {
                    flag=1;
                }
                else
                    n[i]--;
                
                for(;i<l-1;i++)
                {
                    n[i+1]='9';
                }
                break;
            }
        }
        
        if(flag)
        {
            for(i=1;i<l;i++)
                cout<<n[i];
            cout<<endl;
        }
        else
        {
            for(i=0;i<l;i++)
                cout<<n[i];
            cout<<endl;
        }
        
    }
}


