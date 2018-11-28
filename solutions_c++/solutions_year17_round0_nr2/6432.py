#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <fstream>
#define lli long long int
#define MAX 100
#define li long int
using namespace std;
int main()
{
    ifstream input;
    input.open("input.in");
    ofstream output;
    output.open("output.txt");
    int i,index;
    int t;
    input>>t;
    bool flag=true;
    for(int tt=1;tt<=t;tt++)
    {
        string str;
        input>>str;

        flag=true;
		char maximum=48;
		index=0;
		for(i=0;i<str.length()-1;i++)
            {
			if(str[i+1] < str[i]){
				flag=false;
				if(str[i] == maximum){
					str[index]=str[index]-'1'+'0';
					break;
				}
				str[i]--;
				index=i;
				break;

			}
			if(maximum<str[i]){
				maximum = str[i];
				index = i;
			}
		}
		i=0;
		if(str[0] == 48)
            i++;
		output<< "Case #" << tt << ": ";
		while(i<str.length())
		{
			if(!flag && i > index)
			output << 9;
			else output << str[i];
			i++;
		}
		output << endl;
}
return 0;
}
