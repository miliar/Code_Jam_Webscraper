#include <iostream>
#include <iomanip>
using namespace std;

int main(){
	int T, D, N, maxtindex;
	int K[2000];
	int S[2000];
	long double maxt;
	cin >> T;
	
	for(int i=0;i<T;i++){
		cin >> D >> N;
		maxt = 0;
		maxtindex = 0;
		long double t, prov_speed;
		for(int j=0;j<N;j++){
			cin >> K[j] >> S[j];
			t = 1.0*(D-K[j])/(1.0*S[j]);
			if(t>maxt){
				maxt = t;
				maxtindex = j;
			}
			else if(t==maxt){
				if(K[j]<K[maxtindex]){
					t = maxt;
					maxtindex = j;
				}
			}
		}
		prov_speed = 1.0*D/maxt;
		cout << "Case #" << i+1 << ": " << fixed << setprecision(6) << prov_speed << endl;
	}
}
