#include<iostream>
#include<string>
#include<algorithm>
#include<vector>

using namespace std;

void TidyNumber(string num)
{
	if(num.length()  == 1)
		cout<<num;
	else
	{
		vector<int> numVec(num.length());
		for(int i=0;i<num.length();++i)
		{
			numVec[i] = (int)num[i] - 48;
			//cout<<numVec[i];
		}
		//Main logic
		for(int i=1;i<numVec.capacity();++i)
		{
			if(numVec[i-1] > numVec[i])
			{
				numVec[i] = 9;
				numVec[i-1]--;
				int temp = i;
				while(temp < numVec.capacity())
				{
					numVec[temp++] = 9;
				}
				i=0;
			}
			
		}

		for(int i=0;i<num.length();++i)
		{
			if(i == 0 && numVec[i]==0)
				continue;
			cout<<numVec[i];
		}
		

		
	}
	
	
}

int main()
{
	int testcase;
	string num;
	cin>>testcase;
	int counter = 1;
	while(testcase--)
	{
		cin>>num;
		cout<<"Case #"<<counter++<<": ";
		TidyNumber(num);
		cout<<"\n";
	}
	return 0;
}