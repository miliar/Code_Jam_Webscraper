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
	#define SLEEP sleep(5); // Make program pause for five sec
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

void tidyCheck(unsigned long long int  &N){
	string str = to_string(N);
	int temp;
	if(str.length() == 1){
		return;
	}
	for(int i = 0; i < str.length()-1; i++){
		// Not valid
		if( str[i] - '0' > str[i+1] - '0'){
			temp = str[i] - '0';
			str[i] = ( (temp-1) % 10) + '0';
			for(int j = i+1; j < str.length(); j++){
				str[j] = '9';
			}
			if(DEBUG){
				cout << "New str: " << str << endl;
			}
			i = -1;
		}
	}
	N = stoull(str);
}

int main(){
	int T, C = 0;
	unsigned long long int N;
	cin>>T;

	while(T--){
		cin>>N;
		if(DEBUG){
			cout << "N: " << N << endl;
		}
		tidyCheck(N);
		printf("Case #%d: %lld\n", ++C, N);
	}

    return 0;
}
