#include <stdio.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <map>
#include <set>
#include <cmath>
#include <sstream>
#include <stack>
#include <string.h>
#include <list>
#include <time.h>

#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define PI 3.14159265358979
#define forn(i, n) for(int i = 0; i < n; ++i)
#define ALL(x) x.begin(), x.end()
#define L(s) (int)((s).size())
#define sz(s) (int)((s).size())
#define ms(x) memset(x,0,sizeof(x))
#define ms1(x) memset(x,-1,sizeof(x))
#define del(y,x) erase(y.begin()+x)

typedef long long ll;
using namespace std;
typedef pair<int,int> pii;
const int INF = 2147483647;
const ll LLINF = 9223372036854775807LL;
const int ST = 100010;
const int ST1 = 1000010;
const ll MOD = 1000000007;

ll ABS(ll a) {
    if(a<0)
        return a*(-1);
    else
        return a;
}


string conv(string a){
	if(L(a)==1)
		return a;
	for(int i = 0;i <L(a)-1;i++){
		if(a[i] > a[i+1]){
			string b = a;
			for(int j = i+1;j < L(a);j++){
				b[j] = '9';
			}
			for(int j = i;j>=0;j--){
				if(b[j]=='0'){
					b[j] = '9';
				}else{
					b[j] = b[j]-1;
					break;
				}
			}
			string c = "";
			bool was = false;
			for(int j = 0;j <L(b);j++){
				if(b[j]!='0'){
					was = true;
					c+=b[j];
				}else{
					if(was){
						c+=b[j];
					}
				}
			}
			return conv(c);
		}
	}
	return a;
}
int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	int T;
	cin >> T;
	int test = 0;
	while(test++<T){
		string t;
		cin >> t;
		string ans = conv(t);

		printf("Case #%d: ",test);
		cout << ans << endl;
	}

    return 0;
}