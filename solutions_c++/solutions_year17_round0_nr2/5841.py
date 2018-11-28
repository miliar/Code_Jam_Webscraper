#include <iostream>
#include <string>
#include <map>
#include <fstream>

using namespace std;


int main()
{
	
	ofstream of;
	of.open("input.in");


	int n;
	cin >> n;

	for (int i = 1; i <= n; i++)
	{
		string in;
		cin >> in;
		int index = 0;
		while (index < in.length() - 1 && in[index] <= in[index+1]) { index++; }
		
		if (index == in.length() - 1) { of << "Case #" << i << ": " << in << "\n"; }
		else if(index==0&&in[index]=='1') {
			of << "Case #" << i << ": ";
			for (int k = 0; k < in.length() - 1; k++)
			{
				of << "9";
			}
			of << "\n";
		
		
		}
		else if (index == 0) {
			of << "Case #" << i << ": "<<(char)(in[0]-1);
			for (int k = 0; k < in.length() - 1; k++)
			{
				of << "9";
			}
			of << "\n";
		}
		else {
			//index--;
			while (index > 0 && in[index] == in[index-1]) { index--; }
			if (index == 0 && in[index] == '1') {
				of << "Case #" << i << ": ";
				for (int k = 0; k < in.length() - 1; k++)
				{
					of << "9";
				}
				of << "\n";


			}
			else if (index == 0) {
				of << "Case #" << i << ": " << (char)(in[0] - 1);
				for (int k = 0; k < in.length() - 1; k++)
				{
					of << "9";
				}
				of << "\n";
			}
			else
			{
				of << "Case #" << i << ": ";
				for (int k = 0; k < index; k++) { of << (in[k]); }
				of << (char)(in[index] - 1);
				for (int k = index+1; k < in.length(); k++)
				{
					of << "9";
				}
				of << "\n";

			}


		}
		

	}

	of.close();

	return 0;
}