#include<iostream>
#include<fstream>

using namespace std;

const int MAX = 1000;
int T, N;
int digit[MAX + 5] = { 0 };
int counter;

void translate(int n)
{
	int temp=n;
	for (int i = 0;; i++)
	{
		digit[i] = temp % 10;
		temp /= 10;
		if (temp < 10) {
			digit[i + 1] = temp;		
			counter = i + 1;
			return;
		}
	}	
}

void swap(int a[], int n) {

	int temp1;
	for (int i = 0, j = n ; i < j; i++, j--) {
		temp1 = a[i];
		a[i] = a[j];
		a[j] = temp1;
	}
	
	return;
}

bool isright(int a[], int n)
{
	for (int i = 0; i < n; i++)
	{
		if (a[i] > a[i + 1]) return false;
	}
	return true;
}

void deleteint(int a[], int n)
{
	if (a[n ] >0) {
		a[n]--;
		return;
	}
	for (int i = n - 1; i >= 0; i--) {
		if (a[i] != 0)
		{
			a[i]--;
			i++;
			while (i <=n) {
				a[i] = 9;
				i++;
			}

			if (a[0] == 0) {
				for (int j = 0; j < n; j++)
					a[j] = a[j + 1];
				counter--;
			}
			return;
		}
	}
}

int main()
{

	ifstream fin("input.in");
	ofstream fout("output.txt");
	fin>> T;
	for (int i = 1; i <= T;i++) {
		fin >> N;
		if (N < 10) fout << "\nCase #" << i << ": " << N;
		else {
			translate(N);
			swap(digit, counter);
			while (1)
			{
				if (isright(digit,counter)) {
					fout << "\nCase #" << i << ": ";
					for (int k = 0; k <= counter; k++) fout << digit[k];
					break;
				}
				deleteint(digit, counter);
			}
			

		}


	}

}