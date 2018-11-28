#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <vector>
#include <iomanip>
#define FOR(it, loop) for(auto (it) = (loop).begin();(it) != (loop).end();(it)++)
#define FORP(it, loop) for(auto (it) = (loop)->begin();(it) != (loop)->end();it++)
using namespace std;
static int testCount = 1;
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
	if(num == 0) return "0";
	string result = "";
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
void mainRoutineWithVariableCaseNum(string filepath, int (*lineFunction) (long long), void (*func)(vector<string> *)){
	ifstream in;
	ofstream out;
	in.open(filepath);
	out.open("result");
	if(in.is_open()){
		string line;
		getline(in, line); //test case size
		
		vector<string> strData = vector<string>();
		int lineCount;
		bool lineCountSet = false;
		while(getline(in, line)){
			if(!lineCountSet) {
				vector<long long> linev = vector<long long>();
				splitToNum(line, ' ', &linev);
				lineCount = (*lineFunction)(linev[1]); //number to read consequently
				lineCountSet = true;
				strData.push_back(line);
				continue;
			}
			else{
				if(lineCount > 0){
					strData.push_back(line);
					lineCount--;
				}
			}
			if(lineCount == 0)
			{
				(*func)(&strData);
				strData.clear();
				lineCountSet = false;
			}
		}
		in.close();
		out.close();
	}
}
int line(long long input)
{
	//cout << input << endl;
	return input;
}
double getTime(long long dest, long long start, long long speed)
{
	//cout << dest << ", "<<start << ", "<<speed<<endl;
	return (double)(dest - start)/speed;
}

void process(vector<string>* input)
{
	//cout<< input->size()<<endl;
	vector<long long> data = vector<long long>();
	splitToNum((*input)[0], ' ', &data);
	long long dest = data[0];
	double maxTime = 0;
	for(int i = 1; i<input->size();i++)
	{
		data.clear();
		splitToNum((*input)[i], ' ', &data);
		double time = getTime(dest, data[0], data[1]);
		if(maxTime < time) maxTime = time;
	}
	printf("Case #%d: %7f\n", testCount++, ((double)dest / maxTime));
	//cout << "Case #" << testCount++ << ": " << setprecision(7) << ((double)dest / maxTime) << '\n';
}
int main(void)
{
	mainRoutineWithVariableCaseNum("A-large.in", line, process);
	return 0;
}