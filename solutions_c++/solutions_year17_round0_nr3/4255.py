#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <vector>
#define FOR(it, loop) for(auto (it) = (loop).begin();(it) != (loop).end();(it)++)
#define FORP(it, loop) for(auto (it) = (loop)->begin();(it) != (loop)->end();it++)
using namespace std;
struct level
{
	long long max;
	long long min;
	long long max_count;
	long long min_count; 
};
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
void splitToNum(string text, char delimiter, vector<long long>* container){
	vector<string> temp;
	split(text, delimiter, &temp);
	FOR(it, temp){
		container->push_back(getNumFromText(*it));
	}
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
int get_level(long long num)
{
	int result = 0;
	while(num > 0)
	{
		result++;
		num = num >> 1;
 	}
 	return result - 1;
}
vector<long long> lol(long long num, int level)
{
	long long max_count = 1;
	long long min_count = 0;
	while(level-- > 0)
	{
		max_count = num % 2 == 0 ? max_count : min_count + max_count * 2;
		min_count = num % 2 == 0 ? min_count * 2 + max_count : min_count;
		num /= 2;
	}
	vector<long long> result = vector<long long>();
	result.push_back(num);
	result.push_back(max_count);
	return result;
}
string process(vector<string>* input)
{
	vector<long long> data = vector<long long>();
	splitToNum((*input)[0], ' ', &data);
	long long n = data[0];
	int level = get_level(data[1]);
	vector<long long> a = lol(n, level);
	long long remaining = data[1] - (1 << level) + 1;
	long long _max, _min;
	cout << a[0] << ", " << a[1] << endl;
	if(remaining <= a[1])
	{
		cout <<"mini" << endl;
		_max = a[0] / 2;
		_min = (a[0] - 1) / 2;
	}
	else
	{
		cout << "many" << endl;
		_max = (a[0] - 1) / 2;
		_min = (a[0] - 2) / 2;
	}
	cout << _max << " v " << _min << endl;
	return getStrFromNum(_max)+" "+getStrFromNum(_min);

}
int main()
{

	mainRoutine("C-small-2-attempt0.in", 1, process);
	return 0;
}