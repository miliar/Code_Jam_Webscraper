#include<bits/stdc++.h>
#define s(x) scanf("%d",&x)
#define ll long long
#define l(x) scanf("%I64d",&x)
#define cst int t; s(t); while(t--)
#define fr freopen("B-large.in", "r", stdin)
#define fo freopen("out.txt", "w", stdout)
#define finp ios_base::sync_with_stdio(false)
#define pb push_back
#define pf printf

using namespace std;

vector<ll> numberToArray(ll n)
{
    vector<ll> v;
    stack<ll> s;
    while(n!=0){
        s.push(n%10);
        n/=10;
    }
    while(!s.empty()){
        v.push_back(s.top());
        s.pop();
    }
    return v;
}

ll findTidy(ll n)
{
    vector<ll> v = numberToArray(n);
    int i=0;
    ll tidyNo=0;
    while(i < (v.size()-1)){
        if(v[i+1]<v[i])
            break;
        i++;
    }
    if(i == (v.size()-1))
        return n;
    while(i>0 && v[i]==v[i-1])
        i--;
    for(int j=0; j<i; j++)
        tidyNo = tidyNo*10 + v[j];
    tidyNo = tidyNo*10 + v[i]-1;
    for(; i<v.size()-1; i++)
            tidyNo = tidyNo*10 + 9;
    return tidyNo;

}


int main()
{
    fr;
    fo;
    int t;
    cin>>t;
    for(int caseNo=1; caseNo<=t; caseNo++){
        ll n;
        cin>>n;
        printf("Case #%d: %lld\n", caseNo, findTidy(n));
    }
    return 0;
}
