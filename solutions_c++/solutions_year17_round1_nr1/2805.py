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
	int R, C;
	char S[25][25];
	bool XX[1000];
	
	int R_start, C_start, R_end, C_end;
	char In;
	char Ot;
		
	int y;
    for (int T_i=0; T_i<T;T_i++){
		cin >> R >> C;
		for (int i=0; i < R ;i++) {
			for (int j=0; j < C; j++){
				cin >> S[i][j];	
			}
		}

		for (int i=0; i < 1000;i ++) XX[i]=false;

		R_start =-1;
		C_start =-1;
		R_end = 0;
		C_end = 0;
		In = ' ';
		for (int i=0; i < R ;i++) {
			for (int j=0; j < C; j++){
				if (In ==' ') {
					if (S[i][j] == '?') {
						if (R_start ==-1){
							R_start = i;
							C_start = j;
						}
					} else {
						if ((XX[S[i][j]] == false)) {
						In = S[i][j];
						if (R_start ==-1){
							R_start = i;
							C_start = j;
						}
					}
					} 
				} else {
					if ((In != S[i][j])  && (S[i][j] != '?')  )  {
						if ((XX[In] == false)) {
						XX[In] = true;
						R_end = i;
						Ot = In;
						while ((Ot == In) && (R_end < R)) {
							for (int x=C_start; x < j; x++) {
								S[R_end][x] = In;
							}	
							R_end ++;
							if (R_end < R) {
								for (int x=C_start; x< j;x++){
									if (( S[R_end][x] != In) && (S[R_end][x] != '?'))	Ot = S[R_end][x];								
								}
							}
						}

						R_end = i;
						Ot = In;
						while ((Ot == In) && (R_end >= 0)) {
							for (int x=C_start; x < j; x++) {
								S[R_end][x] = In;
							}	
							R_end --;
							if (R_end >= 0) {
								for (int x=C_start; x< j;x++){
									if (( S[R_end][x] != In) && (S[R_end][x] != '?'))	Ot = S[R_end][x];								
								}
							}
						}
						}

						In = S[i][j];
							R_start = i;
							C_start = j;
					}
				}
			}
			if ((In != ' ') && (In != '?') && (XX[In] == false)) {
						XX[In] == true;
						R_end = i;
						Ot = In;
						while ((Ot == In) && (R_end < R)) {
							for (int x=C_start; x < C; x++) {
								S[R_end][x] = In;
							}	
							R_end ++;
							if (R_end < R) {
								for (int x=C_start; x< C;x++){
									if (( S[R_end][x] != In) && (S[R_end][x] != '?'))	Ot = S[R_end][x];								
								}
							}
						}

						R_end = i;
						Ot = In;
						while ((Ot == In) && (R_end >= 0)) {
//							cout << "Masuk "  << C_start << endl;
							for (int x=C_start; x < C; x++) {
								S[R_end][x] = In;
							}	
							R_end --;
							if (R_end >= 0) {
//								cout << "CEK" << endl;
								for (int x=C_start; x< C;x++){
									if (( S[R_end][x] != In) && (S[R_end][x] != '?'))	Ot = S[R_end][x];								
//									cout << S[R_end][x];
								}
//								cout << "END CEK" << endl;
							}
//							cout << "in " << In << " Ot " << Ot << endl;
						}

			} 
			
			In = ' ';
			C_start = -1;						
			R_start = -1;						
			

		}


				
        cout << "Case #" << T_i+1 << ":"  << endl;
		for (int i=0; i < R ; i++) {
			for (int j=0; j < C; j++){
				cout << S[i][j];	
			}
			cout << endl;
		}
    }
    return EXIT_SUCCESS;
}
