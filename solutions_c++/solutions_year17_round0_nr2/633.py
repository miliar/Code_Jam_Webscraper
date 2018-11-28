#include <iostream>
#include <vector>
using namespace std;



int main() {
	int t;
	cin >> t;
	for(int i=1; i<=t; i++){

		long long n;
		cin >> n;
		vector<int> d, e;
		while(n>0){
			d.push_back(n%10);
			n/=10;
		}
		for(int j=1; j<d.size(); j++){
			if(d[j]>d[j-1]){
				d[j]--;
				for(int l=j-1; l>=0; l--){
					d[l] = 9;
				}
			}
		}
		while(d[d.size()-1] == 0){
			d.pop_back();
		}
		cout << "Case #" << i << ": ";
		for(int j = d.size()-1; j>=0; j--){
			cout << d[j];
		}
		cout << endl;

	}
	return 0;
}
