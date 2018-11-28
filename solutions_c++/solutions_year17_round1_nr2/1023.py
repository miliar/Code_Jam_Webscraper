#include <iostream>
#include <algorithm>
using namespace std;
int x[55];
int y[55][55];
int z[55];
int main(){

	int t,n,p;
	cin >> t;
	for(int i =1 ;i<=t;i++){

		cin >> n >> p;
		for(int j=0;j<n;j++){
			cin >> x[j];

		}
		for(int j=0;j<n;j++){
			for(int k =0;k<p;k++){
				cin >> y[j][k];
			}
		}

		for(int j =0;j<n;j++){
			sort( &y[j][0] , &y[j][0]+p);
		}

		for(int j=0;j<n;j++){
			z[j] = 0;
		}

		bool chk = true;
		int count = 0;
		int pro = 1;
		int cou = 0;
		int cou1 = 0;
		bool chk1 = false;
		while(chk){
			chk1 = true;
			cou = 0;
			cou1 = 0;
			for(int j = 0;j<n;j++){
				//cout << y[j][z[j]] << endl;
				if(y[j][z[j]] < 0.9*pro*x[j]) {
					z[j]++;
					chk1 = false;
				}else if ( y[j][z[j]] > 1.1*pro*x[j]){
					chk1 = false;
					cou++;
				}else cou1++;

			}
			if(chk1) {
				count++;
				for(int j=0;j<n;j++){
					z[j]++;
					//cout << y[j][z[j]] << endl;
				}
			}
			if(cou+cou1 == n && !chk1){
				pro++;
			}
			for(int j =0;j<n;j++){
				if(z[j]>=p) chk=false;
			}
			
			//cout << " pro" << pro << endl;


		}
		cout << "Case #" << i << ": " << count << endl; 


	}





	return 0;
}