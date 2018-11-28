#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

typedef long long int ll;

string itoll(ll a)
{
    string ss="";   //create empty string
    while(a)
    {
        int x=a%10;
        a/=10;
        char i='0';
        i=i+x;
        ss=i+ss;      //append new character at the front of the string!
    }
        if (ss=="")
        {
                ss="0";
        }
    return ss;
}

bool is_tidy (ll n)
{
	int prev=n%10;
	n/=10;
	while (n>0)
	{
		int curr=n%10;
		if (curr>prev)
			return false;
		n/=10;
		prev=curr;
	}
	return true;
}

ll make_tidy (ll n)
{
	ll orig=n;
	string s=itoll(n);
	int index=s.length()-1;
	ll tidy_cand=orig;
	while (index>=0)
	{
		if (s[index]=='0')
			s[index]='9';
		else
			s[index]--;
		ll tidy_cand=atoll(s.c_str());
		if ((tidy_cand<orig)&&(is_tidy(tidy_cand)))
			return tidy_cand;
		else
			s[index]='9';
		index--;
	}
	return tidy_cand;
}

int main() {
	int t;
	cin >> t;
	for (int i=0; i<t; i++)
	{
		ll n;
		cin >> n;
		if (is_tidy(n))
			printf ("Case #%d: %lld\n", i+1, n);
		else
			printf ("Case #%d: %lld\n", i+1, make_tidy(n));
	}
}
