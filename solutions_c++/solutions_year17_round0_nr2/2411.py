/*
ID: meetdi1
PROG: gift1
LANG: C++
*/
#include <iostream>
#include <fstream>
#include <string>


using namespace std;



int main() {
	//ofstream fout("outp.txt");
	//ifstream fin("gift1.in");
	//ifstream fin("input.txt");
	int T;// N, Nn;

	cin >> T;
	for (int i = 0; i < T; i++)
	{
		char str[22] = { 0, };
		char ostr[22] = { 0, };
		int k = 0, j = 0, M, curr, curr_i, o_i=0, t=0, change =0;
		//int d[10] = { 0, }, t, m = 1;
		cin >> str;
		//fin >> N;
		M = strlen(str);
		curr = str[0];
		curr_i = 0;
		for (t = 0; t < (M -1) ; t++)
		{
			if ( str[t] == str[t + 1])
			{

			}
			else if (str[t] < str[t + 1])
			{
				
				for (int mm = curr_i; mm <= t; mm++)
				{
					ostr[o_i++] = str[mm];
				}
				curr = str[t + 1];
				curr_i = t + 1;
				if (t + 2 == M)//last element
				{
					ostr[o_i] = curr;
				}
			}
			else
			{// t is larger than t+1
				change = 1;
				curr--;
				if (curr == '0')
				{
					M--;
					for (int tt = 0; tt < M; tt++)
					{
						ostr[o_i++] = '9';
					}
				}
				else
				{
				//	for (int tt = curr_i; tt <= t; tt++)
					{
						ostr[o_i++] = curr;
						curr_i++;
					}
					for (int tt = curr_i; tt < M; tt++)
					{
						ostr[o_i++] = '9';
					}
					
				}
				break;
			}
		}
		if (M == 1 || change == 0)
		{
			cout << "Case #" << i + 1 << ": " << str << endl;
		}
		else
		{
			cout << "Case #" << i + 1 << ": " << ostr << endl;
		}
		
	}
	return 0;
}