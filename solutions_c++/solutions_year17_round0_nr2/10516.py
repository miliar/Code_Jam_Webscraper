#include<bits/stdc++.h>

using namespace std;

int main()
{
	int T;
	string number;
	scanf("%d", &T);
	for(int i = 0; i<T; i++)
	{
		cin>>number;
		long long int temp;
		bool flag = true;
		while(flag)
		{
			if(is_sorted(number.begin(), number.end()))
			{
				flag = false;
				break;
			}
			else
			{
				temp = stoll(number)-1;
				number = to_string(temp);
			}
		}		
		cout<<"Case #"<<(i+1)<<":"<<" "<<number<<endl;
	}
	return 0;
}
