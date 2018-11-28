#include <iostream>
#include <algorithm>
#include <string>
#include <sstream>

using namespace std;

void reduce(string &ss, int inx)
{
	if (inx < 0)return;
	if (ss[inx] == '0')
	{
		ss[inx] = '9';
		reduce(ss, inx - 1);
	}
	else {
		int d = ss[inx] - '0';
		d--;
		ss[inx] = d + '0';
		if (inx > 0 && ss[inx] < ss[inx - 1]){
			ss[inx] = '9';
			reduce(ss, inx - 1);
		}
	}
}

void setnine(string& s, int inx)
{
	for (int i = inx ; i < s.size() ; i++)
		s[i] = '9';
}

void solve(string& ss)
{
	for(int i = 0; i < ss.size(); i++) {
		if(i + 1 < ss.size() && ss[i] > ss[i + 1])
		{
			reduce(ss, i);
			setnine(ss, i + 1);
			break;
		}
	}
	
}

int main()
{
	int T;
	long long dd;
	//~ freopen("B-large.in", "r" , stdin);
	//~ freopen("out.txt", "w", stdout);
	cin >> T;
	string digit;
	for (int i = 0; i < T; i++)
	{
		cin >> digit;
		solve(digit);
		stringstream ss;
		ss << digit;
		ss >> dd;
		cout << "Case #" << i + 1<< ":  ";
		cout << dd << endl;
	}
	return 0;
}
