#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>
#include <cstdio>
#include <sstream>
using namespace std;
bool is_non_decreasing(unsigned long long int num)
{
	int least = 0;
	stringstream ss;
	ss << num;
	string s = ss.str();
	for(int i=0;i<s.length();i++)
	{
		if(s[i] >= least)
		{
			least = s[i];
			continue;
		}
		else
			return false;
	}
	return true;
}
int main() {
  int t;
  //string N;
  unsigned long long  N;
  unsigned long long  max;
  freopen("B-small-attempt0.in", "r", stdin);    // redirects standard input
  freopen("B-small-attempt0.out", "w", stdout);    // redirects standard input
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= t; ++i) {
  	cin >> N;
  	max = 0;
    for(unsigned long long j = 1;j<=N;j++)
    {
    	if(is_non_decreasing(j))
    		max = j;
	}
	cout<<"Case #"<<i<<": "<<max<<endl;
  }
  return 0;
}

