/*
Google Code Jam 2017
Qualification Round
A: Oversided Pancake Flipper
*/

#include <algorithm>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>

using namespace std;

vector<int> answers;
int num;

bool isHappy(string s)
{
	for (char c : s)
		if (c == '-')
			return false;

	return true;
}

string flip(string s, int index, int flipLength)
{
	for (int i = index; i < index + flipLength; i++)
	{
		if (s[i] == '+')
			s.replace(i, 1, "-");
		else
			s.replace(i, 1, "+");
	}

	return s;
}

void solve(string s, int flipLength, int& minCounter, int counter, map<string, int>& alreadyTested)
{
	if (isHappy(s))
	{
		if (counter < answers[num])
			answers[num] = counter;
		return;
	}
	
	if (counter > s.length())
		return;
	if (counter >= minCounter)
		return;
	if (alreadyTested.find(s) != alreadyTested.end())
	{
		if (alreadyTested[s] <= counter)
			return;
		else
			alreadyTested[s] = counter;
	}

	for (int i = 0; i <= s.length() - flipLength; i++)
	{
		if (isHappy(s.substr(i, i + flipLength)))
			continue;
		string temp = flip(s, i, flipLength);
		// cout << temp << minCounter << endl;
		solve(temp, flipLength, minCounter, counter + 1, alreadyTested);
		alreadyTested.insert_or_assign(temp, counter);
	}

	
}

int solve(string s, int flipLength)
{
	if (isHappy(s))
		return 0;

	map<string, int> stringSet;
	int min = 99999;
	solve(s, flipLength, min, 0, stringSet);

	min = answers[num];

	if (min == 99999)
		return -1;
	else
		return min;
}

int main()
{
	//ifstream fin("input.in");
	ifstream fin("A-small-attempt2.in");
	ofstream fout("output.out");
	
	int T;
	fin >> T;
	for (int i = 0; i < T; i++)
	{
		string S;
		int K;
		fin >> S >> K;
		
		answers.push_back(99999);
		num = i;

		int n = solve(S, K);
		string s;
		if (n == -1)
			s = "IMPOSSIBLE";
		else
			s = to_string(n);

		cout << "Case #" << i + 1 << ": " << s << endl;
		fout << "Case #" << i + 1 << ": " << s << endl;
	}

	return 0;
}