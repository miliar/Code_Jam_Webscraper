#include<iostream>
#include<fstream>
#include<string>
#include<sstream>

using namespace std;

bool tidy(long long number) {
	
	stringstream ss;
	ss << number;
	string str = ss.str();
	for (long long i = str.length()-1; i > 0; i--) {
		if (str.length() == 1)return true;
		if (str[i] >= str[i - 1] && str[i] != 0);
		else return false;
	}
	return true;
}
string tidy2(long long number) {
	stringstream ss;
	ss << number;
	string str = ss.str();
	for (int i = 0; i < str.length()-1; i++) {
		if (str[i] <= str[i + 1]);
		else {
			int j = 0;
			for (int j = i + 1; j < str.length()  ; ++j) {
				str[j] = '0';
				//cout << j;
			}
			number = stoll(str);
			number -= 1;
			
			ss.str("");
			ss << number;
			str = ss.str();
			i = i-2;
		}
	}
	//cout << number;
	//cout << str;
	return str;
}

int main() {
	long long x;
	bool check;
	int casee,n;
	string str;
	ifstream infile("C:\\Users\\f12_2_000\\Desktop\\input.txt");
	ofstream myfile;
	myfile.open("C:\\Users\\f12_2_000\\Desktop\\output.txt");
	infile >> casee;
	//cout << casee << endl;
	n = casee;
	//myfile << "hello";
	while (casee--) {
		infile >> x;
		cout << x<<endl;
		
		str = tidy2(x);
		
		myfile <<"Case #"<<n-casee<<": "<< str<<endl;
		cout << "Case #" << n - casee << ": " << str << endl;
				
		myfile.flush();
	}
	
	myfile.close();
	system("pause");
}