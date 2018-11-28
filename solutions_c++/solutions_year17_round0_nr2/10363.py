#include <iostream>
#include<sstream>
#include<algorithm>
#include<iterator>
using namespace std;
bool check(int i)
{   bool ch;
	string st;
	stringstream convert;
	convert<<i;
	st=convert.str();
	return is_sorted(st.begin(),st.end());
    
}


int main() {
	// your code goes here
	long long int T,N,c,i;
	cin>>T;
	for(long long int t=0;t<T;t++)
	{
		cin>>N;
		for(i=N;i>0;i--)
		{
			c=check(i);
			if(c==1)
			break;
			else continue;
		}
		cout<<"Case #"<<t+1<<": "<<i<<endl;
	}
	return 0;
}