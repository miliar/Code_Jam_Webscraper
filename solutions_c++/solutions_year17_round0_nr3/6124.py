#include <bits/stdc++.h>

#define mp make_pair
#define ll long long
using namespace std;

vector<vector<int> > vv;
bool visited[100005];

string getss(int n)
{
    string s = "";
    for(int i = 0 ; i < n ; i++)
    {
        s+='+';
    }
    return s;
}

string getss2(int n)
{
    string s = "";
    for(int i = 0 ; i < n ; i++)
    {
        bool flag = rand()%2;
        if(flag ) s+='+';
        else s+='-';
    }
    return s;
}
int main()
{
    freopen("test.txt" , "r", stdin);
    freopen("test2.txt","w", stdout);
    int tt;
    cin >> tt;
    int a = 1;
    while(a<=tt)
    {
        ll n , k;
        cin >> n >> k;
        ll L , R ;
        L = 0 , R = n+1;
        priority_queue<pair<ll,pair<ll,ll> > >qs;
        qs.push(mp(R-L,mp(L,R)));
        int mx , mn;
        while(k>0)
        {
            pair<ll,pair<ll,ll> > tmp = qs.top();
            qs.pop();
            ll l = tmp.second.first , r = tmp.second.second;
            ll stal = (r+l)/2;
            qs.push(mp(stal-l-1, mp(l,stal)));
            qs.push(mp(r-stal-1, mp(stal,r)));
            mn = min(r-stal-1 , stal-l-1);
            mx = max(r-stal-1, stal-l-1);
            k--;
        }
        cout << "Case #" << a++ <<": " << mx << " " << mn << endl;
    }
}
