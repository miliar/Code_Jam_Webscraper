#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<vector>
#include<map>
#include<unordered_map>
#include<set>
#include<unordered_set>
#include<cstring>
#include<queue>
#include<deque>
#include<stack>
#include<algorithm>
#include<climits>
#include<string>
#include<sstream>
#include<cmath>
#include<cctype>
#include<iomanip>
#include<list>
#include<conio.h>

using namespace std;

typedef pair <int, int> PII;
typedef pair <int, double> PID;
typedef pair <double, double> PDD;
typedef vector <int> VI;
typedef vector <double> VD;
typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;

#define MP make_pair
#define PB push_back
#define PPB pop_back
#define PF push_front
#define PPF pop_front
#define EL endl
#define CO cout

bool isTidy(ll x){
	while(x > 0){
		ll a = x % 10;
		x /= 10;
		if(a < (x%10)) return false;
	}
	return true;
}

void solve(){
	ll N;
	cin >> N;
	ll maxi = 1;
	for(ll i = 1;i <= N;i++){
		if(isTidy(i)){
			maxi = i;
		}
	}
	cout << maxi <<endl;
}
int main() {
    freopen("B-small-attempt0.in","r",stdin);
    freopen("a.out","w",stdout);
	int T;
	cin>>T;
	for (int t=1;t<=T;t++){
		cout<<"Case #"<<t<<": ";
        solve();
	}
	getch();
	return 0;
}
