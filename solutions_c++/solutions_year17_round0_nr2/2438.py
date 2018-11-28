#include <iostream>
#include <vector>
#include <string>

using namespace std;

string largesttidynum(string number){
	string tidy_number;
	int length = number.length();
	int pos;

	for(pos = length-1;pos != 0; pos --){
        if(number[pos - 1] > number[pos]){
            number[pos-1] = number[pos-1] - 1;
            number[pos] = '9';
        }
	}

	for(pos = 1;pos != length; pos ++){
        if(number[pos - 1] == '9'){
            number[pos] = '9';
        }
	}

	if(number[0] == '0'){
        if(length == 1)
            tidy_number = number;
        else
            tidy_number = number.substr(1);
	}
    else{
        tidy_number = number;
    }

	return tidy_number;
}

int main()
{
	int num_test_cases;
	string number;
	vector<string> v1;

	string tidy_number;

	cin>>num_test_cases;

	for(int i=1; i <= num_test_cases; i++){
		cin>>number;
		v1.push_back(number);
	}

	for(int i=0; i < num_test_cases; i++){
		number =  v1[i];
		tidy_number = largesttidynum(number);

		cout << "Case #"<<i+1<<": "<<tidy_number<<endl;
	}

	return 0;
}
