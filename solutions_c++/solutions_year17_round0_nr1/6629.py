/*__ _(_) __ _  ___  ___ _   _  __| | __ _ _   _| |_ ___
 / _` | |/ _` |/ _ \/ __| | | |/ _` |/ _` | | | | __/ _ \
| (_| | | (_| | (_) \__ \ |_| | (_| | (_| | |_| | || (_) |
 \__, |_|\__,_|\___/|___/\__,_|\__,_|\__,_|\__,_|\__\___/
 |___/                                  Accepted Code  */
#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
#ifdef gsdt
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
#endif // gsdt

    int T; cin>>T;
    for(int test=1; test<=T; test++){
        string s; cin>>s;
        int k; cin>>k;
        int res=0;

        unsigned int x=0;
        while(true){
            while(x<=s.length()-1 && s[x]=='+') x++;
            if(x==s.length()){
                //cout<<"Case #"<<test<<": "<<res<<endl;
                printf("Case #%d: %d\n",test,res);
                break;
            }
            if(x>s.length()-k) {
                //cout<<"Case #"<<test<<": IMPOSSIBLE"<<endl;
                printf("Case #%d: IMPOSSIBLE\n",test);
                break;
            }
            res++;
            for(unsigned int i=x; i<x+k; i++)
                if(s[i]=='+') s[i]='-';
                else s[i]='+';
        }
    }


    return 0;
}
