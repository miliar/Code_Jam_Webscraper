#include <iostream>
#include <fstream>

using namespace std;

string filp(string str, int position,int k)
{
	for(int i = 0; i < k; i++)
	{
		if(str[position + i] == '+')str[position + i] = '-';
		else str[position + i] = '+';
	}
	return str;
}

int allch(string str)
{
	for(int i = 0; i < str.length();i++)
	{
		if(str[i] != '+')
		{
			return 0;
		}

	}	
	return 1;
}
int main()
{
	fstream fin;
	fin.open("A-large.in.txt");
	ofstream fout("a.out"); 

	int casenum;
	fin >> casenum;
	int counter = 1;
	while(casenum--)
	{
		string str;
		fin >> str;
		int k; 
		fin >> k;
		int flipcount = 0;
		for(int i = 0; i <= str.length() - k; i++)
		{
			if(str[i] == '-')
			{
				str = filp(str,i,k);
				flipcount++;
			}
		}
		
		cout << str << endl;
		if(allch(str) == 0)fout << "Case #"<< counter++ <<": "<<"IMPOSSIBLE" << endl;
		else fout << "Case #"<< counter++ <<": "<< flipcount << endl;
	}

    fout.close(); 

    fin.close();
    return 0;
}