#include <cstdlib>
#include <iostream>
#include "set"
#include <map>
#include <iomanip>

using namespace std;

int main(int argc, char *argv[])
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int T,N;
    int R,O,Y,G,B,V;
    int Rn,Yn,Bn;
    int Rnn,Ynn,Bnn;

	string S;
//	std::map<int,int>::iterator IT = MAP.begin();

	cin >> T;
	int y;
	int MAX;
	char MAX_c;
	int MAX2;
	char MAX2_c;
	int MAX3;
	char MAX3_c;
	char CC;
	char CC_OLD;
	bool IMP;
    for (int T_i=0; T_i<T;T_i++){
		cin>> N >> R >> O >> Y >> G >> B >> V;
		
		Rnn = R + O + V;
		Ynn = O + Y + G;
		Bnn = G + B + V;

		S = "";
		CC_OLD = ' ';
		IMP = true;
		for (int N_i=0; N_i < N; N_i ++) {
			if (IMP) {
	
			Rn = (R + O + V) * 1000 + Rnn;
			Yn = (O + Y + G) * 1000 +Ynn;
			Bn = (G + B + V) * 1000 +Bnn;

			MAX = 0;
			MAX2 = 0;
			MAX3 = 0;
			if (Rn > MAX) { 
				MAX = Rn;
				MAX_c = 'R';				
			}
			if (Yn > MAX) { 
				MAX = Yn;
				MAX_c = 'Y';				
			}
			if (Bn > MAX) { 
				MAX = Bn;
				MAX_c = 'B';				
			}

			if ((Rn > MAX2) && (MAX_c != 'R') ){ 
				MAX2 = Rn;
				MAX2_c = 'R';				
			}
			if ((Yn > MAX2) && (MAX_c != 'Y') ) { 
				MAX2 = Yn;
				MAX2_c = 'Y';				
			}
			if ((Bn > MAX2) && (MAX_c != 'B') ) { 
				MAX2 = Bn;
				MAX2_c = 'B';				
			}

			if ((Rn > MAX3) && (MAX_c != 'R')  && (MAX2_c != 'R')){ 
				MAX3 = Rn;
				MAX3_c = 'R';				
			}
			if ((Yn > MAX3) && (MAX_c != 'Y') && (MAX2_c != 'Y') ) { 
				MAX3 = Yn;
				MAX3_c = 'Y';				
			}
			if ((Bn > MAX3) && (MAX_c != 'B')  && (MAX2_c != 'B')) { 
				MAX3 = Bn;
				MAX3_c = 'B';				
			}

			CC = ' ';
			if ((MAX_c == 'R') && (MAX2_c == 'Y') && (O>0) && ( (CC_OLD == 'B' )  || (CC_OLD == ' ') ) && (CC ==' ')) {
				CC = 'O';
				O--;
			}
			if ((MAX_c == 'Y') && (MAX2_c == 'R') && (O>0) && ( (CC_OLD == 'B' )  || (CC_OLD == ' ') ) && (CC ==' ')) {
				CC = 'O';
				O--;
			}

			if ((MAX_c == 'Y') && (MAX2_c == 'B') && (G>0) && ( (CC_OLD == 'R' )  || (CC_OLD == ' ') ) && (CC ==' ')) {
				CC = 'G';
				G--;
			}
			if ((MAX_c == 'B') && (MAX2_c == 'Y') && (G>0) && ( (CC_OLD == 'R' )  || (CC_OLD == ' ') ) && (CC ==' ')) {
				CC = 'G';
				G--;
			}

			if ((MAX_c == 'R') && (MAX2_c == 'B') && (V>0) && ( (CC_OLD == 'Y' )  || (CC_OLD == ' ') ) && (CC ==' ')) {
				CC = 'V';
				V--;
			}
			if ((MAX_c == 'B') && (MAX2_c == 'R') && (V>0) && ( (CC_OLD == 'Y' )  || (CC_OLD == ' ') ) && (CC ==' ')) {
				CC = 'V';
				V--;
			}

			if ((MAX_c == 'R') && (R>0) && ((CC_OLD == 'Y' ) || (CC_OLD == 'G') || (CC_OLD == 'B') || (CC_OLD == ' '))  && (CC ==' ')) {
				CC = 'R';
				R--;
			}
			if ((MAX_c == 'Y') && (Y>0) && ((CC_OLD == 'R' ) || (CC_OLD == 'B') || (CC_OLD == 'V')|| (CC_OLD == ' ')) && (CC ==' ')) {
				CC = 'Y';
				Y--;
			}
			if ((MAX_c == 'B') && (B>0) && ((CC_OLD == 'R' ) || (CC_OLD == 'O') || (CC_OLD == 'Y')|| (CC_OLD == ' ')) && (CC ==' ')) {
				CC = 'B';
				B--;
			}



			if ((MAX3_c == 'R') && (MAX2_c == 'Y') && (O>0) && ( (CC_OLD == 'B' )  || (CC_OLD == ' ') ) && (CC ==' ')) {
				CC = 'O';
				O--;
			}
			if ((MAX3_c == 'Y') && (MAX2_c == 'R') && (O>0) && ( (CC_OLD == 'B' )  || (CC_OLD == ' ') ) && (CC ==' ')) {
				CC = 'O';
				O--;
			}

			if ((MAX3_c == 'Y') && (MAX2_c == 'B') && (G>0) && ( (CC_OLD == 'R' )  || (CC_OLD == ' ') ) && (CC ==' ')) {
				CC = 'G';
				G--;
			}
			if ((MAX3_c == 'B') && (MAX2_c == 'Y') && (G>0) && ( (CC_OLD == 'R' )  || (CC_OLD == ' ') ) && (CC ==' ')) {
				CC = 'G';
				G--;
			}

			if ((MAX3_c == 'R') && (MAX2_c == 'B') && (V>0) && ( (CC_OLD == 'Y' )  || (CC_OLD == ' ') ) && (CC ==' ')) {
				CC = 'V';
				V--;
			}
			if ((MAX3_c == 'B') && (MAX2_c == 'R') && (V>0) && ( (CC_OLD == 'Y' )  || (CC_OLD == ' ') ) && (CC ==' ')) {
				CC = 'V';
				V--;
			}




			if ((MAX2_c == 'R') && (R>0) && ((CC_OLD == 'Y' ) || (CC_OLD == 'G') || (CC_OLD == 'B')|| (CC_OLD == ' ')) && (CC ==' ')) {
				CC = 'R';
				R--;
			}
			if ((MAX2_c == 'Y') && (Y>0) && ((CC_OLD == 'R' ) || (CC_OLD == 'B') || (CC_OLD == 'V')|| (CC_OLD == ' ')) && (CC ==' ')) {
				CC = 'Y';
				Y--;
			}
			if ((MAX2_c == 'B') && (B>0) && ((CC_OLD == 'R' ) || (CC_OLD == 'O') || (CC_OLD == 'Y')|| (CC_OLD == ' ')) && (CC ==' ')) {
				CC = 'B';
				B--;
			}

			if ((MAX3_c == 'R') && (R>0) && ((CC_OLD == 'Y' ) || (CC_OLD == 'G') || (CC_OLD == 'B')|| (CC_OLD == ' ')) && (CC ==' ')) {
				CC = 'R';
				R--;
			}
			if ((MAX3_c == 'Y') && (Y>0) && ((CC_OLD == 'R' ) || (CC_OLD == 'B') || (CC_OLD == 'V')|| (CC_OLD == ' ')) && (CC ==' ')) {
				CC = 'Y';
				Y--;
			}
			if ((MAX3_c == 'B') && (B>0) && ((CC_OLD == 'R' ) || (CC_OLD == 'O') || (CC_OLD == 'Y')|| (CC_OLD == ' ')) && (CC ==' ')) {
				CC = 'B';
				B--;
			}
			
			if (CC != ' ') {
				CC_OLD = CC;
				S = S + CC;
			}
			else {
				IMP =false;
			}
			}
		}
		
		CC_OLD = S[0];
		if ((CC == 'R') && ((CC_OLD == 'R') || (CC_OLD == 'O') || (CC_OLD == 'V'))) IMP = false;
		if ((CC == 'Y') && ((CC_OLD == 'O') || (CC_OLD == 'Y') || (CC_OLD == 'G'))) IMP = false;
		if ((CC == 'B') && ((CC_OLD == 'G') || (CC_OLD == 'B') || (CC_OLD == 'V'))) IMP = false;

		if ((CC == 'O') && ((CC_OLD != 'B'))) IMP = false;
		if ((CC == 'G') && ((CC_OLD != 'R'))) IMP = false;
		if ((CC == 'V') && ((CC_OLD != 'Y'))) IMP = false;
		
		
		if (IMP) {
        cout << "Case #" << T_i+1 << ": " << S << endl;
		} else {
        cout << "Case #" << T_i+1 << ": IMPOSSIBLE"  << endl;
		}
    }
    return EXIT_SUCCESS;
}
