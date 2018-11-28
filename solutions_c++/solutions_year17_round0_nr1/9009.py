#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
#include <map>
#include <cmath>
 
#define rep(i,n) for(int i = 0;i < (n);i++)
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
    int k;
    cin >> s >> k;
    int count = 0;
    rep(j, (int)(s.size())-k+1){
      if(s[j] == '-'){
        for(int l=j;l < k+j;l++){
          if(s[l] == '-'){
            s[l] = '+';
          }else if(s[l] == '+'){
            s[l] = '-';
          }
        }
        count++;
      }
    }
    bool flag = false;
    rep(j,(int)s.size()){
      if(s[j] == '-'){
        flag = true;
        break;
      }
    }
    if(!flag)
      cout << "Case #" << i+1 << ": " << count << endl;
    else
      cout << "Case #" << i+1 << ": IMPOSSIBLE" << endl;
  }
	return 0;
}
