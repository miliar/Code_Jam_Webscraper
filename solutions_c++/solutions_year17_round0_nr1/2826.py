#include <cstdlib>
#include <iostream>
#include "set"

using namespace std;

int main(int argc, char *argv[])
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int T;
    cin >> T;
    
    string S;
    int K;
    int X;

	int y;

    for (int T_i=0; T_i<T;T_i++){
		cin >> S >> K;
		if (S.length() < K) {
        cout << "Case #" << T_i+1 << ": IMPOSSIBLE" << endl;
		} else {
			y=0;
			for (int i=0; i < S.length() - K+1;i++){
				if (S[i]!='+' ){
					y++;
					for (int j=i; j<i+K;j++) 
					if (S[j]=='+') S[j]='-'; else S[j]='+';
				} 
			}
			X=0;
			for (int i=S.length()- K;i< S.length();i++ ) if (S[i]!='+') X++;
		if (X>0)
        cout << "Case #" << T_i+1 << ": IMPOSSIBLE" << endl;
        else 
        cout << "Case #" << T_i+1 << ": " << y << endl;
		}
    }
    return EXIT_SUCCESS;
}
