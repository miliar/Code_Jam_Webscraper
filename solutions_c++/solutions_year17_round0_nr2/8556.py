#include <vector>
#include <queue>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <deque>

#include <cassert>
#include <cmath>
#include <cstring>
#include <cstdio>
#include <cstdlib>

#include <algorithm>
#include <functional>
#include <string>
#include <tuple>
#include <utility>

#include <iostream>
#include <sstream>

using namespace std;

#define forn(i,n) for(int i=0;i<(int)(n); i++)
#define forsn(i,s,n) for(int i=(s);i<(int)(n); i++)
#define esta(x,v) (find((v).begin(),(v).end(),(x)) !=  (v).end())
#define index(x,v) (find((v).begin(),(v).end(),(x)) - (v).begin())
#define debug(x) cout << #x << " = "  << x << endl

typedef long long tint;
typedef unsigned long long utint;
typedef vector<tint> vi;

void imprimirVector (vi &v){
	if (!v.empty()){
		int p = v.size();
		cout << "[";
		forn(i,p-1)
			cout << v[i] << ",";
		cout << v[p-1] << "]" << endl;
	}else
		cout << "[]" << endl;
}

tint MAXN = 1000000000000000000;

int main(){
  //cout << MAXN << endl;
  
	tint T; cin >> T;
  forn(CASE,T) {
    string num; cin >> num;
    reverse(num.begin(), num.end());
    
    forsn(i,1,num.size()){
      if (num[i] > num[i-1]) {
        num[i] -= 1;
        forn(j,i) {
          num[j] = '9';
        }
      }
    }
    reverse(num.begin(), num.end());
    
    tint res = stol(num);
    //cout << res << endl;
    cout << "Case #" << CASE+1 << ": " << res << "\n";
  }
	return 0;
}
