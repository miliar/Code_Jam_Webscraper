/*__ _(_) __ _  ___  ___ _   _  __| | __ _ _   _| |_ ___
 / _` | |/ _` |/ _ \/ __| | | |/ _` |/ _` | | | | __/ _ \
| (_| | | (_| | (_) \__ \ |_| | (_| | (_| | |_| | || (_) |
 \__, |_|\__,_|\___/|___/\__,_|\__,_|\__,_|\__,_|\__\___/
 |___/                                  Accepted Code  */
#include <bits/stdc++.h>
using namespace std;

bool isTidy(string s){
    if(s.length()==1) return true;
    unsigned int x=0;
    while(x<s.length()-1 && s[x]<=s[x+1])x++;
    if(x==s.length()-1) return true;
    return false;
}

string makeTidy(string s, int pos){
    string res=s;
    for(unsigned int i=pos; i<s.length(); i++) res[i]='9';
    pos--;
    while(true){
        if(res[pos]>'0') {
            res[pos]=char(int(res[pos]-1));
            break;
        }
        else {
            res[pos]='9';
            pos--;
        }
    }
    while(res[0]=='0' && res.length()>1) res.erase(0,1);
    return res;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
#ifdef gsdt
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
#endif // gsdt

    int T; cin>>T;
    for(int test=1; test<=T; test++){
        string s; cin>>s;
        if(isTidy(s)){
            cout<<"Case #"<<test<<": "<<s<<endl;
            continue;
        }
        for(int i=s.length()-1; i>=1; i--){
            string tmp=makeTidy(s,i);
            if(isTidy(tmp)){
                cout<<"Case #"<<test<<": "<<tmp<<endl;
                break;
            }
        }
    }

    return 0;
}
