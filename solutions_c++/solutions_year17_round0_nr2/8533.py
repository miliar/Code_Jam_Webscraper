#include <bits/stdc++.h>

#define ll long long
using namespace std;

int main() {
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    ll t;
    cin >> t;
    for (ll i = 1; i <= t; i++) {
        string k;
        cin >> k;
        int s = k.size()-1;
        while (true) {
            bool f = true;
            for (int j = 1; j < k.size(); j++)
                if (k[j - 1] > k[j]) f = false;
            if (f) break;
            else
            {
                k[s] = '9';
                if (k[s-1] != '0') {k[s-1]--; s--;}
                else{
                    for (int j = s-1; j >=0; j--)
                    {
                        if (k[j] != '0') k[j] = '9';
                        else {k[j]--; s = j; break;}
                    }
                }
            }
        }
        cout << "Case #" << i << ": ";
        int y = 0;
        for (int j = 0; j < k.size(); j++)
            if (k[j] != '0') {y = j; break;};
        for (int j = y; j < k.size(); j++)
            cout << k[j];
        cout << endl;
    }
    return 0;
}