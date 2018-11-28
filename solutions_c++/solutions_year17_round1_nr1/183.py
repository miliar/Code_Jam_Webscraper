#include <iostream>
#include <iomanip>
#include <string>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <ctime>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <deque>
#include <bitset>
#include <algorithm>
#include <utility>
#include <complex>

using namespace std;
typedef long long ll;
typedef double ld;

typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef complex<ll> pt;

string cake[32];
char output[32][32];

int r,c;
int le[32];
//int right[32];
int mi;

int main(){
	int tt; cin >> tt;
	for (int zz = 1; zz <= tt; zz++){
		cin >> r >> c;
		memset(output,'0',sizeof(output));
		memset(le,-1, sizeof(le));
		//memset(right,-1, sizeof(right));
		for (int i = 0; i < r; i++){
			cin >> cake[i];
			for (int j = 0; j < c; j++){
				if (le[i] == -1 && cake[i][j] != '?')
					le[i] = j;
				//if (cake[i][j] != '?')
				//	right[i] = j;
				output[i][j] = cake[i][j];
			}
		}
		mi = -1;
		
		for (int i = 0 ; i < r; i++){
			if (le[i] == -1) continue;
			if (mi == -1) mi = i;
			char curr = output[i][le[i]];
			for (int j = 0; j < c; j++){
				if (output[i][j] == '?')
					output[i][j] = curr;
				else curr = output[i][j];
			}
		}
		int pos = mi;
		for (int i = 0; i < r; i++){
			if (le[i] == -1){
				for (int j = 0; j < c; j++)
					output[i][j] = output[pos][j];
			}
			else pos = i;
		}

		cout << "Case #" << zz << ":" << endl;
		for (int i = 0; i < r; i++){
			for (int j = 0; j < c; j++)
				cout << output[i][j];
			cout << endl;
		}
	}
	
	return 0;
}
