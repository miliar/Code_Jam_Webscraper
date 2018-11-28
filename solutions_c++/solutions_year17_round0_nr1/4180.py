#include <string>
#include <fstream>
#include <iostream>

using namespace std;
string row;
int k, c;
bool possible;
void compute(int i)
{
	if(i == row.size())
		return;
	else if(row[i] == '+')
		compute(i+1);
	else if(i+k <= row.size()) 	//devo girarlo
	{
		for(int j = i; j < i+k; j++)
			row[j] = row[j] == '+' ? '-' : '+';
		c++;
		compute(i+1);
	}
	else //impossibile
		possible = false;
}
int main()
{
	int a;
	ifstream in("A-large.in");
	ofstream out("out.txt");
	in >> a;
	for(int z = 0; z < a; z++)
	{
		out << "Case #" << z + 1 << ": ";
		in >> row;
		in >> k;
		c = 0;
		possible = true;
		//cout << row << endl;
		compute(0);
		if(possible)
			out << c << endl;
		else 
			out << "IMPOSSIBLE" << endl;
	}
	return 0;
}