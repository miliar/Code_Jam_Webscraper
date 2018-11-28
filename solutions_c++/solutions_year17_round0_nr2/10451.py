#include <algorithm>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <climits>
#include <numeric>

using namespace std;

bool check(int n){
	bool c = true;
	int rem;
	int last = n%10;
			while(n!=0){

				rem=n%10;
				n=n/10;
				if(last >= rem) {
					c= true;
					last = rem;
				}
				else {c = false;
						break;
				}
			}

			return c;
}

int main() {


	freopen("B-small-attempt0.in","r", stdin);
	freopen("out.out","w", stdout);

	int test_cases;
	cin >> test_cases;
	int n,last;

	for (int test_case = 1; test_case <= test_cases; test_case++) {
			cin>>n;
			last =1;
			for(int i=1; i<=n;  i++){
					if(check(i)) last = i;
					else continue;

			}
	
		cout << "Case #" << test_case << ": " << fixed << setprecision(10) << last << endl;
		cout.flush();
	}

	fclose(stdout);
	fclose(stdin);
	return 0;
}