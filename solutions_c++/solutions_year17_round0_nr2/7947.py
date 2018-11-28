#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <string>

using namespace std;

int main() {
	FILE *fin = freopen("B-small-attempt1.in", "r", stdin);
	assert( fin!=NULL );
	FILE *fout = freopen("B-small-attempt1.out", "w", stdout);
	int T;
	string N;
	string out;
	cin >> T;

	int sol=0;

	for(int t = 0; t < T; t++){
		// Get N
		cin >> N;

		sol=0;
		int loc=-1;
		int loc2=0;
		bool odd=false;
		// Find flip
		for (int n=0; n<(int)N.size()-1; n++) {
			// Last location of increasing change
			if (N[n+1]>N[n])
				loc2=n+1;
			// First location of decreasing change
			if (N[n+1]<N[n]) {
				loc=n;
				if (N[n]=='1')
					odd=true;
				break;
			} 
		}
				
		// If the number is already ordered, return it
		if (loc<0) {		
			cout << "Case #" << t+1 << ": " << N << endl;
			continue;
		}
		// Otherwise do the calculation
		out.clear();
		
		
		for (int n=0; n<(int)N.size(); n++) {
			
			if (n<loc2) {
				if (odd) { 
					if (n==0)
						continue;
					else
						out.push_back('9');
				}
				else
					out.push_back(N[n]);
			} else {
				if (n>loc2 || odd) {
					if (odd && n==0)
						continue;
					if (n<loc)
						out.push_back(N[n]-1);
					else
						out.push_back('9');
				} else {
					if (n==loc2)
						out.push_back(N[n]-1);
					else
						out.push_back('9');
				}	
			}
		}
		cout << "Case #" << t+1 << ": ";
		//for (int i=(int)out.size()-1; i>=0; i--)
		for (int i=0; i<(int)out.size(); i++)
			cout << out[i];
		cout << endl;
		
	}
	return 0;
}
