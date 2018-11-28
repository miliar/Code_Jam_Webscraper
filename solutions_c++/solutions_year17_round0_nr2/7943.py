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

#define pa pair<ll,ll>
#define pad pair<double ,double>
#define pai pair<int,int>
#define mp make_pair
#define nn 100005
#define pi 3.1415926535898
#define inf 1e35
#define md 359999
#define it ::iterator
#define pb push_back
#define sync ios::sync_with_stdio(false);cout.tie(0);cin.tie(0);
using namespace std;


string s;
int main()
{
    int t,i,flag,j,size,g,h;
    cin>>t;
    for(int l=1;l<=t;++l)
    {
        cin>>s;
        i=0;
        cout<<"Case #"<<l<<": ";
        
        flag=0;
        size=s.length();
        
        for(i=0;i<size-1;++i)
        {
            g=s[i]-48;
            h=s[i+1]-48;
            if(g>h)
            {flag=1;
                break;
            }
        }
        
        if(flag==1)
        {
            while(i>0 && s[i]-1<s[i-1])
                i--;
            
            if(i==0 && s[i]=='1')
            {
                for(i=1;i<size;i++)
                    cout<<"9";
            }
            else
            {
                s[i]--;
                i++;
                for(;i<size;i++)
                    s[i]='9';
                cout<<s;
            }
            
            cout<<endl;
        } 
        else
            cout<<s<<endl;
    }
}
