//#include <bits/stdc++.h>
 #include <iostream>
 #include <string>
using namespace std;

long long coordinate(long long number, long long index)
{

	if(index == 1)
		return number;
	else
	{
		long long min, max;
		number = number - 1;
		if(number%2 == 0)
		{
			min = number/2;
			max = number/2;
		} 
		else
		{
			min = number/2;
			max = number/2 + 1;
		}
		if(index%2 == 0)
		{
			return coordinate(max,index/2);
		}
		else
			return coordinate(min,index/2);
	}
}


int main(){
	long long t;
	cin>>t;
	int case_no=1;
	while(t--){
		
		long long n,k;
		long long min, max;
		cin>>n>>k;
		
		long long number = coordinate(n,k);

		number = number - 1;

		if(number%2 == 0)
		{
			min = number/2;
			max = number/2;
		} 
		else
		{
			min = number/2;
			max = number/2 + 1;
		}

		cout<<"Case #"<<case_no<<": "<<max<<" "<<min<<endl;
		case_no++;
	}
	return 0;
}

