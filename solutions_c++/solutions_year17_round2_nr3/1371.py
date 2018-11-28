#include <iostream>
using namespace std;
int main(){
	int zes;
	cin>>zes;
	for(int i = 1; i <= zes; i++){
		int N, Q;
		cin>>N>>Q;
		double Dist[N][N];
		double Horse[N][2];
		double Dyn[N][N];
		for(int i = 0 ;i < N; i++){
			cin>>Horse[i][0]>>Horse[i][1];
		}
		for(int i = 0; i < N; i++){
			for(int j = 0; j < N; j++){
				cin>>Dist[i][j];
				Dyn[i][j] = -1;
			}
		}
		int start, end;
		cin>>start>>end;
		double DIST[N];
		DIST[0] = 0;
		for(int i = 1; i < N; i++)
			DIST[i] = DIST[i - 1] + Dist[i - 1][i];
		Dyn[0][0] = 0;
		for(int i = 1; i < N; i++){
			
			for(int j = 0; j <= i - 1; j++){
				if(Dyn[j][j] != -1){
					if(Horse[j][0] >= DIST[i] - DIST[j]){
						Dyn[j][i] = Dyn[j][j] + (DIST[i] - DIST[j])/Horse[j][1];
					}
				}
			}
			double M = 1e11;
			for(int k = 0; k < i; k++){
				if(M > Dyn[k][i] && Dyn[k][i] > 0) M  = Dyn[k][i];
			}
			Dyn[i][i] = M;

		}
		cout<<"Case #"<<i<<": ";
		cout.precision(9); 
		cout<<fixed<<Dyn[N-1][N-1]<<endl; 
	}
}
