#include <iostream>

#include <conio.h>
using namespace std;
int main()
{
	int N = 11;
	static int a[10];
	int i = 1;
	int flag = 0;
	long long number;// = 100000000000000000;
	int in;
	int testCases = 1;
	int testCases1 = 1;
	long long largestTidy = 1;
	int tidyFlag = 0;
	int notTidyFlag = 0;
	

	FILE *fp;
	fp = fopen("testcase.in", "r+");

	FILE *fp1;
	fp1 = fopen("output.in", "w+");

	fscanf(fp, "%d", &testCases1);


	while (fscanf(fp, "%lld", &number) != EOF)
	{
		i = 1;
		
		
		
		while (number > 0 && tidyFlag == 0)
		{
			notTidyFlag = 0;
			cout << number << endl;
			long long temp = number;
			if (temp / 10 == 0)
			{
				flag = 1;
				largestTidy = temp;
				break;

			}
			long long prev = -1;
			long long cur = -1;

			while ((temp / 10) != 0)
			{
				
				cur = temp % 10;
				if (prev == -1)
				{
					prev = cur;
					temp = temp / 10;
					
					continue;
				}
				if (prev < cur)
				{
					notTidyFlag = 1;
					break;
				}
				prev = cur;
				temp = temp / 10;
			}

			if (notTidyFlag == 0)
			{
				cur = temp % 10;

				if (prev < cur)
				{
					notTidyFlag = 1;
					
				}
				else
				{
					largestTidy = number;
					break;
				}
			}
			
			
			number--;
			
		}
	
			std::cout << "case #" << testCases << ": " << number << endl;
			fprintf(fp1, "case #%d: %lld\n", testCases, number);
			flag = 0;
	
		testCases++;
	}


		std::cout << "\nLargest Tidy Flag" << largestTidy << endl;




	return 0;
}