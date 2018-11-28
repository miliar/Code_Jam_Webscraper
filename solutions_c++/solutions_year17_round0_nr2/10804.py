#include <iostream>
#include <string>
#include <vector>
#include <sstream>
using namespace std;

int a[10];
void reset() 
{
	for(int i = 0; i < 10; ++i) a[i] = -1;
}


// Number to String
template <class T>
inline std::string to_string (const T& t)
{
    std::stringstream ss;
    ss << t;
    return ss.str();
}

bool checkTidy(unsigned long long num) 
{
	unsigned long long min = 0;
	string s = to_string(num); // 123,
	for(int i = 0; i < s.length(); ++i) 
	{
		if(min <= s[i] - '0') 
		{
			min = s[i] - '0';
		}
		else 
			return false;		
	}
	return true;
}


void formTidy(unsigned long long num)
{
	if(checkTidy(num)) {
		cout<< num <<endl;
		return;
	}

	string s = to_string(num);
	int t = 0;
	for(int i = 0; i < s.length() - 1; ++i)
	{
		if(s[i] < s[i+1]) continue;
		else
		{
			t = s[i] - '0' - 1;

			string k = to_string(t);
			char c = '9';
			k += c; // append
			string res;
			
			for(int j = 0; j < s.length(); ++j)		
			{
				if(j<i) 
				  res += s[j];
				else if(j == i)
				{
					res += k;
					j += 1;
				}
				else
			    res += c; // append
			}

			// string to long long
			std::stringstream sstr(res);
			__int64 val;
			sstr >> val;
			cout<< val <<endl; 
			return;
		}
	}
	cout<< num <<endl;
}


int main()
{
	freopen("Input.in", "rt", stdin);
	freopen("Output.out", "wt", stdout);
	int ntc = 0;
	cin >> ntc;
	for(int tc = 0; tc < ntc; ++tc)
	{
		unsigned long long num = 0;
		cin >> num; // 132 -> 129

		// num = 377;
#if 1
		cout<<"Case #"<<tc+1<<": ";
		formTidy(num);	
#else		
		for(unsigned long long n = num; n > 0; --n)
		{
			if(checkTidy(n))
			{
				cout<<"Case #"<<tc+1<<": "<< n << endl;
				break;
			}
		}		
#endif
	}
	return 0;
}