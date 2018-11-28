#include <cstdio>
#include <iostream>
#include <vector>

using namespace std;

vector<double> k, s;
int main() {

    int TC;
    cin >> TC;

    for (int tc = 1; tc <= TC; tc++) {
	double d;
	int n;

	cin >> d;
	cin >> n;
	for (int i = 0; i < n; i++) {
	    int tk, ts;
	    cin >> tk >> ts;
	    k.push_back((double)tk);
	    s.push_back((double)ts);
	}

	double result = -1;
	for (int i = 0; i < n; i++) {
	    double tmp = k[i]*s[i]/(d-k[i]) + s[i];
	    if (result == -1)
		result = tmp;
	    else 
		result = min(result, tmp);
	}

	printf("Case #%d: %.6lf\n", tc, result);
	k.clear();
	s.clear();
    }
    
    return 0;
}
