#include <iostream>
#include <cstring>
#include <cmath>
#include <fstream>
#include <queue>
using namespace std;
int T; int N, K;
int main() {
    ifstream cin("cjam2017p3in.txt");
    ofstream cout("cjam2017p3out.txt");
	cin>>T;
	for (int t=1; t<=T; t++) {
		cin>>N>>K;
		priority_queue<int> q;
		q.push(N);
		for (int i=0; i<K-1; i++) {
			int b=q.top();
			q.pop();
			if (b%2) {
				q.push(b/2);
				q.push(b/2);
			} else {
				q.push(b/2-1);
				q.push(b/2);
			}
		}
		int last=q.top();
		cout<<"Case #"<<t<<": "<<(last)/2<<" "<<(last-1)/2<<"\n";
	}
}
