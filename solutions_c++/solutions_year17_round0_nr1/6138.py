#include<bits/stdc++.h>
using namespace std;
#define int long long
#define pb push_back 
#define mp make_pair
#define fr first
#define sc second
#define Rep(i,n) for(int i=0;i<(n);i++)
#define All(v) v.begin(),v.end()
typedef pair<int, int> Pii; typedef pair<int, Pii> Pip;
const int INF = 1107110711071107;

main()
{
  int T, n = 0;
  cin >> T;
  
  while( T-- ) {
    n++;
    string S;
    int K, cnt = 0;
    
    cin >> S >> K;
    Rep(i, S.size()-K+1) {
	if( S[i] == '-' ) {
	  cnt++;
	  for(int j=i; j<i+K; j++) {
	    if( S[j] == '+' ) S[j] = '-';
	    else S[j] = '+';
	  }
	}
    }

    bool flag = true;
    Rep(i, S.size()) {
      if( S[i] == '-' ) {
	flag = false;
	break;
      }
    }

    printf("Case #%d: ", n);
    if( flag ) {
      cout << cnt << endl;
    } else {
      cout << "IMPOSSIBLE" << endl;
    }

  }

}

 

    
  
	 
	 
