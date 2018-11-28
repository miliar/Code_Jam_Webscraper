#include <bits/stdc++.h>

#define mt make_tuple
#define mp make_pair
#define pb push_back

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ii> vii;
typedef vector<string> vs;

void test(){
  ld d;
  int n;
  cin >> d >> n;
  ld ans = -1;
  for(int i = 0 ; i < n ; i++){
    ld a, b;
    cin >> a >> b;
    ans = (ans < 0) ? (b*d)/(d-a) : min(ans,(b*d)/(d-a));
  }
  cout << setprecision(20);
  cout << ans << endl;
}

int main(){
    int t;
    cin >> t;
    for( int i = 1;i<= t;i++){
        cout << "Case #" << i << ": ";
        test();
    }
	return 0;
}
