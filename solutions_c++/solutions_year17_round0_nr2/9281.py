#include <iostream>
#include <sstream>
#include <fstream>
#include <stdint.h>

using namespace std;

uint64_t Tidy_Numbers(uint64_t s)
{
	int m=0;
	uint64_t p = s;
	while(p>0){
		p=p/10;
		m++;
	}
	int n=m;
	int arr[n];
	uint64_t k;
	k = s;
	for(int i = 0;k>0;i++)
	{
		arr[n-i-1] = k%10;
		k = k/10;
	}
	bool b = true;
	for(int i=n-1;i>=1;i--)
	{
		if(arr[i]<arr[i-1])
		{
			arr[i] = 9;
			arr[i-1]-=1;
			b = false;
		}
	}
	if(b==false)
	{
	for(int i=0;i<n-1;i++)
	{
		if(arr[i]>arr[i+1])
		{
			arr[i+1] = 9;
		}
	}
	}
	uint64_t x=0;
	for(int i = 0;i<n;i++)
	{
		x=x*10+arr[i];
	}
	return x;
}

int main()
{
	uint64_t data;
	ifstream infile;
	infile.open("E:\\GCJam\\B-large.in");
	ofstream outfile;
	cout << "Reading from the file" << endl; 
	int test_cases,i;
	infile>>test_cases;
	i = test_cases;
	while(i)
    {
	infile >> data;
	uint64_t v = Tidy_Numbers(data);
	cout<<data<<endl;
	outfile.open("E:\\GCJam\\Problem_B_Tidy_Numbers_output_large.txt",ios::app);
	outfile<<"Case #"<<test_cases-i+1<<": "<<v<<endl;
	outfile.close();
    i--;
	}
	infile.close();
}
