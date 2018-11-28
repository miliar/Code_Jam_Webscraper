#include <bits/stdc++.h>
using namespace std;

int t, k;
string s;

int main() {
    cin>>t;

    for(int test=1; test<=t; test++) {
        cin>>s>>k;

        int flips = 0;
        bool possible = true;
        for(int i=0; i<s.size(); i++)
            if(s[i] == '-') {
                ++flips;
                for(int j=i; j<=i+k-1; j++) {
                    if(j >= s.size()) {
                        possible = false;
                        break;
                    }

                    if(s[j] == '+')
                        s[j] = '-';
                    else
                        s[j] = '+';
                }
            }

        cout<<"Case #"<<test<<": ";
        if(possible)
            cout<<flips<<"\n";
        else
            cout<<"IMPOSSIBLE\n";

    }

    return 0;
}
