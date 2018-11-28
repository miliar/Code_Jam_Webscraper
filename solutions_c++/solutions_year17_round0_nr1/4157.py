#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <vector>
#define FOR(it, loop) for(auto (it) = (loop).begin();(it) != (loop).end();(it)++)
#define FORP(it, loop) for(auto (it) = (loop)->begin();(it) != (loop)->end();it++)
using namespace std;
int getNumFromText(string text){
	int result = 0;
	for(auto it = text.begin() ; it != text.end() ; it++){
		if(*it > '9' || *it < '0') throw;
		result *= 10;
		result += *it - '0';
	}
	return result;
}
string getStrFromNum(int num){
	string result = "";
	if(num == 0) return "0";
	while(num > 0){
		result = (char)((num % 10) + '0') + result;
		num /= 10;
	}
	return result;
}
void split(string text, char delimiter, vector<string>* container){
	string part = "";
	for(auto it = text.begin();it != text.end();it++){
		if(*it == delimiter){
			container->push_back(part);
			part = "";
			continue;
		}
		part += *it;
	}

	container -> push_back(part);
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

bool is_finished(string input)
{
	for(auto it = input.begin();it != input.end();it++)
	{
		if(*it == '-') return false;
	}
	return true;
}

void change(string* input, int pos, int flip_num)
{
	for(int i = 0;i < flip_num;i++)
	{
		(*input)[pos+i] = (*input)[pos+i] == '-'? '+':'-';
	}
}

string process(vector<string>* input)
{

	vector<string> container = vector<string>();
	split((*input)[0], ' ', &container);
	int num = getNumFromText(container[1]);

	cout << container[0] << ", " << num << endl;
	int pos = 0;
	int count = 0;
	while(!is_finished(container[0]) && pos + num <= container[0].length())
	{
		if(container[0][pos] == '-')
		{
			change(&container[0], pos, num);
			count++;
		}
		cout << container[0] << endl;
		pos++;
	}
	cout <<"end " << endl;
	return is_finished(container[0]) ? getStrFromNum(count): "IMPOSSIBLE";

}
int main(int args, char** argv)
{
	mainRoutine("A-large.in", 1, process);
	return 0;
}