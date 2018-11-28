#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

string tidy(string N)
{
	int len = N.size();
	string n;
	vector<int> digits;
	// convert N to digits
	for(int j=len-1;j>=0;j--)
		digits.push_back(N[j]-'0');

	vector<int> tidy_num(len,0);
	// start from the significant digit
	int i = len-1;
	while(i>=0)
	{
		int j;
		for(j=i-1;j>=0;j--)
			if(digits[j]!=digits[i])
				break;
		if(j<0 || digits[j]>digits[i])
		{
			for(int k=i;k>j;k--)
				tidy_num[k] = digits[i];
			i = j;
		}
		else
		{
			tidy_num[i] = digits[i]-1;
			for(int k=i-1;k>=0;k--)
				tidy_num[k] = 9;
			break;
		}
	}
	for(i=len-1;i>=0;i--)
		if(tidy_num[i]!=0)
			break;
	for(int j=i;j>=0;j--)
		n.push_back('0'+tidy_num[j]);
	return n;
}

int main()
{
	int t;
	string N;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		cin>>N;
		string n = tidy(N);
		cout<<"Case #"+to_string(i+1) + ": " + n<<endl;
	}
	return 0;
}

