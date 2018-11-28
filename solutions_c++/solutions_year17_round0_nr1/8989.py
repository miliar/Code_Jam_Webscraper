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

int T,k;
string s;
int sz;

int main () {

    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    sc("%d",&T);
    int t = 0;
    while(++t <= T){
        cin >> s >> k;
        sz = s.size();
        int cnt = 0;
        rep(i,0,sz-k+1){
            //cout << i << endl;
            if(s[i] == '-'){
                //cout << "yes" << endl;
                cnt++;
                rep(j,i,i+k){
                    if(s[j] == '+') s[j] = '-';
                    else s[j] = '+';
                }
            }
        }
        bool ageHy = 0;
        rep(i,0,sz){
            if(s[i] == '-'){
                ageHy = 1;
                printf("Case #%d: IMPOSSIBLE\n",t);
                break;
            }
        }
        if(!ageHy){
            printf("Case #%d: %d\n",t,cnt);
        }

    }

    return 0;
}






