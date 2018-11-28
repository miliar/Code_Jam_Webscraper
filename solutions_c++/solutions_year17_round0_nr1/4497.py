#include <iostream>
#include <string>
using namespace std;

int cnt = 0;
int f;
void flip(string& cake, int idx)
{
	for (int i = idx; i < idx + f; i++)
	{
		if (cake[i] == '-') cake[i] = '+';
		else cake[i] = '-';
	}
	cnt++;
}


void process(int tc)
{
	string cake;
	cnt = 0;
	cin >> cake >> f;

	for (int i = 0; i < cake.size() - (f - 1); i++)
	{
		if (cake[i] == '-') flip(cake, i);
	}


	for (int i = cake.size() - (f - 1); i < cake.size(); i++)
	{
		if (cake[i] == '-') {
			cout << "Case #" << tc << ": IMPOSSIBLE" << endl;
			return;
		}
	}
	cout << "Case #" << tc << ": " << cnt << endl;
}
int main()
{
	int C;
	cin >> C;
	for (int i = 0; i < C; i++) process(i + 1);
	return 0;
}





