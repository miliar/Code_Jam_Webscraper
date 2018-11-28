#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(void) {
	int t; cin >> t;
	for(int cn=1; cn<=t; cn++) {
		int n, k; cin >> n >> k;
		int last;
		vector<int> indexes;
		indexes.push_back(1);
		indexes.push_back(n+2);
		while(k-->0) {
			int i1, i2, mdiff=-1;
			for(int i=0; i<indexes.size()-1; i++)
				if(indexes.at(i+1)-indexes.at(i)>mdiff) {
					i1=indexes.at(i);
					i2=indexes.at(i+1);
					mdiff=i2-i1;
				}
			last=(i2+i1)/2;
			indexes.push_back(last);
			sort(indexes.begin(),indexes.end());
		}
		int md=-1,Md=-1;
		for(int i=0; i<indexes.size()-1; i++) 
			if(indexes.at(i)==last) {
				md=last-indexes.at(i-1);
				Md=indexes.at(i+1)-last;
			}
		cout << "Case #" << (int) cn << ": " << (int) (Md-1) << " " << (int) (md-1) << endl;
	}
	return 0;
}
