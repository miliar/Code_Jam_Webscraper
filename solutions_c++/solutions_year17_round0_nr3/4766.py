#include <bits/stdc++.h>
#define F first
#define S second

using namespace std;

set<pair<int,int> > s;
int n,k;

int main()
{
    freopen("C_small2.in","r",stdin); freopen("C_small2.out","w",stdout);
    int t;
    cin >> t;
    int tc;
    for(tc=1;tc<=t;tc++)
    {
        cin >> n >> k;
        s.clear();
        s.insert({-n,0});
        int mini,maxi;
        while(k--)
        {
            pair<int,int> cur=*(s.begin());
            int sz=(-cur.F)-1;
            pair<int,int> l={-(sz/2),cur.S};
            pair<int,int> r={-(sz/2+sz%2),cur.S+sz/2};
            s.erase(s.begin());
            s.insert(l); s.insert(r);
            mini=sz/2; maxi=sz/2+sz%2;
        }
        cout << "Case #" << tc << ": " << maxi << " " << mini << endl;
    }
}
