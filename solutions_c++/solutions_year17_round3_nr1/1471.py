#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

const double pi = 3.1415926535897;

double plate(double rad){
	return rad * rad * pi;
}

double side(double rad, double hi){
	return 2 * pi * rad * hi;
}

int main(){
	int zes;
	cin>>zes;
	for(int i = 1; i <= zes;i++){
		int N, K;
		cin>>N>>K;
		vector<pair<int, int>> G;
		for(int i = 0; i < N; i++){
			int r, h;
			cin>>r>>h;
			pair<int, int> o = make_pair(r, h);
			G.push_back(o);
		}
		double result = 0;
		sort(G.begin(), G.end());
		vector<pair<int, int>> V;
		for(int i = N - 1; i >= 0; i--){
			V.push_back(G[i]);
		}
		double temp = 0;
		for(int i = 0; i <= N - K; i++){
			temp = 0;
			temp += plate(V[i].first);
			temp += side(V[i].first, V[i].second);
			double T[N - i - 1];
			for(int j = 0; j < N -i - 1; j++){
				T[j] = side(V[i + 1 + j].first, V[i + 1 + j].second);		
			}
			sort(T, T + N - i - 1);
			for(int j = N - i - 2; j >= N - i - K; j--){
				temp += T[j];
			}
			if(temp > result) result = temp;
		}
		cout<<"Case #"<<i<<": ";
		cout.precision(9); 
		cout<<fixed<<result<<endl;
	}
}
