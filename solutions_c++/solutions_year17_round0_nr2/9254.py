#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>

using namespace std;  // since cin and cout are both in namespace std, this saves some text

bool IsTidy(char N[]);

int main() {
	int T,j,k;
	char N[20];
	char Tidy[20];
	int TEST = 0;
	cin >> T;  // read t. cin knows that t is an int, so it reads it as such.

	for (int i = 1; i <= T; ++i) {

	cin >> N;  // read n and then m.

	strcpy(Tidy,N);
	
	for(j=strlen(Tidy) ; j>1 ; j--)
	{
		if(Tidy[j-2] > Tidy[j-1])
		{
			if(Tidy[j-2] != '0')
				Tidy[j-2]--;
			else
				Tidy[j-2]='9';

			for(k=j-1 ; k<strlen(Tidy) ; k++)
				Tidy[k] = '9';
		}
	}
	if(Tidy[0] == '0')
		cout << "Case #" << i << ": " << Tidy+1 << endl;
	else
		cout << "Case #" << i << ": " << Tidy << endl;
    // cout knows that n + m and n * m are ints, and prints them accordingly.
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.

  }
  return 0;
}