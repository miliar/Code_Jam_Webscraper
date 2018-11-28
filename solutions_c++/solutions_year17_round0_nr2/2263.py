#include<bits/stdc++.h>

#define INF 9223372036854775807
#define mod 1000000007
#define ll  long long int
#define ld double
#define endl '\n'
#define sz 202
#define fast() ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)

using namespace std;

ll arr[sz],n;
string str;

void change(ll x){
    arr[x] -=1;
    for(ll i = x+1; i < n;i++)
        arr[i] = 9;
}

int main(){
    ll t,i,j;
    fast();
    cin>>t;
    for(ll test = 1; test <= t; test++){
        cin>>str;
        n = str.size();
        for(i = 0; i < n; i++){
            arr[i] = (ll)(str[i] - '0');
        }
        cout<<"Case #"<<test<<": ";

        if(n == 1)
            cout<<str<<endl;
        else{
            for(i = n-1; i > 0; i--){
                if(arr[i] < arr[i-1])
                    change(i-1);
            }
            i = 0;
            for(;i < n; i++){
                if(arr[i] != 0)
                    break;
            }
            for(;i < n; i++)
                cout<<arr[i];
            cout<<endl;
        }
    }
    return 0;
}

