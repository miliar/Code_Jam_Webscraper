#include<bits/stdc++.h>
#define x first
#define y second
using namespace std;
typedef long long LL;
typedef long double LD;
const LL LLinf=9e18+5;
const int MOD=1e9 + 7;
const LD pi = acos(-1.0L);
const int NMAX = 100000+69;
const int INF = 0x3f3f3f3f;

bool check(int x){
  string s="";
  while(x){
    s+='0' + (x%10);
    x/=10;
  }
  reverse(s.begin(), s.end());
  for(int i=1; i<s.size(); i++){
    if(s[i] < s[i-1]){
      return 0;
    }
  }

  return 1;
}

int T;
LL n;

void solve(){
  cin>>T;
  for(int tt=1; tt<=T; tt++){
    cout<<"Case #"<<tt<<": ";
    cin>>n;
    string s="";
    while(n){
      s+='0' + (n%10);
      n/=10;
    }
    reverse(s.begin(), s.end());
    bool q=1;
    while(q){
      q=0;
      for(int i=0; i<s.size()-1; ++i){
        if(s[i]>s[i+1]){
          s[i]--;
          q=1;
          for(int j=i+1; j<s.size(); ++j){
            s[j] = '9';
          }
          break;
        }
      }
    }
    bool fst = 0;
    for(int i=0; i<s.size(); i++){
      if(s[i] != '0'){
        fst = 1;
      }
      if(s[i] == '0'){
        if(fst)
          cout<<s[i];
      }
      else
        cout<<s[i];
    }
    cout<<"\n";
  }

}

int main()
{
  cout<<setprecision(6)<<fixed;
	ios_base::sync_with_stdio(0);
	cin.tie(0);


  solve();
	 
	return 0;
}
