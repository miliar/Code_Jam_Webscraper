#include <cstdlib>
#include <iostream>
#include <cstring>
#include <algorithm>
#include <iomanip>
#include <fstream>
using namespace std;
int T; 
int N;
int K;
double U;
double P[55];


int main(){
	fstream in;
	fstream out;
	out.open("output.txt",ios::out);
	in.open("input.txt",ios::in);
	in >> T;
	for(int tc = 1; tc <= T; ++tc){
		in >> N >> K;
		in >> U;
		for(int i = 0; i < N; ++i)
			in >> P[i];
		sort(P,P+N);
		double sum = 0;
		double ans = 0;
		for(int i = 0; i < N; ++i){
			sum+= P[i];
			double tmpans = 1;
			double Y = min(1.000000000,(sum + U)/(i+1));
			if(Y >= P[i]){
				for(int j = 0; j < i+1; ++j)
					tmpans*= Y;
				for(int j = i+1; j < N; ++j)
					tmpans*= P[j];
			}else tmpans = 0;
			ans = max(ans,tmpans);
			//cout << Y << " " << tmpans << endl;
		}
		out << setprecision(7) << fixed << "Case #" << tc << ": " << ans << endl;
	}
}
	

