#include "stdafx.h"

#include <iostream>
#include <string>

using namespace std;

int main()
{
	int ncase, k, a;
	int i;
	string s;
	cin>>ncase;
	for (int icase=1;icase<=ncase;icase++) {
		cin>>s>>k;
		int l = s.length();
		a=0;
		for (i=0;i<=l-k;i++)			
			if (s[i]=='-') {
				for (int j=0;j<k;j++)
					s[i+j] = (s[i+j]=='+')?'-':'+';
				a++;
			}
		//cout<<s<<a;
		for (;i<l;i++)
			if (s[i]=='-') {a=-1; break;}		
		if (a>=0)			
			cout << "Case #" << icase << ": " << a << "\n";
		else
			cout << "Case #" << icase << ": IMPOSSIBLE\n";
	}
}