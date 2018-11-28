#include <iostream>
#include <iomanip>
#include <string>

using namespace std;

int main(){
	int cases;
	cin>>cases;

	for (int cas=1; cas<=cases; ++cas){
		cout << "Case #"<<cas << ": ";

		long long D,N;
		cin>>D>>N;

		double arrive=0.0;

		for (int i=0;i<N;++i){
			long long K,S;
			cin>>K>>S;

			arrive = max(arrive, (double)(D-K)/(double)S);
		}

		cout << setprecision(10) << (double)D/arrive << endl;



	}
}

