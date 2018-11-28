#include <bits/stdc++.h>
#define rep(i,n) for(int i=0;i<n;i++)
#define FOR(i,a,b) for(int i=a;i<=b;i++)
#define rz resize
#define pb push_back
#define fi first
#define se second
#define MOD 1000000007
#define MAX 100005
#define tc int _t;cin>>_t;while(_t--)

using namespace std;

typedef long long int ll;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<bool> vb;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef vector<vi> vvi;
typedef vector<vll> vvll;

ll mp(ll b,ll a){ll ans = 1;while(b) {if (b&1) ans=(ans*a)%MOD;a=(a*a)%MOD;b>>=1;}if (ans<0) ans+=MOD;return ans;}
// char A[1000009];vector<int> v;
bool f(char a,char b) {
  return (a<=b);
}

string vv(string s) {
    string ans = "";
      bool ch = false;
    int l = s.length();
    if (l == 1)ans = s;
    else {
    for (int i =0 ; i<l-1;i++) {
      if (f(s[i],s[i+1])) {
        ;
      } else {
        ch = true;
        if (s[i] == '1') {
          ans="";
          for (int k = 0;k<l-1;k++)
            ans+='9';
          break;
        } else {
          int x = (int)s[i] - '0';
          ans += x - 1+ '0';
          for (int kk = i +1;kk <l;kk++) ans+='9'; 
          // cout << (char)(x - 1+ '0') << " [] \n"<<ans<<"\n";
            if (x-1+'0' >= s[i-1]) {
              // cout << s[i-1] << " ::\n";
          break;
            }
          else 
            ans = vv(ans);
          break;
        }
      }
      ans+=s[i];
    }}
    if (!ch)ans = s;
    return ans;
}

int main()
{
	ll n,c,a,ans;
  ios::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
  int t;cin>>t;
  int cc = 0;
  while(t--)
  {
    cc++;
    string s;
    cin >> s;
    string ans = vv(s);
    cout << "Case #"<<cc<<": "<<ans<<"\n";
  }
}