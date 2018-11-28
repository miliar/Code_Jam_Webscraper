#include <bits/stdc++.h>

#include <string>
#include <iostream>
#include <sstream>

using namespace std;
typedef long long ll;

string to_string(ll n) {
    ostringstream os;
    os << n;
    return os.str();
}

string fine(ll n) {
    string s = to_string(n);
    for(int i=1;i<s.size();i++) {
        if(s[i]<s[i-1]) {
            string temp = s;
            for(int j=i;j<s.size();j++) {
                temp[j] = '0';
            }
            return temp;
        }
    }
    return s;
}

bool all(string s)
{
    for(int i=1;i<s.size();i++) {
        if(s[i]<s[i-1])return false;
    }
    return true;
}

ll to_int(string s) {
    ll ans = 0;
    for(int i=0;i<s.size();i++) {
        ans *= 10;
        ans += s[i]-'0';
    }
    return ans;
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("google2.out","w",stdout);
    int test;
    cin >> test;
    int j = 0;
    while(test--)
    {
        j++;
        ll n;
        cin >> n;
        while(true)
        {
            if(all(to_string(n))) {
                cout << "Case #"<< j << ": " << n << endl;
                break;
            }
            if(to_string(n)==fine(n)) {
                n = n-1;
                continue;
            }
            n = to_int(fine(n));
        }
    }
}
