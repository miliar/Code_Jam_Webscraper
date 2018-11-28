#include <iostream>
#include <vector>

using namespace std;


int main()
{
	int t;
	cin>>t;
	for (int i = 0; i < t; ++i)
	{
		long long int n;
		cout<<"Case #"<<i+1<<": ";
		cin>>n;

		vector<int> digits;
		int temp = n;
		while(temp){
			digits.push_back(temp%10);
			temp /= 10;
		}
		int save_it=digits.size()-1,end_it = 0;
		for (int i = digits.size()-1; i >= 1; --i)
		{
			if(digits[i-1] < digits[i]){
				end_it = i;
				break;
			}
			if(digits[i-1]!=digits[save_it]){
				save_it = i-1;
			}
		}

		// cout<<save_it<<endl;

		if(end_it!=0){ 
			digits[save_it] -= 1;
			for (int i = save_it - 1; i >= 0; --i)
			{
				digits[i] = 9;
			}
		}
		int result = 0;
		temp = digits.size();
		for (int i = temp - 1; i >= 0; --i)
		{
			result *= 10;
			result += digits[i];
		}
		cout<<result<<endl;
	}
}