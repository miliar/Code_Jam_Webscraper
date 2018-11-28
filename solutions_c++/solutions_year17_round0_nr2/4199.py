using namespace std;

#include<bits/stdc++.h>

#define ll long long


int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);

    ll T, N;
    cin>>T;

    for(int iter=1; iter<=T; iter++){
        cin>>N;
        vector<ll> a;
        ll temp, ans = 0;
        bool isTedi = true;

        temp = N;
        while(temp>0){
            a.push_back(temp%10);
            temp /= 10;
        }

        reverse(a.begin(), a.end());
        /**for(int i=0; i<a.size(); i++) cout<<a[i]<<" ";
        cout<<"\n";**/

        for(int i=1; i<a.size() && isTedi; i++){
            if(a[i-1]>a[i]) isTedi = false;
        }
        if(isTedi) ans = N;

        for(int i=a.size()-1; i>0; i--){
            isTedi = true;
            vector<ll> b;
            ll cur = 9;

            if(a[i-1]>0){a[i] = 9; a[i-1]--;}
            else{
                a[i] = 9; a[i-1] = max(0ll, a[i-1]-1);
                i--;
                while(i>0 && a[i]==0){
                    a[i] = 9; a[i-1] = max(0ll, a[i-1]-1);
                    i--;
                }
                i++;
            }

            /**cout<<"i : "<<i<<" a : ";
            for(int j=0; j<a.size(); j++) cout<<a[j]<<" ";
            cout<<"\n";**/

            for(int j=0; j<a.size(); j++) b.push_back(a[j]);
            for(int j=b.size()-1; j>=0; j--){
                cur = min(cur, b[j]);
                b[j] = cur;
            }
            /**cout<<" b : ";
            for(int j=0; j<b.size(); j++) cout<<b[j]<<" ";
            cout<<"\n";**/

            ll val = 0, mul = 1;
            for(int j=b.size()-1; j>=0; j--){
                val += mul*b[j];
                mul *= 10;
            }
            ans = max(val, ans);
        }
        cout<<"Case #"<<iter<<": "<<ans<<"\n";
    }

return 0;
}
