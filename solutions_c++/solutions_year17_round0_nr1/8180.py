#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int arr[1050];
int n,k,cntMin;


bool check() {
	for(int i = 0 ; i < n; i++) {
		if(arr[i] == 0)
			return 0;
	}
	return 1;
}

bool print() {
	for(int i = 0 ; i < n; i++) {
		cout << arr[i] << "";
	}

	cout << endl;
}

int slidingWindow() {

	int cnt = 0;
	
	for(int i = 0 ; i <= n - k; i++) {

		if(arr[i] == 0) {

			for(int j = 0; j < k; j++) {

				arr[i+j] = 1 - arr[i+j];

			}

			cnt++;
		
		}

	}

	cntMin = cnt;
}

int main() {

	long T;
	string str;
	cin >> T;

	ofstream outfile;
   	outfile.open("ans.txt");


	for (int currentTest = 0; currentTest < T; ++currentTest)
	{
		outfile << "Case #" << (currentTest+1) << ": ";

		cin >> str >> k;

		n = str.length();
		cntMin = 999999;

		for(int i = 0;  i< n; i++) {
			arr[i] = str[i] == '+';
		}

		slidingWindow();

		if(!check()) 
			outfile << "IMPOSSIBLE ";
		else
			outfile << cntMin << " ";
		
		outfile << endl;
		


	}

	outfile.close();

	return 0;
}