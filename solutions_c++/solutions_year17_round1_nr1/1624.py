#include <iostream>
#include <vector>
#include <string>

using namespace std;

bool isPainted(const string &s)
{
  for(auto ch : s)
  {
	if(ch == '?')
	{
	  return false;
	}
  }
  return true;
}

bool isAllPainted(const vector<string> &ss)
{
  for(auto s : ss)
  {
	if(!isPainted(s)) return false;
  }
  return true;
}

bool hasInitial(const string &s)
{
  for(auto ch : s)
  {
	if(ch != '?') return true;
  }
  return false;
}

char getInit(const string &s)
{
  for(auto ch : s)
  {
	if(ch != '?') return ch;
  }
  return '?';
}

int main()
{
  int T;
  cin >> T;
  for(int t = 1; t <= T; t++)
  {
	int r, c;
	cin >> r >> c;
	vector<string> ss(r);
	for(int i = 0; i < r; i++)
	{
	  cin >> ss[i];
	}
	while(!isAllPainted(ss))
	{
	  if(r == 1)
	  {
		char prev = getInit(ss[0]);
		for(char &ch : ss[0])
		{
		  if(ch == '?')
		  {
			ch = prev;
		  }
		  else
		  {
			prev = ch;
		  }
		}
	  }
	  
	  for(int i = 1; i < r; i++)
	  {
		if(hasInitial(ss[i]))
		{
		  char prev = getInit(ss[i]);
		  for(char &ch : ss[i])
		  {
			if(ch == '?')
			{
			  ch = prev;
			}
			else
			{
			  prev = ch;
			}
		  }
		}
		else if(isPainted(ss[i - 1]))
		{
		  ss[i] = ss[i - 1];
		}
	  }
	  for(int i = r - 2; i >= 0; i--)
	  {
		if(hasInitial(ss[i]))
		{
		  char prev = getInit(ss[i]);
		  for(char &ch : ss[i])
		  {
			if(ch == '?')
			{
			  ch = prev;
			}
			else
			{
			  prev = ch;
			}
		  }
		}
		else if(isPainted(ss[i + 1]))
		{
		  ss[i] = ss[i + 1];
		}
	  }
	}
	cout << "Case #" << t << ":" << endl; 
	for(auto s : ss)
	{
	  cout << s << endl;
	}
  }
}
