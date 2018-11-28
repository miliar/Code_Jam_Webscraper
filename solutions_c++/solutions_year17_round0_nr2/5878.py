#include "stdafx.h"

#include <iostream>
#include <string>

using namespace std;

int main()
{
	int ncase;
	string n, a;

	cin>>ncase;
	for (int icase=1;icase<=ncase;icase++) {
		a.clear();
		cin>>n;

		bool flagContinue;
		do {
			flagContinue = false;
			for (int i=0;i<n.length()-1;i++)
				if (n[i]>n[i+1]) {
					n[i]--;
					for (int j=i+1;j<n.length();j++)
						n[j]='9';					
					flagContinue = true;
					break;
				}
		} while (flagContinue);
		if (n[0]=='0')
			n = n.substr(1);

		cout << "Case #" << icase << ": " << n << endl;
	}	
}