#include <iostream>
#include <string>
using namespace std;

int main()
{
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++){
		string pancakes, strings;
		int s;
		cin >> pancakes >> strings;
		s = stoi(strings);
		bool poss = true;
		int times = 0;
		for (int j = 0; j< pancakes.size(); j++){
			if (j + s == pancakes.size()){
				char last = pancakes[j];
				for (int k = j+1; k < pancakes.size(); k++)
					if (pancakes[k] != last)
						poss = false;
				if (last == '-')
					times++;
				break;
			}
			else if (pancakes[j] == '-'){
				times++;
				for (int k = 0; k < s; k++){
					if (pancakes[k+j] == '+')
						pancakes[k+j] = '-';
					else
						pancakes[k+j] = '+'; 
					
				}
			}
		}
		cout << "Case #" <<  i << ": ";
		if (poss)
			cout << times << endl;
		else
			cout << "IMPOSSIBLE" << endl;
	}
	return 0;
}