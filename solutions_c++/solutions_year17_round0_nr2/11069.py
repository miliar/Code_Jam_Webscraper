#include <iostream>
#include <fstream>
#include <string>
using namespace std;
#define ll long long

int checkorder(string str1)
{
	//string str1 = to_string(number);
	int length_str1 = str1.length();
	int i = 0;
	while(i<(length_str1-1))
	{
		if(str1[i]<=str1[i+1])
		{	i++;
			continue;

		}
		else
			return 0;
		cout<<"here";
		i++;
	}
	return 1;
}
int main(int argc, char const *argv[])
{
	fstream myfile, outfile;
  	myfile.open("B-small-attempt0.in");
  	outfile.open("out.txt");
  	int i=0,j;
  	ll n,ans;
  	string num;
  	myfile>>n;
  	while(i<n)
  	{
  		myfile>>num;
  		while(num.length()>1)
  		{
  			if(checkorder(num))
  				break;
  			num = to_string(stoll(num)-1);
  		}
  		i++;
  		outfile<<"Case #"<<i<<": "<<num<<endl;
  	}

	return 0;
}