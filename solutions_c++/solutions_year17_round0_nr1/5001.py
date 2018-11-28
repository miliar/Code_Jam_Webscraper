#include <iostream>
#include <cstdlib>
#include <vector>
#include <queue>
using namespace std;
#define MAX_SIZE 1027

int main() {
	ios_base::sync_with_stdio(0);

	int T;
	cin>>T;

	for(int tt=1; tt<=T; tt++) {
		string S;
		int K;		
		cin>>S>>K;
		
		int result = 0;
		for(int i=0; i<S.length()-K+1; i++) {
			if(S[i] == '-') {
				result++;
				for(int j=0; j<K; j++)
					if(S[i+j] == '-')
						S[i+j] = '+';
					else
						S[i+j] = '-';
			}
		}

		for(int i=0; i<S.length(); i++)
			if(S[i] == '-')
				result = -1;


		cout<<"Case #"<<tt<<": ";
		if(result != -1)
			cout<<result;
		else
			cout<<"IMPOSSIBLE";
		cout<<endl;

	}
	return 0;
}