#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
#include <map>
#include <cmath>
 
#define rep(i,n) for(int i = 0;i < (n);i++)
#define repp(i,a,n) for(int i = (a);i < (n);i++)
#define all(x) (x).begin(),(x).end()
#define pb(x) push_back(x)
#define mp(a,b) make_pair(a,b)

using namespace std;

typedef long long int ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ll> vl;
typedef vector<pair<int, int> > vpi;
typedef vector<pair<ll, ll> > vpl;

int main(){
	cin.tie(0);
	ios::sync_with_stdio(false);
	int t;
  cin >> t;
  rep(i,t){
    string s;
    cin >> s;
    int pre = (int)(s[0]-'0');
    repp(j, 1, (int)s.size()){
      if((int)(s[j]-'0') < pre){
        s[j] = '9';
        s[j-1] = (char)(pre-1+'0');
        if(j > 1){
          pre = (int)(s[j-2]-'0');
          j-=2;
        }else{
          if(s[0] == '0'){
            string ans = "";
            rep(l,(int)s.size()-1) ans += "9";
            s = ans;
            break;
          }
          pre = '9';
        }
      }else{
        pre = (int)(s[j]-'0');
      }
    }

    cout << "Case #" << i+1 << ": " << s << endl;
  }
	return 0;
}
