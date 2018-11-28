
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


char a[30][30];
		
int n, m;


void f(){
	for (int i = 0; i < n; i++){
		for(int j = 0; j <m;j++){
			cout << a[i][j];
		}
		cout << endl;
	}
}

int main() {
	ios::sync_with_stdio(0);
	int t, z = 1;
	cin >> t;
	while(t--){
		cout << "Case #" <<z++<<":"<<endl;
		cin >> n >> m;

		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++) cin >> a[i][j];

	    for(int i = 1; i < n; i++)
			for (int j = 0; j < m; j++)
				if(a[i][j] == '?') a[i][j] = a[i - 1][j];

		for (int i = n - 2; i >= 0; i--)
			for (int j = 0; j < m; j++)
				if(a[i][j] == '?') a[i][j] = a[i + 1][j];
		
		for (int j = 1; j < m; j++)
			for(int i = 0; i < n; i++) 
				if(a[i][j] == '?') a[i][j] = a[i][j - 1];

		for (int j = m - 2; j >= 0; j--)
			for (int i= 0; i< n; i++)
				if(a[i][j] == '?') a[i][j] = a[i][j + 1];
		f();
	}
	return 0;
}