#include <fstream>
#include <string>

using namespace std;
long long n;
string number;
bool corr()
{
	bool b, corretto = true;
	for(int i = number.size() - 1; i > 0 && corretto; i--)
	{
		b = number[i] >= number[i-1];
		corretto = corretto && b;
	}
	return corretto;
}
int main()
{
	int a;
	ifstream in("B-small-attempt0.in");
	ofstream out("out.txt");
	in >> a;
	for(int i = 0; i < a; i++)
	{
		out << "Case #" << i+1 << ": ";
		in >> n;
		number = to_string(n);
		while(!corr())
		{
			n--;
			number = to_string(n);
		}
		out << n << endl;
	}
	return 0;
}