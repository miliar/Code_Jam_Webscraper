#include <bits/stdc++.h>
using namespace std;
 
#define lld long long int
vector< pair<string, lld> > all;
 
lld toNum(string str) {
    lld rs;
    stringstream ss(str);
    ss >> rs;
    return rs;
}
 
string toStr(lld n) {
    stringstream ss;
    ss << n;
    return ss.str();
}
 
string bstr(string m, lld n) {
    string rs="";
    for (lld i = 0; i < (lld)n; i++){
        rs+=m;
    }
    return rs;
}
 
bool isTidy(lld n) {
    string c=toStr(n);
     for (lld i = 0; i < (lld)c.length()-1; i++)
        if ((lld)c[i] > (lld)c[i+1]) return false;
    return true;
}
 
void solve(lld idx, lld n) {
    lld ans=n;
 
    if (n>=10||!isTidy(n)) {
        while(!isTidy(ans)) {
            string c=toStr(ans);
            for (lld i = 0; i < (lld)c.length()-1; i++){
                if ((lld)c[i] > (lld)c[i+1]) {
                    string gb = c.substr(0,i);
                    lld t=toNum(string(1,c[i]))-1;
                    if (t==0&&i!=0)
                        gb.replace(gb.end()-1,gb.end(),string(1,gb[gb.length()-1]));
                    gb+=toStr(t)+bstr("9", (lld)c.length()-i-1); 
                    ans=toNum(gb);
                    break;
                }
            }
        }
    }
 
    printf("Case #%lld: %lld\n", idx+1, ans);
}
 
int main(int argc, char *argv[]) {
    lld N, inp;
 
    scanf("%lld", &N);
 
    for(int i  = 0 ; i < N ; i++){
        scanf("%lld", &inp);
        solve(i, inp);
    }
}