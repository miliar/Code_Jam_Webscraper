#include<iostream>
#include<vector>
using namespace std;

int main()
{
	int t;
	cin>>t;

	for(int i = 0 ; i < t ; i++)
	{
		long long int n,k;
		cin>>n>>k;
		vector<long long int> vec;
		vector<long long int> vec2;
		long long int index1 = 0;
		long long int index2 = 0;
		vec.push_back(n);
		long long int max = 0;
		long long int min = 0;
		for(long long int j = 0 ; j < k ; j++)
		{
			if(index1 == 0)
			{
				if(vec[index1]%2 == 0)
				{
					max = vec[index1]/2;
					min = vec[index1]/2-1;
					vec.push_back(max);
					vec2.push_back(min);
				}
				else
				{
					max = vec[index1]/2;
					min = max;
					vec.push_back(max);
					vec2.push_back(min);	
				}
				index1++;
			}
			else
			{
				if(vec[index1] >= vec2[index2])
				{
					if(vec[index1]%2 == 0)
					{
						max = vec[index1]/2;
						min = vec[index1]/2-1;
						vec.push_back(max);
						vec2.push_back(min);
					}
					else
					{
						max = vec[index1]/2;
						min = max;
						vec.push_back(max);
						vec2.push_back(min);	
					}
					index1++;
				}
				else
				{
					if(vec2[index2]%2 == 0)
					{
						max = vec2[index2]/2;
						min = vec2[index2]/2-1;
						vec.push_back(max);
						vec2.push_back(min);
					}
					else
					{
						max = vec2[index2]/2;
						min = max;
						vec.push_back(max);
						vec2.push_back(min);	
					}
					index2++;
				}
			}
			if(max == 0 && min == 0)
			{
				break;
			}
		}

		cout<<"Case #"<<i+1<<":"<<" "<<max<<" "<<min<<endl;
	}
}