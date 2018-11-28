
#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <string>
#include <cstring>
#include <cmath>
#include <bitset>
#include <stack>
#include <vector>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <ctime>
#include <cstring>
#include <list>
#include <iomanip>
#include <cassert>
#include <functional>	

const double EPS = 0.00000001;
const long long mod = 1000000000 + 7;
using namespace std;
#define ll long long
#define ull unsigned long long
#define mk make_pair

//----------------------------

#define cin fin
//
#define cout fout

//----------------------------

#ifdef cin fin
ifstream fin("in.in");
#endif
#ifdef cout
ofstream fout("out.out");
#endif



int main() {
	ios::sync_with_stdio(0);
	int t, z = 1;
	cin >> t;
	while(t--){
		cout << "Case #" << z++ << ": ";
		
		ll n;
		cin >> n;

		stringstream ss;
		ss << n;
		string a = ss.str();
		if(a.size() == 1){
			cout << n << endl;
			continue;
		}

		for (int i = (int) a.size() - 2; i >= 0; i--){
			if(a[i] > a[i + 1]){
				a[i] = a[i] - 1;
				for(int j = i + 1; j < a.size(); j++) a[j] = '9';
			}
		}
		ll ans;
		stringstream sss;
		sss << a;
		sss >> ans;
		cout << ans << endl;
	}
	return 0;
}