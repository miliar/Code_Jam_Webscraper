#include <iostream>
using namespace std;

void flip(string &s, int pos, int f){
    for (int i=0;i<f;i++) {
        if (s[pos+i] == '+') s[pos+i] = '-';
        else s[pos+i] = '+';
    }
}
bool chk(string s){
    for (int i =0; i<s.length();i++){
        if (s[i]=='-') return false;
    }
    return true;
}

int main() {
    int n;
    cin>>n;
    string s; int f;
    for(int j=0;j<n;j++){
        cin>>s>>f;
        int i,c=0;
        for (i=0;i<s.length()-f+1;i++){
            if (s[i]=='-') {flip(s,i,f); c++;}
        }
        cout<<"Case #"<<j+1<<": ";
        if(chk(s)) cout<<c<<endl;
        else cout<<"IMPOSSIBLE"<<endl;
    }
}