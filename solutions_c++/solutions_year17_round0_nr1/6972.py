#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>
using namespace std;
#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
typedef long long ll;
#define INF (1<<29)

int main(){
	int tc, K;
  string s;
	cin >> tc;
	for(int i=0;i<tc;i++){
    int ans=0;
		cin >> s >> K;
    for(int j=0;j<s.length()-K+1;j++){
      if(s[j]=='-'){
        for(int k=0;k<K;k++){
          if(s[j+k]=='-')s[j+k]='+';
          else s[j+k]='-';
        }
        ans++;
      }
    }
    bool x=true;
    for(int j=0;j<s.length();j++)if(s[j]=='-')x=false;

		if(x)cout << "Case #" << i+1 << ": " << ans << endl;
    else cout << "Case #" << i+1 << ": IMPOSSIBLE" << endl;;
	}
	return 0;
}
