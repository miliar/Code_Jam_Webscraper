#include <iostream>
#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <sstream>

using namespace std;

typedef long long int ll;

int T;
int K;

int check(string S){

	for(int k=0; k < S.length()-1; k++)
		    if(S[k]>S[k+1])
				return 0;

	return 1;

}
int main() {

        FILE *fin = freopen("B-small-attempt0.in", "r", stdin);
	    assert( fin!=NULL );
	    FILE *fout = freopen("B-small-attempt0.out", "w", stdout);

		cin >> T;

		for(int i=1; i<=T; i++){

			ll N;
			cin >> N;
	
			cout << "Case #" << i << ": ";
			
			if(N<10)
				cout << N << endl;
			else if(N<=1000){

				for(int j=N; j>=1; j--){

					string S = to_string(j);

					if(check(S)){
					   cout << S << endl;
				       break;
					}
				}

			}else{






			}


		}
		
		cin.clear();
		cin.ignore();
		cin.get();

		return 0;
}