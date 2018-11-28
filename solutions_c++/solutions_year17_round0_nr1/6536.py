#include <bits/stdc++.h>
using namespace std;

#define fill(x,y) memset(x,y,sizeof(x))
#define fi first
#define se second
#define sz(x) ((int) (x).size())
#define all(x) (x).begin(), (x).end()
#define sqr(x) ((x) * (x))
#define sqrt(x) sqrt(abs(x))
#define mp make_pair
#define pb push_back

typedef long long ll;
typedef string s;
typedef pair<int,int> pii;
typedef pair<int,string> pis;
typedef pair<string,int> psi;
typedef pair<string,string> pss;
typedef vector<ll> vi;
typedef vector<vi> vvi;
typedef vector<pii> vpii;

const ll oo = 1e10;

const double EPS = (1e-8);
const ll mod = 1000000007;

int dcmp(double x, double y) {  return fabs(x-y) <= EPS ? 0 : x < y ? -1 : 1; }

void intimain(){
	ios_base::sync_with_stdio(0);
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
}

int ts;
vi ans ;


int solve(){
   s str ; int k , steps = 0;
   cin >> str >> k;
   for(int i=0 ; i<str.length() ; i++){
        if(str[i]=='-'){
            if(str.length()-i>=k){
                steps ++;
                for(int j=i  ; j<i+k ; j++)if(str[j]=='+')str[j]='-';else str[j]='+';
            }else return -1;
        }
   }
   return steps ;
}

int main(){
    intimain();
    cin >> ts;
    for(int i=0 ; i<ts ; i++)ans.pb(solve());
    for(int i=0 ; i<ans.size() ; i++)if(ans[i] != -1)cout << "Case #"<<i+1<<": "<<ans[i]<<endl;else cout << "Case #"<<i+1<<": "<<"IMPOSSIBLE"<<endl;
}





