#include<iostream>

using namespace std;

const int size = 20;
int main()
{
	void convert(int [], string );
	void subtract_one(int []);
	void add_one(int []);
	void next_tidy(int [], int []);
	int check(int []);
	int to_int(char);
	int larger(int [], int []);


	int a[size], curr[size], next[size];
	string s;
	int t;
	
	cin>>t;
	
	for(int i = 1; i <= t; ++i)
	{
		cin>>s;
		
		convert(a, s);
		
		for(int j = 0; j < size; j++)
		{
			curr[j] = 0;
			next[j] = 0;
		}
		
		
		while(larger(a, next))
		{
			
			for(int j = 0; j < size; ++j)
			{
				curr[j] = next[j];
			}
			
			next_tidy(curr, next);
			
		}
		/*
		while(check(a) == 0)
		{
			subtract_one(a);
		}
		
		cout<<"Case #"<<i<<": ";
		for(int j = 0; j < size; j++)
		{
			if(a[j] == 0)
			{
				continue;
			}
			
			else
			{
				cout<<a[j];
			}
		}
		cout<<"\n";
		*/
		
		cout<<"Case #"<<i<<": ";

		for(int j = 0; j < size; j++)
			{
				if(curr[j] == 0)
				{
					continue;
				}
				
				else
				{
					cout<<curr[j];
				}
			}
		cout<<"\n";
		
	}
	
}
int to_int(char c)
{
	return c - '0';
}
int larger(int a[], int b[])
{
	int j = 0;
	
	for(; j < size; j++)
	{
		if(a[j] > b[j])
		{
			return 1;
		}
		if(a[j] < b[j])
		{
			return 0;
		}
	}
	
	return 1;
}
void subtract_one(int a[])
{
	int j = size - 1;
	int carry = 1;
	
	for(; j >= 0; j--)
	{
		a[j] -= carry;
		if(a[j] >= 0)
		{
			break;
		}
		else
		{
			a[j] += 10;
		}
	}
}
void add_one(int a[])
{
	int j = size - 1;
	int carry = 1;
	
	for(; j >= 0; j--)
	{
		a[j] += carry;
		
		if(a[j] < 10)
		{
			break;
		}
		else
		{
			a[j] -= 10;
		}
	}
}

void next_tidy(int curr[], int next[])
{
	add_one(curr);
	
	int j = 0;
	for(; j < size - 1; ++j)
	{
		if(curr[j] > curr[j + 1])
		{
			break;
		}
	}
	
	for(int k = 0; k <= j; ++k)
	{
		next[k] = curr[k];
	}
	for(int k = j + 1; k < size; ++k)
	{
		next[k] = next[j];
	}
	
	subtract_one(curr);
	
}
void convert(int a[], string s)
{
	int j = size - 1;
	int k = s.length() - 1;
	
	while(k >= 0)
	{
		a[j--] = to_int(s[k--]);
 
	}
	
	while(j >= 0)
	{
		a[j--] = 0;
	}
}
int check(int a[])
{
	int j = size - 1;
	for(; j > 0; j--)
	{
		if(a[j - 1] > a[j])
		{
			return 0;
		}
	}
	
	return 1;
}

