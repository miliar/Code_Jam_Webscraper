#include<iostream>
#include<vector>
#include <iomanip>
using namespace std;
int main(){
	std::cout << std::setprecision(10) << std::fixed;
	freopen("output.txt","w",stdout);
	int T;
	cin>>T;
	for(int t=1;t<=T;t++){
		cout<<"Case #"<<t<<": ";
		int N,K;
		cin>>N>>K;
		double U;
		cin>>U;
		vector<double> P(N);
		for (int i = 0; i < N; ++i){
			cin>>P[i];
		}
		double answer;
		if(N>1){
			sort(P.begin(),P.end());
			int i = 0;
			while(U>0 && i<N-1){
				while(i<N-1 && P[i] == P[i+1]){
					i++;
				}
				if(i != N-1){
					if(U >= (i+1)*(P[i+1]-P[i]) ){
						U -= (i+1)*(P[i+1]-P[i]);
						for (int j = 0; j <= i; ++j){
							P[j] = P[i+1];
						}
						// i++;
					}else{
						double u = U/(i+1);
						for (int j = 0; j <= i; ++j){
							P[j] += u;
						}
						U=0;
					}
				}
				if(i==N-1){
					double u = U/(i+1);
					for (int j = 0; j <= i; ++j){
						P[j] += u;
					}
					U=0;
				}
			}
			answer = P[0];
			for (i = 1; i < N; ++i){
				answer*=P[i];
			}
		}else{
			answer = P[0]+U;	
		}
		if(answer>1.0){
			answer = 1;
		}
		cout<<answer<<endl;
	}
}