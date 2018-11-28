#include <iostream>
#include <string>
#include <fstream>

using namespace std;

long long int getlegnth(long long int number) {
	string a; 
	long long int b;
	a = to_string(number);
	b = a.size();
	return b;
}

bool isTidy(long long int tmatrix[], long long int flag, long long int one, long long int two) {
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

long long int tidy(long long int number) {
	long long int temp; long long int remainder; 
	long long int back;
	long long int *arr_temp = new long long int[getlegnth(number)]; 
	long long int flag = 0;
	long long int one = 0, two = 1;
	for (long long int o = 1; o <= number; o++) {
		temp = o;
		while (temp > 0) {
			remainder = temp % 10;
			arr_temp[flag] = remainder;
			flag++;
			temp = temp / 10;
		}
		if (isTidy(arr_temp, flag, one, two)) {
			back = o;
		}
		flag = 0;
	}
	delete[] arr_temp;
	arr_temp = NULL;
	return back;
}

int main() {
	ifstream in;
	ofstream out;
	in.open("B-small-attempt2.in");
	out.open("out.txt");
	long long int totalNum, tidyNum;
	in >> totalNum;
	long long int *Num = new long long int[totalNum];
	for (long long int i = 0; i < totalNum; i++) {
		in >> Num[i];
	}
	for (long long int i = 0; i < totalNum; i++) {
		tidyNum = tidy(Num[i]);
		out << "Case #" << i + 1 << ": " << tidyNum << endl;
	}
	in.close();
	out.close();
	delete[] Num;
	Num = NULL;
	return 0;
}