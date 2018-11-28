#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;

#define F first
#define S second
#define inf INT_MAX
#define INF LONG_LONG_MAX
#define all(v) v.begin(), v.end()
#define rall(v) v.rbegin(), v.rend()

bool istidy(ll n){
    ll prv = 9;
    while(n){
        ll r=n%10;
        if(r>prv)
            return 0;
        prv=r;
        n/=10;
    }
    return 1;
}

string conv(ll n){
    string ret="";
    while(n){
        ll r=n%10;
        ret+=r+48;
        n/=10;
    }
    reverse(all(ret));
    return ret;
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int t, cnt = 1;
    cin >> t;
    while(t--){
        ll n;
        cin >> n;
        if(istidy(n)){
            cout << "Case #" << cnt++ << ": " << n << endl;
            continue;
        }
        string num=conv(n), res="";
        int p=0;
        for(int i = 0; i < num.size()-1; i++){
            if(num[i]>num[i+1]){
                p=i;
                break;
            }
        }
        if(num[p]=='1'){
            for(int i = 0; i < num.size()-1; i++)
                res+='9';
            num.clear();
            num=res;
        }
        else if(p!=0&&num[p]==num[p-1]){
            for(int i = p; i>= 0; i--){
                if(i==0){
                    p=0;
                    break;
                }
                if(num[i]!=num[i-1]){
                    p=i;
                    break;
                }
            }
            num[p]--;
            for(int i = p+1; i<num.size(); i++){
                num[i]='9';
            }
        }
        else{
            num[p]--;
            for(int i = p+1; i<num.size(); i++){
                num[i]='9';
            }
        }
        cout << "Case #" << cnt++ << ": " << num << endl;
    }
    return 0;
}
