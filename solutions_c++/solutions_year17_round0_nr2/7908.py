#include <bits/stdc++.h>

#define ll long long
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define Nn 100005
#define M 1000005
//#define mod 1e9+7

using namespace std;

typedef pair<int,int> ii;
typedef pair<ll,ll> lii;
typedef vector<int> vi;
typedef vector<ii> vii;
const double pi = acos(-1);
const int inf = 2e9;

int t , p = 1;
ll n , x;
char s[50];
vi v;

bool ok(int x) {
      if(x / 10 == 0)
            return true;

      v.clear();
      while(x / 10 >= 0 && x != 0) {
            v.pb(x % 10);
            x /= 10;
      }
      for(int i = v.size()-2; i >= 0; --i) {
            //cout << v[i] << endl;
            if(v[i] < v[i+1])
                  return false;
      }
      return true;
}

int main() {

      #ifndef ONLINE_JUDGE
            freopen("in.in", "r", stdin);
            freopen("out.in", "w", stdout);
      #endif
            scanf("%d" , &t);
            while(t--) {
                  v.clear();

                  scanf("%s" , s);
                  int l = strlen(s);
                  if(l == 1) {
                        printf("Case #%d: %d\n" ,p++ ,  s[0]-'0');
                        
                  }
                  else{

                  while(l--) {
                        v.pb(s[l]-'0');
                  }
                  for(int i = 0; i < v.size()-1; ++i) {
                        //cout << v[i] << endl;
                        if(v[i] < v[i+1]) {
                              v[i+1]--;
                              for(int j = i; j >= 0; --j)
                                    v[j] = 9;
                        }
                  }
                  ll ans = 0 , m = 1;
                  for(int i = 0; i < v.size(); ++i) {
                        ans += v[i]*m;
                        m *= 10;
                  }

                   printf("Case #%d: %lld\n" ,p++ ,  ans);
            }
      }
            
}