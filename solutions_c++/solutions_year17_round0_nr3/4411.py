#include <cstdlib>
#include <iostream>
#include <cstring>
#include <fstream>
#include <algorithm>
#include <queue>
using namespace std;
int T;
typedef long long ll;
int N,K;
int main(){
	fstream in;
	fstream out;
	out.open("output.txt",ios::out);
	in.open("input.txt",ios::in);
	in >> T;
	for(int tc = 1; tc <= T; ++tc){
		priority_queue<int> pq;
		in >> N >> K;
		pq.push(N);
		int l = 0;
		int r = 0;
		for(int i = 0; i < K; ++i){
			//cout << i << ". PQ SIZE: " <<  pq.size() << endl;
			int x = (pq.top()); pq.pop();
			x--;
			l = x/2;
			r = x - x/2;
			//cout << "Removed " << x+1 << " and pushing " << l << " " << r << endl;
			pq.push(l);
			pq.push(r);
		}
		out << "Case #" << tc << ": " << r << " " << l << endl;
	}

}
