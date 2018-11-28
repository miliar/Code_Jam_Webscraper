#include <iostream>
#include <gmp.h>
#include <assert.h>


using namespace std;

bool checkTidy(string nb){
	for ( int i =1; i<nb.length();i++ ){
		if ( nb[i-1] > nb[i] ){
			return false;
		}
	}	
	return true;
}

string findLastTidy(string number){
	char last[number.length()];
	mpz_t n;
	int flag;
	
	mpz_init(n);
	mpz_set_ui(n,0);
	flag = mpz_set_str(n, number.c_str(), 10);
	assert (flag == 0);
	while ( !checkTidy(number) && mpz_sgn(n) > 0 ){
		mpz_sub_ui(n, n, 1);
		mpz_get_str(last, 10, n);
		number=(string)last;
	}	
	
	mpz_get_str(last, 10, n);
	mpz_clear(n);
	return string(last);
}

string test(string number){
	char last[number.length()];
	mpz_t n;
	int flag;
	
	mpz_init(n);
	mpz_set_ui(n,0);
	
	flag = mpz_set_str(n, number.c_str(), 10);
	assert ( flag == 0 );
	mpz_sub_ui(n, n, 1);
	
	mpz_get_str(last, 10, n);
	mpz_clear(n);
	return string(last);
}

int main (int argc, char* argv[]) {
	int i=0,j;
	string number;
	cin >> j;
	for (; i<j; i++){
		cin >> number;
		/*cout << number << " " << test(number) << " ";
		cout << boolalpha << checkTidy(test(number)) << endl;;
		*/
		cout << "Case #" << i+1 << ": " << flush;
		cout << "" + findLastTidy(number) << endl;
	}
	return 0;
}
