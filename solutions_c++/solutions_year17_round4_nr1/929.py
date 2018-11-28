#include <bits/stdc++.h>
using namespace std;
//#define DEBUG
#define INF 0x3f3f3f3f
#define INF16 16000000000000000LL
#define INF18 1000000000000000000LL
#define F first
#define S second
#define mp make_pair
#define pb push_back
#define mod9 (int)(1e7 + 9)
#define mod7 (int)(1e7 + 7)
#define eps 1e-9
#define mse(x , y) memset(x , y , sizeof(x))
#define ALL(x) x.begin(),x.end()
#define RALL(x) x.rbegin(),x.rend()
#define IOS do { ios::sync_with_stdio(0);cin.tie(0); } while (0)
typedef pair< int , int > pii;
typedef long long ll;

template < typename Iter >
ostream& _out(ostream& s , Iter a , Iter b){
    for(auto it = a; it != b; it++)
        s << (it == a ? "" : " ") << *it;
    return s;
}

template < typename A , typename B > 
ostream& operator << (ostream &s , pair< A , B > &p){ return s << "(" << p.F << " , " << p.S << ")"; }
template < typename T >
ostream& operator << (ostream &s , vector< T > &v){ return _out(s , ALL(v)); }



inline ll rit(){
    int key = 1;
    char c = getchar();
    while(!isdigit(c)){
        if(c == '-') key = -1;
        c = getchar();
    }

    ll x = 0;
    while(isdigit(c)){
        x = x * 10 + c - '0';
        c = getchar();
    }
    return x * key;
}

int __ = 1;

/*********default*********/

void init(){
}

void read(){
}

void solve(){
}

int a[1000];

int main(){
    int t, n, p;
    int kase = 0;
    cin >> t;
    while(t--) {
        scanf("%d%d", &n, &p);
        int left = 0;
        int box[10];
        memset(box, 0, sizeof(box));
        for(int i = 0; i < n; i++) {
            int x = rit();
            a[i] = x;
            box[x % p]++;
        }

        int ans;
        if(p != 4) {
            ans = box[0];
            for(int i = 1; i < p; i++) {
                if(box[i] >= box[p - i] && box[i]) {
                    if(p - i != i)
                        ans += box[p - i];
                    else 
                        ans += box[i] / 2;

                    int foo;
                    if(p - i != i)
                        foo = box[i] - box[p - i];
                    else 
                        foo = box[i] % 2;
                    box[p - i] = 0;

                    if(foo == 0) continue;
                    ans += (foo - 1) / p + 1;
                }
            }
        } else {
            ans = box[0];
            ans += min(box[1], box[3]);
            int foo = max(box[1], box[3]) - min(box[1], box[3]);
            if(box[2])
                ans += (box[2]) / 2;
            if(box[2] & 1) {
                if(foo == 0)
                    ans++;
                if(foo >= 2) {
                    foo -= 2;
                    ans++;
                }
                if(foo)
                ans += (foo - 1) / p + 1;
            } else {
                if(foo)
                ans += (foo - 1) / p + 1;
            }
        }

        printf("Case #%d: %d\n", ++kase, ans);



    }
    return 0;
}





