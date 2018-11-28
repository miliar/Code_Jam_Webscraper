#include <algorithm>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <sstream>
#include <functional>
#include <map>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <set>
#include <list>
#include <numeric>
using namespace std;
const double PI = 3.14159265358979323846;
const double EPS = 1e-12;
const int INF = 1<<25;
typedef pair<int,int> P;
typedef long long ll;
typedef unsigned long long ull;


int main(){
	int T;
	cin>>T;
	for(int Case = 1; Case <= T; Case++){
		ll n, k;
		cin>>n>>k;
		ll a = n, an = 1, bn = 0;
		ll i = 1;
		while(2*i<=k){
			i *= 2;
			if(a%2==0){
				bn *= 2;
				bn += an;
			} else {
				an *= 2;
				an += bn;
			}
			a = (a-1)/2;
		}
		k -= i-1;
		ll c = (k<=bn)?a+1:a;
		cout<<"Case #"<<Case<<": "<<c/2<<" "<<(c-1)/2<<endl;

	}
	return 0;
}

