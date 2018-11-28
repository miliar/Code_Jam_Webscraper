#include <iostream>
#include <string>
using namespace std;

string solve(string s){
    unsigned n = s.size();
    int i=1;
    while((i<n) && (s[i-1] <= s[i])){
        ++i;
    }
    
    if(i>=n){
        return s;
    }
    
    for(int j=i-1; j>=0; --j){
        if(s[j] > s[j+1]){
            s[j]--;
            s[j+1] = '9';
        }
    }
    
    while(i<n){
        s[i] = '9';
        ++i;
    }
    
    if(s[0] == '0'){
        return s.substr(1, n-1);
    }
    return s;
}

int main(){
    int T;
    cin>>T;
    
    for(int t=1; t<=T; ++t){
        string s;
        cin>>s;
        string sol = solve(s);
        cout<<"Case #"<<t<<": "<<sol<<endl;
    }
    return 0;
}

