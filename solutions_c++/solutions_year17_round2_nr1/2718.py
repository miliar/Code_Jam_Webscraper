#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <map>
#include <unordered_map>
#include <set>
#include <unordered_set>
#include <cstring>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <climits>
#include <string>
#include <sstream>
#include <cmath>
#include <cctype>
#include <iomanip>
#include <list>
#include <conio.h>

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

void solve(){
	ld D, N;
	cin>>D>>N;
	vector<ld> Ki, Si;
	for(int i=0;i<N;i++){
		int k, s;
		cin>>k>>s;
		Ki.push_back(k);
		Si.push_back(s);
	}
	vector<ld> turtle;
	for(int i=0;i<N;i++){
		turtle.push_back((D-Ki[i])/Si[i]);
	}
	ld maxi = *max_element(turtle.begin(),turtle.end());
	cout<<fixed<<setprecision(6)<<D/maxi<<endl;
	return;
}
int main() {
   freopen("A-large.in","r",stdin);
   freopen("a.txt","w",stdout);
	int T;
	cin>>T;
	for (int t=1;t<=T;t++){
		cout<<"Case #"<<t<<": ";
        solve();
	}
	getch();
	return 0;
}
