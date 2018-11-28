#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>

using namespace std;

void tidyv(vector<int> &v) {
	int l = v.size();
	int i = l-1;
	i--;
	while(true) {
		if(i < 0) break;
		else if(v[i] >= v[i+1]) i--;
		else {
			for(int j=0; j<=i; j++) v[j] = 9;
			v[i+1] = v[i+1]-1;
			tidyv(v);
			break;
		}
	}
}

long long int tidy(long long int n) {
	if(n < 10) return n;
	long long int res = 0;
	vector<int> v;
	while(n != 0) {
		v.push_back(n%10);
		n /= 10;
	}
	tidyv(v);
	for(int i=v.size()-1; i>=0; i--) {
		res *= 10;
		res += v[i];
	}
	return res;
}

int main(int argc, char *args[]) {
    if (argc == 2 && strcmp(args[1], "small") == 0) {
        freopen("small.in","rt",stdin);
        freopen("small.out","wt",stdout);
    }
    else if (argc == 2 && strcmp(args[1], "large") == 0) {
        freopen("large.in","rt",stdin);
        freopen("large.out","wt",stdout);
    }

		int t;
		long long int n;
    cin>>t;
    for(int i=1; i<t+1; i++) {
				cin >> n;
				printf("Case #%d: ", i);
				cout << tidy(n) << endl;
    }
    return 0;
}
