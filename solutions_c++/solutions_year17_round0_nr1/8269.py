#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
using namespace std;  // since cin and cout are both in namespace std, this saves some text

std::ifstream infile("A-large.in");
std::ofstream outfile("A-large.out");

//std::ifstream infile("input.txt");
//std::ofstream outfile("output.txt");

bool string_has_all_of_the_same_chars(const std::string& s) {
    return s.find_first_not_of(s[0]) == std::string::npos;
}

int flip_pancakes(std::string s, int start, int end, int k, bool& valid)
{
	if(end - start + 1 == k)
	{
		valid = string_has_all_of_the_same_chars(s.substr(start, end+1));

		if(valid)
		{
			if(s.at(start)=='+') return 0;
			else return 1;
		}
		else return -1;
	}
	else
	{
		if(s[start]=='-')
		{
			replace( s.begin() + start, s.begin() + start + k, '+', '~' );
			replace( s.begin() + start, s.begin() + start + k, '-', '+' );
			replace( s.begin() + start, s.begin() + start + k, '~', '-' );

			return (1 + flip_pancakes(s, start + 1, end, k, valid));
		}
		else return flip_pancakes(s, start + 1, end, k, valid);
	}
}


int main() {
  int t, k, no_flips;
  unsigned int pos;
  std::string line, s;
  bool valid;


  infile>>t;// read t. cin knows that t is an int, so it reads it as such.
  std::getline (infile, line);

  for (int i = 1; i <= t; ++i) {

  	std::getline (infile, line);
  	pos = line.find(' ');
  	s = line.substr( 0, pos );
  	k =  std::stoi(line.substr( pos+1, line.size() ));

  	no_flips = flip_pancakes(s, 0, s.size()-1, k, valid);

  	if(valid)
  		outfile<<"Case #" << i << ": " << no_flips << endl;
  	else
  		outfile<<"Case #" << i << ": " << "IMPOSSIBLE" << endl;
   
  }

  return 0;
}