#include<bits/stdc++.h>
#define ll long long
#define pb push_back
#define all(v) v.begin(),v.end()
#define mp make_pair
#define ff first
#define ss second
#define MAX  1e6+5;
using namespace std;


int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    ll t;
    string s;
    ll k;
    cin>>t;
    for(ll i=0;i<t;i++){
        cout<<"Case #"<<i+1<<": ";
        cin>>s>>k;
        ll l=s.size();
        ll j=0;
        ll count=0;
        while(j<l)
        {
            while(s[j]=='+'&&j<l){
                j++;
            }
            if(j==l)
                break;
            if(j+k<=l){
                count++;
                for(ll r=j;r<j+k;r++){
                    if(s[r]=='+')
                        s[r]='-';
                    else
                        s[r]='+';
                }
            }
            else{
                cout<<"IMPOSSIBLE\n";
                count=-1;
                break;
            }
        }
        if(count!=-1){
            cout<<count<<endl;
        }
    }


    return 0;
}

