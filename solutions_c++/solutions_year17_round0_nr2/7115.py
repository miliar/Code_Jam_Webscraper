// gcj2.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <string>
#include <iostream>

using namespace std;

int main(int argc, _TCHAR* argv[])
{
	string s;
	int T;
	int t = 1;
	cin>>T;
	getline(cin, s);
	while(t <= T) {
		string arr;
		getline(cin, arr);
		int len = arr.length();
		for(int i = len - 1; i>=0; i--) {
			if(i>0) {
				if(arr[i] < arr[i-1]) {
					int k = i;
					while(k<len)
						arr[k++] = '9';
					arr[i-1] = arr[i-1] - 1;
				} else if(arr[i] == '0')
					arr[i] = '9';
			}
		}
		int i = 0;
		while(arr[i] == '0' && i < len) i++;
		cout<<"Case #"<<t<<": ";
		while(i < len)
			cout<<arr[i++];

		cout<<endl;
		t++;
	}
	return 0;
}

