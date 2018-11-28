#include <iostream>
#include<fstream>
#include<vector>
#include<string>
#include<cstring>
#include<set>
#include<stack>
#include<queue>
#include<cmath>
#include<algorithm>
#include<cstdio>
#include<cstdlib>
#include<utility>
#include<map>
#include<functional>
#define rep(i,l,r) for(long long int i=l;i<r;i++)
#define down(i,l,r) for(long long int i=l;i>r;i--)
#define pb(x) push_back(x)
#define mp(a,b) make_pair(a,b)
#define ll long long
#define pii pair<int,int>
using namespace std;

struct wash
{
    ll int st;
    ll int en;
    ll int mid;
    ll int l;
    ll int r;
    friend bool operator<(wash a, wash b)
    {
        if(min(a.l,a.r)>min(b.l,b.r))
        {
            return false;
        }
        if(min(a.l,a.r)<min(b.l,b.r))
        {
            return true;
        }
        if(max(a.l,a.r)>max(b.l,b.r))
        {
            return false;
        }
        if(max(a.l,a.r)<max(b.l,b.r))
        {
            return true;
        }
        if(a.mid<b.mid)
        {
            return false;
        }
        else
        {
            return true;
        }
    }

};




int main()
{
    ios_base::sync_with_stdio(false);
    ll int h;
    fstream ci,co;
    ci.open("C-small-2-attempt0.in",ios::in|ios::binary);
    co.open("cout.txt",ios::out);
    ci>>h;
    rep(t,1,h+1)
    {
        ll int n,k;
        ci>>n>>k;
        priority_queue<wash> q;
        wash w;
        w.st=0;w.en=n-1;w.mid=(w.st+w.en)/2;w.l=w.mid-w.st;w.r=w.en-w.mid;
        q.push(w);
        wash last;
        rep(i,0,k)
        {
            wash a;
            a=q.top();
            q.pop();
            last=a;
            wash b,c;
            b=a;
            c=a;
            b.en=a.mid-1;b.mid=(b.st+b.en)/2;b.l=b.mid-b.st;b.r=b.en-b.mid;
            c.st=a.mid+1;c.mid=(c.st+c.en)/2;c.l=c.mid-c.st;c.r=c.en-c.mid;

            if(b.st<=b.en && b.st>=0)
            {
                q.push(b);
            }
            if(c.st<=c.en && c.st>=0)
            {
                q.push(c);
            }
        }
        co<<"Case #"<<t<<": "<<max(last.l,last.r)<<" "<<min(last.l,last.r)<<endl;
    }

}
