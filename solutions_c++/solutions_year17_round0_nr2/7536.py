# define _CRT_SECURE_NO_WARNINGS 
#include <iostream> 
#include <algorithm> 
#include <cstring> 
#include <cmath> 
#include <stdio.h> 
#include <vector> 
#include <cstdlib> 
#include <string> 
#include <map> 
#include <ctime> 
#include <list> 
#include <stack> 
#include <set> 
#include <memory.h> 
#include <deque> 
#include <queue> 
#include <cctype> 
#include <iomanip> 
#include <bitset> 
#include <sstream> 
#include <unordered_map> 
#include <fstream>

# define pi acos(-1.) 
# define e exp(1.) 

using namespace std;
using ld = long double;
using ll = long long;

const double EPS = 1e-6;
const int N = 100010;

int n, k;
bool Check(string& s)
{
	for (int i = 0; i < s.size(); ++i)
	{
		if (s[i] == '-')
		{
			return false;
		}
	}
	return true;
}

int GetMinuses(string& s)
{
	int ans = 0;
	for (int i = 0; i < s.size(); ++i)
	{
		ans += (s[i] == '-');
	}
	return ans;
}

void AddIntervals(vector<int>& v, string& s)
{
	for (int i = 0; i < n - k + 1; ++i)
	{
		if (Check(s.substr(i, k)) && !binary_search(v.begin(), v.end(), i))
		{
			v.emplace_back(i);
		}
	}
}

bool checkInterval(int ind, vector<int>& v)
{
	for (int i = 0; i < k;++i)
	{
		for (int j = 0; j < v.size(); ++j)
		{
			if (ind + i >= v[j] && ind + i < v[j] + k)
			{
				return false;
			}
		}
	}
	return true;
}

void f(int n)
{

	for (int i = n;; --i)
	{

		string s = to_string(i);
		bool ok = true;
		for (int j = 0; j < s.size() - 1; ++j)
		{
			if (s[j]>s[j + 1])
			{
				ok = false;
				break;
			}
		}
		if (ok)
		{
			cout << i << endl;
			break;
		}
	}
}


int main()
{
	////ios::sync_with_stdio(false);
	//fstream out("C:\\Users\\volok\\Desktop\\out.txt");
	//int t;
	//scanf("%d", &t);
	//for (int i = 1; i <= t;++i)
	//{
	//	vector<int>intervals;
	//	string ans = "Case #" + to_string(i) + ": ";
	//	string s;
	//	cin >> s;
	//	scanf("%d", &k);
	//	int minn = INT_MAX;
	//	n = s.size();
	//	if (Check(s))
	//	{
	//		minn = 0;
	//	}

	//	else
	//	{
	//		for (int j = 0; j < n - k + 1; ++j)
	//		{
	//			AddIntervals(intervals, s);
	//			sort(intervals.begin(), intervals.end());
	//			int current = 0;
	//			int ind = 0;
	//			for (int l = 0; l < n - k + 1; ++l)
	//			{
	//				if (GetMinuses(s.substr(l, k))>current&&checkInterval(l, intervals))
	//				{
	//					current = GetMinuses(s.substr(l, k));
	//					ind = l;
	//				}
	//			}

	//			for (int l = 0; l < k; ++l)
	//			{
	//				if (s[ind + l] == '-')
	//				{
	//					s[ind + l] = '+';
	//				}
	//				else
	//				{
	//					s[ind + l] = '-';
	//				}
	//			}
	//			if (Check(s))
	//			{
	//				minn = j + 1;
	//				break;
	//			}
	//		}
	//	}
	//	ans += (minn == INT_MAX ? "IMPOSSIBLE" : (to_string(minn)));
	//	out << ans << endl;
	//}

	fstream out("C:\\Users\\volok\\Desktop\\out.txt");
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i)
	{
		string ans = "Case #" + to_string(i) + ": ";
		string s;
		cin >> s;
		//f(stoi(s, nullptr, 10));
		int in = 0;
		for (int j = 1; j < s.size(); ++j)
		{
			if (s[j]<s[j - 1])
			{
				in = j;
				break;
			}
		}

		if (in)
		{
			for (int j = in; j < s.size(); ++j)
			{
				s[j] = '9';
			}

			--in;
			while (in>0 && s[in] == s[in - 1])
			{
				--in;
			}
			--s[in];

			if (s.front() == '0')
			{
				swap(s.front(), s.back());
				s.pop_back();
			}
			for (int j = in + 1; j < s.size(); ++j)
			{
				s[j] = '9';
			}
		}
		ans += s;
		out << ans << endl;
	}

}