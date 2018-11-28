#include <iostream>
#include <string>

using namespace std;

void flip(string & v, int& n);
bool find(string::size_type &pos, string *stack, int i);
int main()
{
	int number_tests;
	unsigned int p;
	int * k = nullptr;
	string::size_type pos;
	bool xpos;
	int jok;
	cin >> number_tests;
	string *stack = nullptr;
	stack = new (nothrow)string[number_tests];
	k = new (nothrow) int[number_tests];
	//reading

	for (int i = 0; i < number_tests; i++)
	{
		cin.ignore();
		getline(cin, stack[i], ' ');
		cin >> k[i];
	}

		for (int i = 0; i < number_tests; i++)
		{
			p = 0;
			xpos = true;
			
			while (find(pos, stack, i)== true)
			{
				if (k[i] + pos > stack[i].length())
				{
					xpos = false;
					cout << "Case #" << i + 1 << ": "<< "IMPOSSIBLE" << endl;
					goto label;
					
				}
				else
				{
					for (int h = 0; h < k[i]; h++)
					{
						jok = pos + h;

						flip(stack[i], jok);
					}
					p++;
				}					
			}
			cout << "Case #" << i + 1 << ": " << p << endl;
		label:
			;
		}

		delete[] stack;
		delete[] k;
		return 0;
	}

bool find(string::size_type &pos, string *stack, int i)
{
		pos = stack[i].find_first_of('-');
		if (pos == string::npos)
		{
			return false;
		}
		return true;
}
void flip(string & v, int& n)
{
		if (v[n] == '+')
			v[n] = '-';
		else if (v[n] == '-')
			v[n] = '+';
}