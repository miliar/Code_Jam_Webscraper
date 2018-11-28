#include <bits/stdc++.h>

using namespace std;

const int N=1e3+10;
string s;

string solve(){
    int n=s.length();
    int R=0;
    while (R<n-1&&s[R+1]>=s[R]) R++;
    if (R==n-1) return s;
    while (R&&s[R]==s[R-1]) R--;
    if (R==0&&s[0]=='1') return string(n-1,'9');
    s[R]--;
    for(int i=R+1;i<n;i++) s[i]='9';
    return s;
}
int main(){
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    int test;
    cin>>test;
    for(int te=1;te<=test;te++){
        cin>>s;
        cout<<"Case #"<<te<<": "<<solve()<<'\n';
    }
}
