#include <iostream>
#include <vector>
#include <unordered_set>
#include <queue>
#include <algorithm>
#include <string>
#include <iomanip>
using namespace std;
#define ll longlong

int main(void) {
	string N;
	int T;
	scanf("%i", &T);
	for (int i=0;i<T;i++) {
		cin >> N;
		for (int j=N.size()-1; j>0; j--) {
			if (N[j]<N[j-1]) {
				N[j-1]--;
				for (int k=j;k<N.size();k++)
					N[k]='9';
			}
		}
		cout << "Case #" << i+1 << ": ";
		int j=0;
		while (N[j]=='0')
			j++;
		for (;j<N.size();j++)
			cout << N[j];
		cout << endl;
	}
	return 0;
}
