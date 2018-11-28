#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <vector>
#define FOR(it, loop) for(auto (it) = (loop).begin();(it) != (loop).end();(it)++)
#define FORP(it, loop) for(auto (it) = (loop)->begin();(it) != (loop)->end();it++)
using namespace std;
long long getNumFromText(string text){
	long long result = 0;
	for(auto it = text.begin() ; it != text.end() ; it++){
		if(*it > '9' || *it < '0') throw;
		result *= 10;
		result += *it - '0';
	}
	return result;
}
string getStrFromNum(long long num){
	if(num==0) return "0";
	string result = "";
	while(num > 0){
		result = (char)((num % 10) + '0') + result;
		num /= 10;
	}
	return result;
}
void mainRoutine(string filepath, int unitLine, string (*func)(vector<string> *)){
	ifstream in;
	ofstream out;
	in.open(filepath);
	out.open("result");
	if(in.is_open()){
		string line;
		getline(in, line);
		int testCount = 1;
		vector<string> strData;
		while(getline(in, line)){
			strData.push_back(line);
			if(strData.size() == unitLine){
				out << "Case #" << testCount++ << ": " << (*func)(&strData) << '\n';
				strData.clear();
			}
		}
		in.close();
		out.close();
	}
}
bool is_tidy(string num)
{
	for(int i = 0;i < num.length() - 1;i++)
	{
		if(num[i] > num[i+1]) return false;
	}
	return true;
}
string get_next_small(string num)
{
	bool found = false;
	for(int i = num.length() - 1;i >= 0;i--)
	{
		if(num[i] != '9') found = true;
		if(found)
		{
			num[i] = '9';
			bool change_complete = false;
			while(i-->0)
			{
				if(num[i] > '0') 
				{
					num[i]--;
					return num;
				}
				num[i] = '9';
			}
		}
	}
}
string process(vector<string>* input)
{
	string num = (*input)[0];
	while(!is_tidy(num))
	{
		num = get_next_small(num);
	}
	return getStrFromNum(getNumFromText(num));
}

int main(int argc, char** argv)
{
	// cout << get_next_small("1000") << endl;
	// cout << get_next_small("11111111111111110") << endl;
	// cout << is_tidy("123456678990") << endl;
	mainRoutine("B-large.in", 1, process);
	return 0;
}