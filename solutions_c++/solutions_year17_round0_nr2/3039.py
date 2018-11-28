#include <iostream>
#include <string>

using namespace std;

int main(int argc, char const *argv[])
{
	unsigned short int casos;
	std::string numero;
	int j;
	cin >> casos;
	for (int i = 0; i < casos; ++i){
		cin >> numero;
		for ( j = numero.size() - 1; j > 0; --j)
		{
			if ( numero[j-1] > numero[j] ){
				for (int k = j; k < numero.size(); ++k){
					numero[k] = '9';
				}

				numero[j-1]--;
			}
		}

		for (j = 0; j < numero.size() && numero[j] == '0'; ++j)	;
		
		cout << "Case #" << i+1 << ": ";
		for (; j < numero.size(); ++j)	
			cout << numero[j];
		cout << '\n';
	}

	return 0;
}
