#include <iostream>
#include <sstream>
#include <string>
#include <cmath>

using namespace std;
int main()
{
	int n;
	cin >> n;
	for (int i=0;i<n;i++){
		long long m;
		long long ans = 0;
		int t = 0;
		cin >> m;
		for (int j=18;j>0;j--){
			long long p = 0;
			p = stoll(string(j, '1'));
			int s = m/p;
			if(t+s>9){
				s = 9-t;
			}
			t += s;
			ans += s * p;
			m -= s * p;
			if(t == 9){
				break;
			}
		}
		cout << "Case #" << i+1 << ": ";
		cout << ans <<endl;

	}
}



