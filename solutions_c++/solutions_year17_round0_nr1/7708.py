#include<iostream>
#include<algorithm>

using namespace std;

bool check(string s) {
    for(int i=0; s[i] != '\0'; i++)
        if(s[i] == '-')
            return false;
    return true;
}

int main () {
    
    int t; cin>>t;

    for(int i=1; i<=t; i++) {
        string s; cin>>s;
        int w; cin>>w;

        int l = s.length();

        int c = 0, j = 0;

        while(j < l) {
            if(s[j] == '-' && j+w <= l) {
                for(int k=j; k<j+w; k++) {
                    if(s[k] == '-') s[k] = '+';
                    else s[k] = '-';
                }
                c++;
            }
            j++;
        }

        if(check(s)) cout<<"Case #"<<i<<": "<<c;
        else cout<<"Case #"<<i<<": IMPOSSIBLE";
        if(i < t) cout<<"\n";
    }
    return 0;
}