#include <bits/stdc++.h>
#define ll long long
using namespace std;
char ss[10010];
bool tidy(string s) {
    for(int i = 0;i < s.size()-1;i++) {
        if(s[i] > s[i+1]) return false;
    }
    return true;
}

void solve() {
    scanf("%s",ss);
    ll n = strtoll(ss,NULL,10);
    string s = ss;
    int nowDig = s.size()-1;
    while((strtoll(s.c_str(),NULL,10)>n || !tidy(s)) && nowDig >= 0) {
        if(s[nowDig] == '0') {s[nowDig] = '9'; nowDig--; }
        else s[nowDig]--;
        //printf("%s\n",s.c_str());
    }
    printf("%lld\n",strtoll(s.c_str(),NULL,10));

}
int main() {
    int t;
    scanf("%d",&t);
    for(int i = 0;i < t;i++) {
        printf("Case #%d: ",i+1);
        solve();
    }
}
