#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <string>
#include <cstring>
#include <fstream>
using namespace std;
bool check(char arr[])
{
	char tmp[1005]="";
	strcpy(tmp,arr);
	int len = strlen(tmp);
	sort(tmp,tmp+len);
	if(strcmp(arr,tmp)==0) return true;
	return false;
}
int main()
{
	fstream outfile,infile;
	infile.open("B-small-attempt0.in",ios::in);
	outfile.open("output.txt",ios::out);
	int cas;
	infile >> cas;
	for(int t=1;t<=cas;t++)
	{
		int n;
		char arr[1005]="";
		infile >> n;
		bool ans=false;
		for(int i=n;i>=1;i--)
		{
			string str = to_string(i);
			strcpy(arr,str.c_str());
			// cout << arr << endl;
			ans = check(arr);
			if(ans)
			{
				outfile << "Case #" << t << ": "<< arr << endl;
				break;
			}
		}

	}
	return 0;
}