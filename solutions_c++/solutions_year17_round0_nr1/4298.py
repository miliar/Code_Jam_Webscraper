#include <cstdlib>
#include <iostream>
#include <cstring>
#include <fstream>
using namespace std;
int T;
string x;
int F[1234];
int S[1234];
int K;
int N;
int main(){
	fstream in;
	fstream out;
	out.open("output.txt",ios::out);
	in.open("input.txt",ios::in);
	in >> T;
	for(int tc = 1; tc <= T; ++tc){
		bool can = true;
		int ans = 0; int cur = 0;
		in >> x >> K;
		N = x.length();
		for(int i = 0; i < N; ++i)
			if(x[i] == '+') S[i] = 0;
			else S[i] = 1;
		
		for(int i = 0; i <= N - K; ++i){
			if( i - K >= 0 && F[i-K] == 1) cur = 1 - cur;
			if(((S[i] + cur) % 2) == 1){
				F[i] = 1;
				ans++;
				cur = 1 - cur;
			}else{
				F[i] = 0;
			}
		}
		
		for(int i = N-K+1; i < N; ++i){
			if( i - K >= 0 && F[i-K] == 1) cur = 1 - cur;
			if(((S[i] + cur) % 2) == 1){
				can = false;
			}else{
				F[i] = 0;
			}
		}
		if(can)	out << "Case #" << tc << ": " << ans << endl;
		else out << "Case #" << tc << ": IMPOSSIBLE" << endl;
		
		
	}
	
}
