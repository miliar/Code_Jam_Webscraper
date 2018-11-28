#include <cmath>
#include <ctgmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <queue>
#include <ctgmath>
#include <fstream>
using namespace std;

typedef long long ll;


int t;
ll n, digit1, digit2, cum1, cum2, lg;
bool flag;

ifstream fin("2.in");
ofstream fout("2.out");

int main() {

	fin >> t;

	for (int a = 0; a < t; a++) {

		flag = 1;

		if (n < 10) {
			fout << "Case #" << a + 1 << ": " << n << endl;
			continue;
		}

		ll lg = 10;

        while (10*lg <= n) lg*= 10;

        while(flag){
    		for (ll i = lg; i>1; i /= 10) {
    		    if (i>n) continue;
    			cum1 = (ll)n / i;
    			cum2 = (ll)n /(i/10);
    			digit1 = cum1 % 10;
    			digit2 = cum2 % 10;
    			if (digit1 > digit2) {
    			    n = (ll)cum1*i-1;
    				break;
    			}
    		}
    		if(digit1 <= digit2) flag = 0;
        }

		fout << "Case #" << a + 1 << ": " << n << endl;

	}

	fin.close();
	fout.close();

	return 0;
}
