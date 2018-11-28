#include <bits/stdc++.h>
typedef long long ll;

using namespace std;


int main()
{
    ios::sync_with_stdio(false);

    int T , p;
    ll n;
    string s1 , s2;
    cin>>T;
    for(int t = 1 ; t <= T ; t++){
        cin>>n;

        s1 = s2 = to_string(n);
        sort(s2.begin() , s2.end());
        p = (int)s1.length() - 1;

        for(ll i = 1 ; s1 != s2 ; i*=10){
            n -= i * (1 + (ll)s1[p] - (ll)'0');
            s1 = s2 = to_string(n);
            sort(s2.begin() , s2.end());
            p--;
        }

        cout<<"Case #"<<t<<": "<<n<<endl;
    }
    return 0;
}
