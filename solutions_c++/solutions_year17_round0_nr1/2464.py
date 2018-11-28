#include <iostream>
#include <vector>
#include <string>

using namespace std;

int happysideup(string pancakes, int flip_size)
{
	int size = pancakes.length();
	int pos;
	for(pos = 0; pos < size; pos++){
		if(pancakes[pos] == '-')
			break;
	}
	if(pos == size)
		return 0;
	else if(size-pos < flip_size)
		return -1;
	else{
		pancakes[pos] = '+';
		for(int i=1;i<flip_size;i++){
			if(pancakes[pos+i] == '-')
				pancakes[pos+i] = '+';
			else
				pancakes[pos+i] = '-';
		}
		string new_pancakes = pancakes.substr(pos+1);
		int new_flips = happysideup(new_pancakes, flip_size);
		if(new_flips == -1)
			return -1;
		else
			return 1+new_flips;
	}
}

int main()
{
	int num_test_cases,flip_size;
	string pancakes;
	vector<string> v1;
	vector<int> v2;
	int num_steps;

	cin>>num_test_cases;

	for(int i=1; i <= num_test_cases; i++){
		cin>>pancakes>>flip_size;
		v1.push_back(pancakes);
		v2.push_back(flip_size);
	}

	for(int i=0; i < num_test_cases; i++){
		pancakes =  v1[i];
		flip_size = v2[i];
		num_steps = happysideup(pancakes,flip_size);
		if(num_steps == -1){
			cout << "Case #"<<i+1<<": "<<"IMPOSSIBLE"<<endl;
		}
		else{
			cout << "Case #"<<i+1<<": "<<num_steps<<endl;
		}
	}

	return 0;
}
