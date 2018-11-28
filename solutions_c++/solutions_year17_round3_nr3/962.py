#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

int T, N, K;
double P[60];
double U;
std::vector< pair<double, int> > V;

int main(){

	cin >> T;
	for(int t=0;t<T;t++){
		cin >> N >> K >> U;
		double prob = 1;
		for(int i=0;i<N;i++){
			cin >> P[i];
		}

		sort(P, P+N);
		reverse(P, P+N);
		for(int i=0;i<N;i++)
			V.push_back(make_pair(P[i], 1));
		
		for(int i=N-1;i;i--)
			if((V[i-1].first - V[i].first) * V[i].second <= U){
				V[i-1].second += V[i].second;
				U -= (V[i-1].first - V[i].first) * V[i].second;
				V.pop_back();
			}
			else{
				V[i].first += U / V[i].second;
				U = 0;
				break;
			}
		if(U > 0)
			V[0].first += U / V[0].second;
		for(int i=0;i<V.size();i++){
			// cout << V[i].first << " " << V[i].second << endl;
			prob *= pow(V[i].first, V[i].second);
		}

		cout << "Case #" << t+1 << ": ";
		printf("%.8lf\n", prob);
		V.clear();
	}
}