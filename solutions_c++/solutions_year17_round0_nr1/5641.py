#include <iostream>
#include <conio.h>
#include <stdio.h>
#include <string>
#include <vector>
#include <fstream>
using namespace std;

void flip(string &, int, int);
bool check(string);
int main()
{
	int T;
	ifstream F("A-large.in");
	ofstream Fil("outputs.txt");
	vector<int> ou;
	F>>T;
	for(int i=0; i<T;i++)
	{
		string st; int k, n=0;
		F>>st>>k;
		if(check(st)) {
			ou.push_back(0);
			continue;
		}
		if(st.length()>=k){ 
			for(int j=0;j<st.length()-k+1;j++)
				if(st[j]=='+') continue;
				else {
					flip(st,k,j);
					n++;}}
		if(check(st)) ou.push_back(n);
		else ou.push_back(-1);	
	}
	for(int i=0;i<T;i++)
		if(ou[i]==-1) Fil<<"Case #"<<i+1<<": IMPOSSIBLE"<<endl;
		else Fil<<"Case #"<<i+1<<": "<<ou[i]<<endl;
	F.close();
	Fil.close();
}
void flip(string& s, int k, int j)
{
	for(int i=j;i<j+k;i++)
		if(s[i]=='+') s[i]='-';
		else s[i]='+';
}
bool check(string st)
{
	for(int i=0;i<st.length();i++)
		if (st[i]=='-') return 0;
		else continue;
	return 1;	
}
