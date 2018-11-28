#include<bits/stdc++.h>
using namespace std;
#define ll long long
bool check(int k)
{
	string s= to_string(k);
	for(int i=1;i<s.length();i++)
	{
		if(s[i]<s[i-1])
			return false;
	}
	return true;
}
int fn(int k)
{
	while(check(k)==false)
		k=k-1;

	return k;
}
int main()
{
	int t=1,lim;
	cin>>lim;
	while(t<=lim)
	{
    	//Enter your code here
		int n;
		cin>>n;
		cout<<"Case #"<<t<<": ";
		
		cout<<fn(n)<<endl;
		t++;
	}

}

//How to compile & run
//	g++ readme.cpp 
//	./a.out <in.txt> out.txt
