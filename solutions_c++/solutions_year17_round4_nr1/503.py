#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#define _USE_MATH_DEFINES
#include <math.h>
#include <string>
#include <iomanip>
using namespace std;

int main(){
	freopen("D:\\temp\\r2al.in", "r", stdin);
	freopen("D:\\temp\\r2al.txt", "w", stdout);
	int o1;
	cin>>o1;
	for (int t = 1; t <= o1; ++t){
		int n, p;
		cin>>n>>p;
		vector<int> mods(p);
		for (int i = 0; i < n; ++i){
			int a;
			cin>>a;
			++mods[a % p];
		}
		int res = mods[0];
		int del = 0;
		switch(p){
		case 2:
			res += (mods[1] + 1) / 2;
			break;
		case 3:
			del = min(mods[1], mods[2]);
			res += del;
			res += (mods[1] - del + 2) / 3;
			res += (mods[2] - del + 2) / 3;
			break;
		case 4:
			res += mods[2] / 2;
			mods[2] = mods[2] % 2;
			del = min(mods[1], mods[3]);
			res += del;
			mods[1] -= del;
			mods[3] -= del;
			if (mods[1] > 0){
				if (mods[2] > 0) mods[1] += 2;
				res += (mods[1] + 3) / 4;
			} else if (mods[3] > 0){
				if (mods[2] > 0)
				{
					if (mods[3] >= 2){ 
						++res;
						mods[3] -= 2;
						res += (mods[3] + 3) / 4;
					} else ++res;
				} else {res += (mods[3] + 3) / 4;}
			} else { res += mods[2]; }
		}
		cout<<"Case #"<<t<<": "<<res<<'\n'; //setprecision(9)<<fixed<<
	}
}