#include<bits/stdc++.h>
#define ll long long

using namespace std;

ll power(ll a, ll b){
ll ans = 1;

  while(b){
        if(1&b){
           ans *= a;
        }
        a *= a;
        b = b>>1;
  }
  return ans;
}

//char a1[] = {'a','e','i','o','u'}, a2[] = {'b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z'};
int a[23];


int main(){
   freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    int t;
    cin >> t;
    for(int j = 1; j <= t; j++){
        ll n;
        cin >> n;

        ll n1 = n;
        int s = 0;

        while(n1){
            int c = n1%10;
            a[s++] = c;
            n1 /= 10;
        }

    //reverse(a, a+s);
    if(s == 1){
        cout << "Case #"<< j << ": " << n << endl;
    }
    else{
        for(int i = 0; i < s-1; i++){
            if(a[i] < a[i+1]){
                for(int k = i; k >=0; k--) a[k] = 9;
                a[i+1]--;
            }
        }
        n1 = 0;
        for(int i = s-1; i >= 0; i--){
            n1 = 10*n1 + a[i]*1LL;
        }
         cout << "Case #"<< j << ": "<< n1 << endl;
    }
    }
}
