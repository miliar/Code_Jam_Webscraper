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

int ins,ts ;
vector<s> ans ;
s str ;

s solve(){
    cin >> str ;
    while(true){
        bool rep = false;
        for(int i=0 ; i<str.length()-1 ; i++){
            if(str[i]>str[i+1]){
                str[i]--;
                for(int j=i+1 ; j<str.length() ; j++)str[j]='9';
                i=str.length()-1;
                rep =true;
            }
        }
        if(!rep)return str;
    }
}

 s zeros(s strc){
    s ne = "" ;
    for(int i=0 ; i<strc.length() ; i++){
        if(strc[i]!='0'){
            return strc.substr(i);
        }
    }
 }

int main(){
    intimain();
    cin >> ts ;
    for(int i=0 ; i<ts ; i++)ans.pb(solve());
    for(int i=0 ; i<ans.size() ; i++)cout<<"Case #"<<i+1<<": "<<zeros(ans[i])<<endl;
}





