#include "stdafx.h"
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <map>
#include <vector>
#include <set>
#include <string>

#include <strstream>

using namespace std;


int _tmain(int argc, _TCHAR* argv[])
{
	int T;
	cin >> T;
	for(int NumCase=1; NumCase <=T; NumCase++) {
		cout << "Case #" << NumCase << ": ";

		long long int Number;
		cin >> Number;

		long long int Tidy=Number;
		strstream NumStream;

		NumStream << Number;
		string NumString;
		NumStream >> NumString;

		NumString = "0" + NumString;


		for(string::iterator p= NumString.begin(); (p+1) != NumString.end(); p++)
			if ( *(p+1) < *p) { 
				*(p) = *(p)-1;
				p++;
				for(; (p) != NumString.end(); p++)
					*p='9'; 
				break;
			}


		for(string::reverse_iterator p= NumString.rbegin(); (p+1) != NumString.rend(); p++)
			if ( *(p+1) > *p) { 
				*p='9'; 
				*(p+1) = (*(p+1))-1;
			}

		for(string::iterator p= NumString.begin(); (p+1) != NumString.end(); p++)
		if (*p == '0'){
			*p=' ';
		}
		else
			break;

		NumStream.clear();
		NumStream << NumString;
		NumStream >> Number;

		cout << Number;
		cout << endl;
	}
 	return 0;
}
