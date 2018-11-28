#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;


int main()
{
	 ifstream myfile ("q.in");
  	
  	ofstream outfile;
  	outfile.open("output.txt");
  	
	int t;
	myfile >> t;
	string input;
	int h;
	for(h=0;h<t;h++)
	{
	
	//outfile << h<<endl;
	myfile >> input;
	/*while(1)
	{
		input.insert(input.begin(),s%10);
		s=s/10;
		if(s==0) break;
	}*/
	
	int flag=0;
	if(input.length()==1) {outfile << "Case #"<<h+1<<": "<< input[0]<<endl;continue;}
	while(1)
	{
		int i;
		int f=0;
		for(i=0;i<input.length();i++)
		{
			if(input[i]>input[i+1] && f==0 && i<input.length()-1)
			{
		
				f=1;
				input[i]=input[i]-1;
				continue;
			}
			if(f==1)
			{
				input[i]='9';
			}
		}
		if(f==0) break;
	}
	int j;
	outfile<<"Case #"<<h+1<<":"<<" "; 
	for(j=0;j<input.length();j++)
	{
		if(input[j]!='0') outfile<<input[j];
	}
	outfile<<endl;
	}
  myfile.close();
	return 0;
}

