#include <bits/stdc++.h>

#define ll long long
#define M 1000000007
#define INF 9223372036854775807
#define mp(x, y) make_pair(x,y)
#define pb(x) push_back(x)
#define pmp(x, y) pb(mp(x,y))
#define ld double
#define PI 3.14159265
#define len(a) (ll)a.size()    //
#define F first
#define S second
#define endl "\n"
#define fast() ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)
using namespace std;

ll to_int(char s){
    return s-'0';
}


bool check(string s){

    for (ll i = 0; i < len(s)-1; i++) {
        if(to_int(s[i])>to_int(s[i+1]))
            return false;
    }
    return true;
}


int main() {

    ll t;
    cin >> t;
    for (ll i = 0; i < t; i++) {

        string s;
        cin>>s;

        while(check(s)==false){

            ll j=0;
            while(to_int(s[j])<=to_int(s[j+1]) and j+1<len(s))
                j++;
            s[j]-=1;
            j++;
            while(j<len(s)){
                s[j]='9';
                j++;
            }
        }

        cout<<"Case #"<<i+1<<": ";
        ll j=0;
        while(s[j]=='0')
            j++;
        while(j<len(s)){
            cout<<s[j];
            j++;
        }
        cout<<endl;
    }
    return 0;
}