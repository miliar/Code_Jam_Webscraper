#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int test;
	cin >> test;
	for(int j=0;j<test;j++) {	
		int horsesAhead;
		long totalDist;
		cin >> totalDist >> horsesAhead;

		long atKm;
		int maxspeed;
		double ans=0.0;
		for(int i=0;i<horsesAhead;i++) {
			cin >> atKm >> maxspeed;
			long prod = maxspeed*totalDist;
			int diff = totalDist - atKm;
			//cout << "Diff: " << diff << " prod: " << prod << endl;
			double temp = (double)prod/diff;
			if(ans==0.0 || ans > temp)
				ans = temp;
		}
		cout << "Case #" << j+1 << ": " << std::fixed << ans << endl;
	}
	return 0;
}
