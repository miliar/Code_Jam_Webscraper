#include <bits/stdc++.h>

using namespace std;

int istidy(long long n){
    string s=to_string(n);
    int count=1;
    for(int i=0;i<s.length()-1;i++){
        if(s[i]>s[i+1]){
            count=0;
            break;
        }   
    }
    return count;
}


int main() {
    std::ios::sync_with_stdio(false);
    int t;
    cin>>t;
    for(int a0=1;a0<=t;a0++){
        long long n;
        cin>>n;
        for(long long i=n;i>=0;i--){
            if(istidy(i)==1){
                cout<<"Case #"<<a0<<": "<<i<<endl;
                break;
            }
        }
    }
    return 0;
}