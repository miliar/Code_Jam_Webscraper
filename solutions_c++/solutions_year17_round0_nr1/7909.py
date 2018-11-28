#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>

using namespace std;

bool a [10000];

int main() {
#ifndef ONLINE_JUDGE
    freopen("/Users/ZALORA/Documents/facebook/facebook/input.txt","r", stdin);
    freopen("/Users/ZALORA/Documents/facebook/facebook/output.txt","w", stdout);
#endif
    
    int t, n;
    string s;
    
    cin>>t;
    for (int test = 1; test <= t; ++test) {
        cin>>s>>n;
        
        cout<<"Case #"<<test<<": ";
        //cout<<s<<" "<<n<<endl;
        int len = (int)s.length();
        
        for (int i = 0; i < len; ++i) {
            a[i] = false;
        }
        
        bool flag = false;
        bool isImposs = false;
        int count = 0;
        for (int i = 0; i < len; ++i) {
            if (a[i] == true) flag = !flag;
            
            bool check = (s[i] == '+' && flag == true) || (s[i] == '-' && flag == false);
            if (check == true && i + n <= len) {
                ++count;
                flag = !flag;
                a[i+n] = true;
            } else if (check == true) {
                isImposs = true;
                cout<<"IMPOSSIBLE";
                break;
            }
        }
        
        if (isImposs == false) cout<<count;
        cout<<endl;
    }
}
