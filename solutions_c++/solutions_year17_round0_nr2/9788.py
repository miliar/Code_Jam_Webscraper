#include<iostream>
#include<conio.h>
#include<string>
#include<sstream>
#include<cstring>
#include<algorithm>
#include<vector>
using namespace std;
string conv_tidy(string ks)
{
	bool cnt = false;
	int ct = 0;
	int len = ks.length();
	for (int p = 0; p < len; p++)
	{
		if (ks[p] <= ks[p + 1] && cnt==false)
		{
			ks[p] = ks[p];
		}
		else
		{
			if (ct == 0)
				ks[p] = ks[p] - 1;
			else
				ks[p] = '9';
			cnt = true;
			ct++;
		}
	}
	return ks;
}
bool check_tidy(string n1)
{
	bool tm = true;
	int len1 = n1.length();
	for(int r=0;r<len1-1;r++)
	{
		if (n1[r] > n1[r + 1])
		{
			tm = false;
		}
	}
	return tm;
}
long long check(long long k)
{
	int temp = 0, i = 0;
	long long n = 0;
	int count = 0, temp1 = 0, temp2 = 0;
	bool res = true;
	ostringstream convertint;   // stream used for the conversion

	convertint << k;      // insert the textual representation of 'Number' in the characters in the stream

	string s = convertint.str();
	string ns = s;
	bool midcheck = false;
	bool checkmidls = false;
	bool cnt = false;
	int ct = 0;
	int len = s.length();
	bool sum = true;
	for(int l=0;l<len;l++)
	{
		if ((s[l] == s[l + 1]))
		{
			continue;
		}
		else
		{
			sum = false;
			break;
		}
	}
	if (sum == true)
	{
		return k;
	}
	else if (len == 1)
	{
		return k;
	}
	else
	{
		bool checkl = false;
		for (int i = 0; i < len; i++)
		{
			if (i == len - 1 && s[len-1]==s[len-2] && checkl==false)
			{
				ns[i] = s[i];
				break;
			}
			else if(i == len - 1 && checkl==false)
			{
				ns[i] = s[i];
				break;
			}
			if (s[i] <= s[i + 1] && cnt == false)
			{
				ns[i] = s[i];
			}
			else
			{
				checkl = true;
				if (ct == 0)
					ns[i] = ns[i] - 1;
				else
					ns[i] = '9';
				cnt = true;
				ct++;
			}

		}
		if (check_tidy(ns) == true)
		{
			istringstream convert_string(ns);
			convert_string >> n;
		}
		else
		{
			ns=conv_tidy(ns);
			if (check_tidy(ns) == false)
			{
				ns = conv_tidy(ns);
			}
			istringstream convert_string(ns);
			convert_string >> n;
			
		}
		return n;
	}
	
}
void main()
{

	freopen("B-small-attempt4.in", "r", stdin);
	freopen("output_file_name.out", "w", stdout);
	long long n = 0;int t = 0;
	cin >> t;
	int ct = 1;
	while(ct<=t)
	{	
		cin >> n;
		cout << "Case #" << ct<< ": " << check(n)<<endl;
			ct++;
	}
}