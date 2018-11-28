#include <iostream>
#include <stdio.h>
#include <string>
#include <math.h>
#include <vector>
#include <stdlib.h>

using namespace std;

int compare (const void * a, const void * b)
{
	return ( *(int*)a - *(int*)b );
}


vector<int> nlist(long long number) {
	vector<int> ans;
	long long temp = number;
	int i;
	if (temp == 0) {
		ans.push_back(0);
	}
	
	while (temp > 0) {
		i = temp%10;
		temp = (long long) ((long long) temp - i)/10;
		ans.push_back(i);
	}
	
	return ans;
}


void * solve(){
	void * ans;
	long long lnumber;
	vector<int> nrl;
	int sz, i, j;
		
	cin >> lnumber;
		
	if (lnumber == 0) {
		cout << 0;
		return ans;
	}
	
	nrl = nlist(lnumber);
	sz = nrl.size();
	
	for (i = 0; i < sz - 1; i++) {
		if (nrl[i + 1] > nrl[i]) {
			nrl[i + 1] = nrl[i + 1] - 1;
			for (j = 0; j < i + 1; j++) {
				nrl[j] = 9;
			}
		}
	}
	
	if (nrl[sz - 1] != 0) {
		printf("%d",nrl[sz - 1]);
	}
	
	for (i = sz - 2; i > -1; i--) {
		printf("%d", nrl[i]);
	}
	
	return ans;
}



int main (int argc, char * const argv[]) {
    int ncases, cases;
	scanf("%d\n", &ncases);
	for (cases = 0; cases < ncases; cases++) {
		cout << "Case #" << cases + 1 << ": ";
		solve();
		cout << endl;
	}
    return 0;
}