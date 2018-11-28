#include <iostream>
#include <cstring>
using namespace std;

bool check(string s)	{
	for(unsigned int i = 1 ; s[i] != '\0' ; i++)	{
		if(s[i] < s[i-1])
			return false;
	}
	return true;
}

int main() {
	// your code goes here
	int t;
	cin>>t;
	for(int i = 1 ; i <= t ; i++)	{
		unsigned long long int n;
		cin>>n;
		if(n < 10)	{
			cout<<"Case #"<<i<<": "<<n<<endl;
			continue;
		}
		A:
		string s = to_string(n);
		if(check(s) == true)
			cout<<"Case #"<<i<<": "<<s<<endl;
			
		else	{
			n--;
			goto A; 
		}
	}
	return 0;
}