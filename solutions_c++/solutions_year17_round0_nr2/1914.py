#include<bits/stdc++.h>
#define ll long long
#define pb push_back
#define ff first
#define mp make_pair
#define ss second
#define mm(a,b) memset(a,b,sizeof(b))
#define pp pair<ll,ll>
#define mp make_pair
using namespace std;

#define LIMIT 1000000000000000000
set<ll> st;

void recur(ll num,int pv)
{
    if(num>LIMIT)return;

    st.insert(num);

    for(int i=pv;i<=9;i++)
        recur(num*10+i,i);

}

ll answer(ll num)
{
    set<ll> :: iterator it = st.lower_bound(num);
    if(it==st.end() || *it>num)it--;
    return *it;
}

int main()
{
    //GENERATE ALL NUMBERS
    st.insert(0);
    for(int i=1;i<=9;i++)
        recur(i,i);


    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    int cnt=0 ;

    int t;
    cin>>t;

    for(int cs=1;cs<=t;cs++)
    {
        ll n;
        cin>>n;
        cout<<"Case #"<<cs<<": "<<answer(n)<<"\n";
    }


}
