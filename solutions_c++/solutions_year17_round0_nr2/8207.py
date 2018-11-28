#include <iostream>
#include <regex>
#include <fstream>
#include <string>
using namespace std;


bool check( string str ) {

	for(int i = 0 ; i < str.length(); i++) {

		if( i+1 < str.length() && str[i + 1] < str[i] )
			return 0;
	
	}

	return true;

}
string genNumber( string str ) {

	if(check(str) )
		return str;


	int cnt = 0;

	for (int i = 1; i < str.length()  && cnt == 0; ++i)
		if(str[i] < str[i - 1])
			cnt = i;

	for( int i = cnt; i < str.length()  ; i++) {
		str[i] = '9';
	}

	for( int i = cnt - 1 ; i >= 0 ; i-- ) {

		if( i > 0 && str[i] == str[i - 1] ) {
			str[i] = '9';
		}
		else {

			int dig = str[i] - '0';

			dig--;
			str[i] = (char) (dig + '0');
			break;
		}

	}

	if( str[0] == '0')
		str = str.substr(1,20); 

	return str;
}

int main() {

	long T;

	string n;
	cin >> T;

	ofstream outfile;
   	outfile.open("ans.txt");


	for (int currentTest = 0; currentTest < T; ++currentTest)
	{
		outfile << "Case #" << (currentTest+1) << ": ";

		cin >> n;

		outfile << genNumber(n) << endl;


	}

	outfile.close();


	return 0;
}