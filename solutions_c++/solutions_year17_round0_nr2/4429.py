#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <climits>
#include <queue>
#include <utility>
#include <set>
#include <bitset>
#include <stdio.h>

using namespace std;
bool isCorrect(long long n){
	vector<int> revdigits;
	while(n!=0){
		revdigits.push_back(n%10);
		n=n/10;
	}
	for (int i = 0; i < revdigits.size()-1; ++i)
	{
		if(revdigits[i]>=revdigits[i+1])
			continue;
		else
			return false;
	}
	return true;
}

int main(int argc, char const *argv[])
{

	int t;
	cin>>t;
	for (int i = 1; i <= t; ++i)
	{
		long long N;
		cin>>N;
		long long n=N;

		while(!isCorrect(n)){
			// cout<<n<<endl;
			vector<int> revdigits;
			vector<int> digits;
			while(n!=0){
				revdigits.push_back(n%10);
				n=n/10;
			}
			for (int l = 0; l < revdigits.size(); ++l)
			{
				digits.push_back(revdigits[revdigits.size()-1-l]);
			}
			bool isNine=false;
			for (int l = 0; l < digits.size(); ++l)
			{
				if(isNine){
					digits[l]=9;
					continue;
				}
				if(l<digits.size()-1 && digits[l]>digits[l+1])
				{
					digits[l]--;
					isNine=true;
				}
			}
			long long ans=0;
			for (int l = 0; l < digits.size(); ++l)
			{
				ans=10*ans+digits[l];
			}
			n=ans;
		}
		cout<<"Case #"<<i<<": "<<n<<endl;
	}

return 0;
}