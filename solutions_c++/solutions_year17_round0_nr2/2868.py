#include <cstdlib>
#include <iostream>
#include "vector"
#include <string>
#include <fstream>

using namespace std;

char sub(char a)
{
	switch(a) {
		case '0': return ' ';
		case '1': return '0';
		case '2': return '1';
		case '3': return '2';
		case '4': return '3';
		case '5': return '4';
		case '6': return '5';
		case '7': return '6';
		case '8': return '7';
		case '9': return '8';

	}
	return '0';

}
//
// main function
//
int main()
{
  int Tests, count = 0; // Counting which test case
  cin >> Tests; // Taking input
  
  ofstream output;
  output.open("tidyNumbersout.txt");

  while(Tests != 0)
  {
  	count++;
  	Tests--;

  	string main;
  	cin >> main;

  	 for(int i = main.length() - 1; i >= 0; i-- )
  	 {
  	 	if(i && main[i] < main[i - 1])
  	 	{
  	 		int j = i;
  	 		while(j < main.length())
  	 		{
  	 			main[j] = '9';
  	 			j++;
  	 		}
  	 		main[i - 1] = sub(main[ i - 1]);
  	 	}
  	 }
  	   	 if(main[0] == '0')
  	   	 	main = main.substr(1,main.length() - 1);

  	   	 output << "Case #" << count << ": " << main << endl;
  }
}