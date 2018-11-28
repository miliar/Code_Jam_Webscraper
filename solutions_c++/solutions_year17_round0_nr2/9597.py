#include<iostream>
#include<string>
#include<fstream>
#pragma warning ( disable : 4996 )
using namespace std;

int decimal[18];
string filename="B-small-attempt5.in";
int main() {

	ifstream fin(filename); // 파일 입력

	int T;
	//cin >> T;
	fin >> T;
	for (int i = 1; i <= T; i++) {

		for (int i = 0; i < 18; i++)
			decimal[i] = 0;

		string N;
		fin >> N;
		//		cin >> N;
		int length = N.length();
		if (length == 1)
			cout << "Case #" << i << ": " << N << endl;
		else {

			for (int j = 0; j < length; j++)
			{
				decimal[j] = N.at(j) - 48;
			}
			int de_count = 0;
			int st=0;
			for (int j = 0; j < length-1; j++)
			{
				if (decimal[j] == decimal[j + 1]) {
					st++;
					de_count++;
					if (j == length - 2) de_count++;
				}
				else if (decimal[j] > decimal[j + 1]) {
					
					if (st == 0)
					{
						decimal[j]--;
						de_count++;
					}
					else {
						if (j - st == 0)
						{
							decimal[0]--;
							de_count = 1;
						}
						else{
						decimal[j-st]--;
						de_count = de_count - st;
						}
					}
					break;
				}
				else {
					st = 0;
					de_count++;
					if (j == length - 2) de_count++;
				}
			}
			string temp="";
			string temp2="";
			
			for (int j = 0; j < de_count; j++)
			{
				int k = 0;
				if (decimal[j] == 0 && k == j) {
					k++;
				}
				else {
					temp2=to_string(decimal[j]);
					temp = temp + temp2;
				}
			}
			for (int j = 0; j < length - de_count; j++) temp = temp+"9";
			
			cout << "Case #" << i << ": " << temp << endl;



		}
	}
	system("pause");
}
