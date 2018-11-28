#include<bits/stdc++.h>
using namespace std;

int f() {
    string s;
    int k;
    cin>>s>>k;
    int n = s.size();
    int flips = 0;
    int totalFlips = 0;
    vector<bool> flipped(n,false);
    
    for(int i=0;i<n;i++) {
        if(i-k>=0 && flipped[i-k]) flips--;
        if(flips % 2 == 1) s[i] = (s[i]=='+') ? '-' : '+';
        if(s[i]=='-') {
            if(i+k > n) return -1;
            flipped[i] = true;
            flips++;
            totalFlips++;
            s[i]='+';
        }
    }
    return totalFlips;


}

int main() {
    int t;
    cin>>t;
    for(int i=1;i<=t;i++) {
        int s = f();
        cout<<"Case #"<<i<<": ";
        if(s<0) cout<<"IMPOSSIBLE\n";
        else cout<<s<<endl;

    }
}
