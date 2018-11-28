// tidy.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <string>
#include <fstream>


bool IsTidyNumber(const std::string& input, int& pos)
{
	char prev = input[0];
	auto len = input.length();
	for (size_t i = 1; i < len; ++i) {
		char ch = input[i];
		if (ch < prev) {
			pos = i;
			return false;
		}

		prev = ch;
	}

	return true;
}

size_t GetNumZeroLead(const std::string& input)
{
	auto len = input.length();
	size_t at = 0;
	while (at < len) {
		if (input[at] != '0')
			break;
		at += 1;
	}

	return at;
}

std::string DecreaseNumber(const std::string& input, int pos)
{
	auto len = input.length();
	auto output = input;
	for (size_t i = pos; i < len; ++i) {
		output[i] = '9';
	}

	int at = pos - 1;
	while (at >= 0) {
		char ch = output[at];
		if (ch == '0') {
			output[at] = '9';
			at -= 1;
		}
		else {
			output[at] = ch - 1;
			break;
		}
	}

	auto numZero = GetNumZeroLead(output);
	if (numZero == 0)
		return output;

	return output.substr(numZero);
}

std::string FindTidyNumber(const std::string& input)
{
	int pos;
	if (IsTidyNumber(input, pos)) {
		return input;
	}

	auto newInput = DecreaseNumber(input, pos);
	return FindTidyNumber(newInput);
}

//////////////////////////////////////////////////////////////////////////
int main()
{
	std::ifstream in("input/B-large.in");
	std::ofstream out("input/B-large.out");

	int numCase;
	in >> numCase;
	for (int i = 1; i <= numCase; ++i) {
		std::string input;
		in >> input;
		
		auto output = FindTidyNumber(input);
		out << "Case #" << i << ": " << output.c_str() << std::endl;
	}
	/*
	std::string input = "135032";
	auto tidy = FindTidyNumber(input);
	int k = 0;
	//*/

}

