#include<iostream>
#include<bits/stdc++.h>
using namespace std;

int main()
{
	freopen("C:\\Users\\Abhishek\\Desktop\\Google Code Jam\\2017 Qualification Round\\B-small-attempt0.in", "r", stdin);
	freopen("C:\\Users\\Abhishek\\Desktop\\Google Code Jam\\2017 Qualification Round\\B-output_small.txt", "w", stdout);
	int t;
	cin >> t;
	for(int test = 1; test <= t; test++)
	{
		long long int n, k, ans;
		cin >> k;
		stack <int> s;
		n = k;
		
		while(n > 0)
		{
			s.push(n % 10);
			n /= 10;
		}
		
		vector <int> v;
		
		while(!s.empty())
		{
			v.push_back(s.top());
			s.pop();
		}
		
		int pos = -1, f = 0;
		
		for(int i = 0; i < v.size() - 1; i++)	
		{
			if(v[i] == v[i + 1])
			{
				if(pos == -1)
					pos = i;
			}
			else if(v[i] > v[i + 1])
			{
				if(pos == -1)
					pos = i;
				f = 1;
				break;
			}
		}
		
		if(f == 0)
			ans = k;
		
		else
		{
			v[pos] = v[pos] - 1;
			for(int i = pos + 1; i < v.size(); i++)
				v[i] = 9;
			
			ans = 0;
			for(int i = 0; i < v.size(); i++)
				ans = ans * 10 + v[i]; 
		}
		
		cout << "Case #" << test << ": " << ans << endl;	
	}
}
