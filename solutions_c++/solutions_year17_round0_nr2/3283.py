#include <bits/stdc++.h>
using namespace std;

string s;
int t;

bool ascending(string &s) {
    for(int i=0; i<int(s.size())-1; i++)
        if(s[i] > s[i+1])
            return false;

    return true;
}

int main() {
    cin>>t;

    for(int test=1; test<=t; test++) {
        cin>>s;

        while(!ascending(s)) {
            for(int i=0; i<int(s.size())-1; i++) {
                if(s[i] > s[i+1]) {
                    s[i]--;

                    for(int j=i+1; j<int(s.size()); j++)
                        s[j] = '9';
                    break;
                }
            }
        }

        s.erase(0, s.find_first_not_of('0'));

        cout<<"Case #"<<test<<": "<<s<<"\n";

    }

    return 0;
}
