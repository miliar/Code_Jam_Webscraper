#include<iostream>
using namespace std;
#include<string>
string last;
#include<fstream>

int isTidy(string num)
{

	for (int i = num.length() - 1; i > 0; i--)
	{
		if (num.at(i) < num.at(i - 1))
		{
		
			return 0;
		}
		
	}
	
	return 1;
}



void lastTidy(string num)
{
	
	int t = 0;
	last = num;
	while ( last.length() >0)
	{
		if (!isTidy(last))
		{
	
			for (int j = last.length() - 1; j >= 0; j--)
			{
				if (last.at(j) > 48)
				{
					t = last.at(j);
					t--;
					last.at(j) = t;
						
						if (j == 0&& t==48)
						{
							last.resize(last.length() - 1);

							for (int k = j ; k<last.size() ; k++)
							{
								last.at(k) = 57;
							}
						}
						else
						{
							for (int k = j+1; k<last.size() ; k++)
							{
								last.at(k) = 57;
							}
						}
						
				
					
					break;
				}

				}
		}
		else
		{
	
			return;
		}
	}

}


int main()
{
	string num;
	ifstream fin;
	fstream fout;
	int T = 0;
	int t = 0;
	fin.open("B-small-attempt0.in");
	fout.open("B-small-attempt0.out", fstream::out);

	fin >> T;
	getline(fin, num, '\n');
	while (t < T)
	{
		t++;
		//cout << "Enter a Number : ";
		//cin >> num;
		getline(fin, num,'\n');
		
		lastTidy(num);

		fout <<"Case #"<<t<<": "<< last <<endl;


	}

	fin.close();
	fout.close();
	return 0;
}
