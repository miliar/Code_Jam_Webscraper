#include <iostream>
#include <fstream>
#include <string>
#include <queue>
#include <map>
using namespace std;

ifstream fin("a-small.in");
ofstream fout("a-small.out");

const int PMAX = 1024;

int getint(const string &pancakes) {
	int p = 0;
	for(int i=0; i<(int)pancakes.size(); i++) {
		if(pancakes[i]=='-')
			p = p | (1<<i);
	}
	return p;
}

int flip(int p, int n, int i, int k) {
	if(i+k>n)
		return -1;
	return ( p ^ ( ((1<<k)-1)<<i ) );
}

int getnflips(const string &pancakes, int K) {
	int p = getint(pancakes);
	int n = (int)pancakes.size();
	bool visited[PMAX];
	for(int i=0; i<(1<<n); i++)
		visited[i] = false;
	queue< pair<int,int> > Q;
	Q.push(make_pair(p,0));
	while(!Q.empty()) {
		pair<int,int> node = Q.front();
		Q.pop();
		p = node.first;
		int d = node.second;
		if(visited[p])
			continue;
		visited[p] = true;
		if(p==0)
			return d;
		for(int i=0; i<=n-K; i++) {
			int next = flip(p, n, i, K);
			Q.push( make_pair(next, d+1) );
		}
	}
	return -1;
}

int main() {
	int T; fin>>T;
	for(int t=1; t<=T; t++) {
		string pancakes;
		int K;
		fin >> pancakes >> K;
		int nflips = getnflips(pancakes, K);
		fout << "Case #" << t << ": ";
		if(nflips<0)
			fout << "IMPOSSIBLE";
		else
			fout << nflips;
		fout << endl;
	}
	return 0;
}

