#include <iostream>
#include <stdio.h>
#include <map>
#include <string>
#include <iomanip>
using namespace std;


int main()
{
	freopen("flat.in","r",stdin);
	freopen("flat.out","w",stdout);
	int n,unit;
	cin >> n >> unit;
	map<string, int> flat;
	flat["bedroom"] = 0;
	flat["bathroom"] = 0;
	flat["kitchen"] = 0;
	flat["balcony"] = 0;
	flat["other"] = 0;
	int num;
	string type;
	int sum = 0;
	for(int i = 0; i <  n; ++i)
	{
		cin >> num >> type;
		flat[type] += num;
		sum += num;
	}
	cout << sum << endl;
	cout << flat["bedroom"] << endl;
	double money = (sum - flat["balcony"] * 0.5) * unit;
	cout << fixed << setprecision(6) << money << endl;
}
