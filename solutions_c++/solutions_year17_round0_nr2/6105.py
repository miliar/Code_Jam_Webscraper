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
    string N;
    cin >> N;
    for(int i=N.size()-1; i>0; i--) {
      if( N[i] < N[i-1] ) {
	N[i-1]--;
	for(int j=i; j<N.size(); j++) {
	  N[j] = '9';
	}	
      }
    }

    printf("Case #%d: ", n);
    if( N[0] == '0' ) {
      for(int i=1; i<N.size(); i++) cout << N[i];
      cout << endl;
    } else {
      cout << N << endl;					     
    }
  }

}
