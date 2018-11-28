#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <cstdlib>
#include <stdio.h>
#include <string>
#include <list>
#include <vector>
#include <queue>
#include <utility>
#include <math.h>
#include <float.h>
#include <bitset>
#include <iomanip>
#define for0(i,n) for(int i=0; i<n; i++)
#define for1(i,n) for(int i=1; i<n; i++)
#define FOR(i,o,n,s) for(int i=0; i<n; i+=s)
#define refor0(i,n) for(int i=n-1; i>=0; i--)
#define pb push_back
using namespace std;  // since cin and cout are both in namespace std, this saves some text

int main() {
	int dataNum;
	cin >> dataNum;

	int i, j, k;
	FOR(i, 0, dataNum, 1) {
		double destination;
		double horse;
		cin >> destination;
		cin >> horse;

		double longestTime=0.0;
		FOR(j, 0, horse, 1) {
			double start;
			double speed;
			cin >> start;
			cin >> speed;
			double consume=(destination-start)/speed;
			if(consume > longestTime) {
				longestTime=consume;
			}
			//cout << start<<" "<<speed<<endl;
		}
		//if(longestTime==0.0) cout<<"aa "<<destination<<" "<<horse<<endl;;
		cout << "Case #"<<i+1<<": "<<fixed<<setprecision(6)<<destination/longestTime<<endl;
	}

	return 0;
}