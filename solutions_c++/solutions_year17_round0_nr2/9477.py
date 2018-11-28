#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include<iomanip>
#include <algorithm>
#include <functional>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>
#include <bitset>
using namespace std;
#define MOD 1000000007
int main(void){
	ifstream cin("B-large.in");
	ofstream cout("output.txt");
	std::ios::sync_with_stdio(false);cin.tie(0);
	int t,T;
	string s;
	int i,j,n;
	char themin;
	cin>>T;
	for(t=1;t<=T;t++)
	{
		cin>>s;
		n=s.length();
		themin=s[n-1];
		for(i=n-2;i>=0;i--)
			if(s[i]>themin)
			{
				s[i]--;
				for(j=i+1;j<n;j++)
					s[j]='9';
				themin=s[i];
			}
			else
				themin=s[i];
		cout<<"Case #"<<t<<": ";
		if(s[0]!='0')
			cout<<s[0];
		for(i=1;i<n;i++)
			cout<<s[i];
		cout<<'\n';
	}
	system("pause");
	return 0;
}