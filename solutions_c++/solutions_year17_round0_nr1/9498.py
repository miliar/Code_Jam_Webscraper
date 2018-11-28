#include <iostream>
#include <sstream>

using namespace std;

//problem flip all '+' to '-' with minimum flips

void print_s(string s);
void print_unfinished_s(string s, int start_i);

void flip(char& ch) {

	if(ch == '+') ch = '-';
	else ch ='+';
}

int update_s_limits(string s, int& start_i) {

	for(int i = start_i;i<s.length();i++) {
		if (s[i] == '+')
			start_i ++;
		else
			return 1;
	}
	
	return 0;
}

bool flip_next_k(string& s, int k, int start_i) {

	for(int i=start_i; i<start_i+k;i++) {

		if (i == s.length()) 
			return false;		

		flip(s[i]);
	}
	
	return true;
}


string Oversized_Pancake_Flipper(string s, int k) {

	int flip_counter = 0;
	int start_i = 0;

	for(;update_s_limits(s, start_i);) {

		//print_s(s);
		//print_unfinished_s(s, start_i);	

		if(!flip_next_k(s, k, start_i))
			return "IMPOSSIBLE";

		flip_counter++;
	}

	ostringstream intToString;
	intToString << flip_counter;

	return intToString.str();
}

int main() {
  int t;
  cin >> t;  
  for (int i = 1; i <= t; ++i) {
	
	string s;
	int k;
    	cin >> s >> k;
    	cout << "Case #" << i << ": " << Oversized_Pancake_Flipper(s, k) << endl;
  }
  
  return 0;
}

void print_s(string s) {

	for(int i=0;i<s.length();i++)
		cout<<s[i];
	cout<<endl;
}

void print_unfinished_s(string s, int start_i) {

	for(int i=start_i;i<s.length();i++)
		cout<<s[i];
	cout<<endl;
}




