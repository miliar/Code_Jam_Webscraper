#include <iostream>
using namespace std;
typedef long long ll;

ll T, N, Q, E[105], S[105], D[105], U, V;
double TT[105];

double Process_delivery(ll U, ll V){
	for(int i=0; i<105; i++){
		TT[i]=0;
	}
	for(int i=0; i<N; i++){
		double minTT = (i==U) ? 0 : 1e11;
		for(int j=0; j<i; j++){
			// with the horse from city j, time taken to reach city i
			E[j]-=D[i-1];
			if(E[j]<0){
				cerr<<"Horsefail: "<<j<<endl;
				continue;
			}
			cerr<<"Before: "<<TT[j]<<endl;
			TT[j] = TT[j] + (double(D[i-1]) / double(S[j]));
			cerr<<"Horse "<<j<<" to city "<<i<<" in "<<TT[j]<<endl;
			minTT = minTT<TT[j] ? minTT : TT[j];
		}
		TT[i]=minTT;
		cerr<<"City "<<i<<": "<<TT[i]<<endl;
	}
	return TT[V];
}

int main(){
	cin>>T;
	cout << fixed;
	cout.precision(7);
	for(int i=1; i<=T; i++){
		cin>>N>>Q;
		for(int j=0; j<N; j++){
			cin>>E[j]>>S[j];
		}
		for(int j=0; j<N; j++){
			int input;
			for(int k=0; k<N; k++){
				cin>>input;
				if(input!=-1){
					D[j]=input;
					cerr<<j<<" "<<input<<endl;
				}
			}
		}
		string ans;
		for(int j=0; j<Q; j++){
			cin>>U>>V;
			ans+=" "+to_string(Process_delivery(U-1, V-1));
		}
		cout<<"Case #"<<i<<":"<<ans<<endl;
	}
}