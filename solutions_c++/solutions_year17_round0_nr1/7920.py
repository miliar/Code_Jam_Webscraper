#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <algorithm>
#include <string>
#include <fstream>
#include <time.h>
#include <sstream>
#include <vector>
using namespace std;

#pragma region defines

#ifdef __linux__// Linux
	#include <unistd.h>
	#define CLEAR system("clear"); // Clear the comand prompt (screen)
	#define SLEEP sleep(1); // Make program pause for five sec
	#define KEYPRESS cout << "Press [Enter] to continue..."; cin.ignore(); // "Press [Enter] key to continue..."
	#define BOLD cout << "\033[1m";// Make text bold
	#define RED cout << "\033[31m";
	#define BLUE cout << "\033[34m";
	#define LIGHTRED cout << "\033[91m";
	#define LIGHTBLUE cout << "\033[94m";
	#define DEF cout << "\033[39m";
#elif _WIN32// Windows
	#include <windows.h>	// Windows features
	#define CLEAR system("cls"); // Clear the comand prompt (screen)
	#define SLEEP Sleep(500); // Make program pause for five sec
	#define KEYPRESS cout << "Press any key to continue..."; _getch(); // "Press any key to continue..."
	#define BOLD ""
	#define RED cout << "";
	#define BLUE cout << "";
	#define LIGHTRED cout << "";
	#define LIGHTBLUE cout << "";
	#define DEF ""
#endif

#define LINEBREAK cout << endl; 	// Line break
#define DEBUG false 					// For debugging
#define CHECKPOINT cout << "Checkpoint" << endl;

#pragma endregion

void flip(string &S, int start, int end){
	if(DEBUG){
		cout << start << "|" << end << endl;
	}
	for(int i = start; i < end; i++){
		if( end > S.length()){
			break;
		}
		if( S[i] == '+'){
			S[i] = '-';
		}
		else{
			S[i] = '+';
		}
	}
	if(DEBUG){
		cout << "After Flips: " << S << endl;
	}
}

bool checkFlips(string S){
	for(int i = 0; i < S.length(); i++){
		if(S[i] == '-'){
			return false;
		}
	}
	return true;
}

int main(){
	int N = 0;
	int T;
	cin>>T;
	int K;
	string S;
	int flips = 0;

	while(T--){
		cin >> S >> K;
		if(DEBUG){
			cout << T << " | " << S << " | " << K << " | " << endl;
		}
		for(int i = 0; i < S.length(); i++){
			if( S[i] == '+' ){
				continue;
			}
			else if( S[i] == '-'){
				flip(S, i, i+K);
				flips++;
			}
		}
		if(checkFlips(S)){
			printf("Case #%d: %d\n", ++N, flips);
		}
		else{
			printf("Case #%d: IMPOSSIBLE\n", ++N);
		}
		flips = 0;
	}

	return 0;
}
