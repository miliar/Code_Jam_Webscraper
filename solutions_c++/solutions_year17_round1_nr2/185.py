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

int n, p;
int r[64];
int q[64][64];
int mi[64][64];
int ma[64][64];
int pos[64];

int main(){
	int tt; cin >> tt;
	for (int zz = 1; zz <= tt; zz++){
		cin >> n >> p;
		for (int i = 0; i < n; i++)
			cin >> r[i];
		for (int i = 0; i < n; i++)
			for (int j = 0; j < p; j++)
				cin >> q[i][j];
		for (int i = 0; i < n; i++)
			sort(q[i],q[i]+p);
		for (int i = 0; i < n; i++){
			for (int j = 0; j < p; j++){
				mi[i][j] = (q[i][j]*10+11*r[i]-1)/(11*r[i]);
				ma[i][j] = (q[i][j]*10)/(9*r[i]);
				//cout << mi[i][j] << "," << ma[i][j] << " ";
			}
			//cout << endl;
		}
			
		bool done = false;
		int cnt = 0;
		memset(pos,0,sizeof(pos));
		while (!done){
			int choice = -1;
			for (int i = 0; i < n; i++)
				if (mi[i][pos[i]] > choice){
					choice = mi[i][pos[i]];
				}
			//cout << "choice = " << choice << endl;
			bool okay = true;
			for (int i = 0; i < n; i++)
				if (ma[i][pos[i]] < choice){
					okay = false;
					pos[i]++;
					if (pos[i] == p) done = true;
				}
			if (okay){
				for (int i = 0; i < n; i++){
					//cout << pos[i] << " ";
					pos[i]++;
					if (pos[i] == p) done = true;
				}
				//cout << endl;
				cnt++;
			}
		}
		cout << "Case #" << zz << ": " << cnt << endl;
	}
	
	return 0;
}
