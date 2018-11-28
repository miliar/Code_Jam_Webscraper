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

	int y;
	string N;
	string R;
	int N_len;
	int N_i;
	int N_j;
    for (int T_i=0; T_i<T;T_i++){
		cin >> N;
		N_i=0;
		N_len = N.length();
		N = N + '9';
		R = "";
		while (N_i < N_len) {
			if (N[N_i] <= N[N_i + 1]) {
				N_i ++;
			} else {
				N[N_i] = N[N_i] -1;
				for (int ii=N_i+1; ii < N_len; ii++) N[ii] = '9';
				if (N_i > 0) {
					N_j = N_i;
					while (N_j > 0){
						if (N[N_j-1] > N[N_j]) {
							for (int ii=N_j; ii < N_len; ii++) N[ii] = '9';
							N_j--;
							N[N_j]--;
						} else {
							N_j=0;
						}
					}
				}
			}
		
		}
		for (int i=0;i < N_len; i++){
			if (N[i]!='0') 	R = R + N[i];
		}
        cout << "Case #" << T_i+1 << ": " << R << endl;
    }
    return EXIT_SUCCESS;
}
