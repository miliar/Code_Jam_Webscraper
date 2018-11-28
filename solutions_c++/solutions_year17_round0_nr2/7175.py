#include <iostream>
#include <string>
#include <bits/stdc++.h>

using namespace std;

typedef unsigned long long ll;
typedef pair<int,int> pi;
typedef vector<int> vi;

#define TEST  int test_case; cin>>test_case; while(test_case--)
#define FOR(arr) for(auto &i:arr)
#define fi  first
#define se  second
#define pb push_back
#define EPS (double)(1e-9)
#define MOD 1000000007
#define SPEED ios_base::sync_with_stdio(false);  cin.tie(0);  cout.tie(0);

ll find_tidy(ll n)
{
	string s = to_string(n);
	int i = 0;
	if(s.size() == 1)
	{
		return n;
	}
	for(i = 1; i < s.size(); i++)
	{
		if(s[i - 1] > s[i])
		{
			break;
		}
	}
	if(i == s.size()) //TIDY NUMBER ITSELF
	{
		return n;
	}
	if(s[i-1] != '0' && ( (i-1) == 0 || (s[i-2] <= s[i-1] - 1) ) ) 
	{
		s[i-1] = s[i-1] - 1;	
		for(;i < s.size(); i++)
		{
			s[i] = '9';
		}
	}
	else
	{
		int j = i - 1;
		while(s[j-1] == s[j] && j >=1)
		{
			j--;
		}//we got a character not zero
		s[j]--;
		i = j + 1;
		for(;i < s.size(); i++)
		{
			s[i] = '9';
		}
	}	
	return stoll(s);
}

int main()
{

	#ifndef TESTING
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    #endif
    int t,i;
    cin>>t;
    i = 1;
    while(t--)
    {
      	ll n, ans;
      	cin>>n;
      	ans = find_tidy(n);
      	cout<<"Case #"<<i++<<": "<<ans<<endl;
    }
    return 0;
}

