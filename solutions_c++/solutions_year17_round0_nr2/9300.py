#include <bits/stdc++.h>

using namespace std;


typedef long long ll;
typedef pair<ll,int> ii;
typedef pair<ii,int> iii;


#define N 100005
#define M 150005
#define MOD 1000000007
#define PI acos(-1)
#define rep(i,a,b) for(int i = a; i < b; i++)
#define reps(i,a,b) for(int i = a; i >= b; i--)
#define sc scanf
#define pc printf
#define pb push_back
#define F first
#define S second

int t,sz;
string s,dup;

int main () {

    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
    sc("%d",&t);

    int tt = 0;
    while(++tt <= t){
        cin >> s;
        sz = s.size();
        dup = "";
        if(sz < 2){
            cout << "Case #" << tt << ": " << s << endl;
        }
        else if(sz == 2 && s == "10"){
            cout << "Case #" << tt << ": 9" <<endl;
        }
        else if(sz == 2){
            if(s[0] > s[1]){
                s[0]--;
                s[1] = '9';
            }
            cout << "Case #" << tt << ": " << s << endl;
        }
        else{
            bool is = 0,prin = 0;
            rep(i,0,sz-1){
                if(is) dup += '9';
                else if(s[i] <= s[i+1]) dup += s[i];
                else{
                    int a = s[i] - '0';
                    a--;
                    int b = dup[i-1] - '0';
                    if(a < b){
                        //cout <<"yes "  <<i << endl;
                        if(s[0] == '1'){
                            dup = "";
                            rep(i,0,sz-1){
                                dup += '9';
                            }
                            prin = 1;
                            cout << "Case #" << tt << ": " << dup << endl;
                            break;
                        }
                        else{
                            dup = "";
                            s[i]--;
                            dup += s[i];
                            rep(i,0,sz-1){
                                dup += '9';
                            }
                            prin = 1;
                            cout << "Case #" << tt << ": " << dup << endl;
                            break;
                        }
                    }
                    else{
                       // cout << "no " << i << endl;
                        s[i]--;
                        dup += s[i];
                        is = 1;
                    }
                }
            }
            if(is){
                dup += '9';
            }
            else{
                dup += s[sz-1];
            }
            if(!prin){
                cout << "Case #" << tt << ": ";
                if(dup[0] == '0'){
                    rep(i,1,sz) cout << dup[i];
                    cout << endl;
                }
                else{
                    rep(i,0,sz) cout << dup[i];
                    cout << endl;
                }
            }

        }
    }

    return 0;
}






