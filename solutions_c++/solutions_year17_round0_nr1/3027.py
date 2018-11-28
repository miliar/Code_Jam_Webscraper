#include <iostream>
using namespace std;

int main() {
    int t, n, counter = 0;
    string s;
    cin>>t;
    for(int i = 0; i<t; i++) {
        counter = 0;
        cin>>s>>n;
        for(int j = 0; j<=s.length() - n; j++) {
            if(s[j] == '-') {
                for(int x = j; x< j+n; x++) {
                    s[x] = (s[x] == '-') ? '+' : '-';
                }
                ++counter;
            }
        }
        int flag = 0;
        for(int j = s.length() - n; j< s.length();j++) {
            if(s[j] == '-') {
                cout<<"CASE #" << i+1 <<": IMPOSSIBLE"<<endl;
                flag = 1;
                break;
            }
        }
        if(!flag) cout<<"CASE #" << i+1<< ": " << counter<<endl;
    }
}