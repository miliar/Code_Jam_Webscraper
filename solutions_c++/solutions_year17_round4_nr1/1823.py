#include <iostream>
#include <vector>

using namespace std;

int main() {
	int T;
	cin >> T;
	for (int it=1;it<=T;++it) {
		int N, P;
		cin >> N >> P;
		
		vector<int> types(P, 0);		

		while (N--){
 			int G;
			cin >> G;
			++types[G%P];
		}
		int ret=types[0];
		if (P==2) {
			ret+=(types[1]+1)/2;
		} else {
			if (P==4) {ret+=types[2]/2; types[2]%=1;}

			int minsta = types[1]<types[P-1]?types[1]:types[P-1];

			ret+=minsta;
			types[1]-=minsta;
			types[P-1]-=minsta;


			//Left is maybe one 2 if P=4 and the rest either 1:s or P-1:s

			if (P==3) {
				ret+=(2+types[1]+types[2])/3;
			}
			if (P==4) {
				ret+=(3+types[1]+types[3]+2*types[2])/4;
			}
		}
			

		cout << "Case #" << it << ": " << ret << endl;
	}
}