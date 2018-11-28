/*
	ID: reagankan
   Lang: c++11
	Google Code Jam 2017
   Qualification Round 
   Problem B. Tidy Numbers
*/
#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <unordered_set>

using namespace std;

int NumCases;
unsigned long long N = 0ull;
pair<bool, int> decrs(string &s)
{
	for(int i = 0; i < s.size()-1; i++)
	{
		int one = s[i]-48, two = s[i+1]-48; ////cout << one << " " << two << endl;
		//char c1 = s[i]-1, c2 = s[i+1]-1; //cout << c1 << " " << c2 << endl;
		if(one > two)
		{
			return make_pair(true, i);
		}
	}
	return make_pair(false, -1);
}
string add9(string s, int idx)
{
	string ret = s.substr(0, idx+1);
	
	int suffixSize = s.size()-1-idx;
	string suffix(suffixSize,'9');
	ret.append(suffix);
	
	return ret;
}
string remove0(string s)
{
	while(s[0] == '0')
	{
		s = s.substr(1,s.size());
	}
	return s;
}
void tidy_numbers(ifstream &fin, ofstream &fout, int caseNum)
{
	fin >> N; string number = to_string(N);
	//return single digit values immmediately
	//cout << "Input #" << caseNum << " " << N << endl;

	//as long as there is a decrs in sequence we reduce by 1 and add on 999999
	while(decrs(number).first)
	{
		//reduce by 1...
		int idx = decrs(number).second; ////cout << number[idx] << " ";
		number[idx] -= 1; 
		
		//...and add on 999999
		number = add9(number, idx);
		
		//remove preceding 0's
		number = remove0(number);	
	}
	//cout << number << endl;	
	//cout << "Case #" << caseNum << ": " << number << endl;
	fout << "Case #" << caseNum << ": " << number << endl;
}
int main() {
	ifstream sampleIn("sample.in");
	ofstream sampleOut("sample.out");
	ifstream smallIn("B-small-attempt0.in");
	ofstream smallOut("small.out");
	ifstream largeIn("B-large.in");
	ofstream largeOut("large.out");
	
	largeIn >> NumCases;
	int i = 0;
	while(i < NumCases)
	{
		////cout << "testcase: " << i+1 << endl;
		tidy_numbers(largeIn, largeOut, i+1);
		i++;
	}
  return 0;
}