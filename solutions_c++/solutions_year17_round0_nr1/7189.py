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

void flip(string &s, int i, int k)
{
	for(;k > 0; i++,k--)
	{
		if(s[i] == '+')
			s[i]='-';
		else
			s[i]='+';
	}
}

int flip_pancakes(string s, int k)
{
	int i,j;
	int ctr = 0;
	for(i = 0; i <= s.size() - k;i++)
	{
		if(s[i] == '-')
		{
			flip(s, i, k);
			ctr++;
		}
	}
	int flag = 1;
	for(;i < s.size();i++)
	{
		if(s[i] == '-')
		{
			flag = -1;
			break;
		}
	}
	if(flag == -1)
	{
		return -1;
	}
	return ctr;
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
    string s;
    int n, ans;
    while(t--)
    {
      	cin>>s>>n;
      	ans = flip_pancakes(s, n);
      	cout<<"Case #"<<i++<<": "<<((ans==-1)?"IMPOSSIBLE":to_string(ans))<<endl;
    }
    return 0;
}

