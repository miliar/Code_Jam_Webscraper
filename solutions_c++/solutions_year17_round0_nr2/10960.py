#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int get_legnth(int number) {
	string a; int b;

	a = to_string(number);
	b = a.size();
	return b;
}

bool check_tidy(int tmatrix[], int flag, int one, int two) {
	bool f = true;
	do {
		if (tmatrix[one] >= tmatrix[two]) {
			one++; two++;
		}
		else
			f = false;

	} while (f && (two <= flag));
	

	return f;
	
}


int tidy(int number) {
	
	int temp; int remainder; int back; int *arr_temp = new int[get_legnth(number)]; int flag = 0;
	int one = 0, two = 1;

	for (int o = 1; o <= number; o++) {
		
		temp = o;
		
		while (temp > 0) {
			remainder = temp % 10;
			arr_temp[flag] = remainder;
			flag++;
			temp = temp / 10;
			
		} 
		

		if (check_tidy(arr_temp, flag, one, two)) {
			back = o;
		}
		flag = 0;
	}

	delete[] arr_temp;
	arr_temp = NULL;
	return back;
}

int main() {
    
	ifstream input;
	ofstream output;

	input.open("B-small-attempt0.in");
	output.open("output.txt");
	
	int T, last_tidy;
	input >> T;
	int *N = new int[T];

	for (int i = 0; i < T; i++) {
		input >> N[i];
	}

	for (int p = 0; p < T; p++) {
		last_tidy = tidy(N[p]);
		output << "Case #" << p+1 << ": " <<  last_tidy << endl;
	}

	
   


	input.close();
	output.close();




	delete[] N;
	N = NULL;
	system("pause");
	return 0;
}