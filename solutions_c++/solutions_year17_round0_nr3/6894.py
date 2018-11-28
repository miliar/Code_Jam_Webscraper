#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
	int numberOfInput;
	cin >> numberOfInput;
	for(int i = 0; i < numberOfInput; i++)
	{
		int stall;
		cin >> stall;
		vector<int> set;
		set.push_back(stall);
		int people;
		cin >> people;
		int a;
		int b;
		for(int k = 0; k < people; k++)
		{
			int temp = set[set.size() - 1];
			a = temp/2;
			b = temp - (temp/2) - 1;
			set.erase(set.begin() + set.size() - 1);
			set.push_back(a);
			set.push_back(b);
			sort(set.begin(), set.end());
		}
		cout << "Case #" << i+1 << ": " << a << ' ' << b << endl;
	}
}