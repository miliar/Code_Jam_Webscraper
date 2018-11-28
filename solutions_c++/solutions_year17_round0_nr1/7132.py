// gcj-1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>

using namespace std;

int main(int argc, _TCHAR* argv[])
{
	char c;
	int t, k, T;
	cin>>T;
	bool arr[1001] = {0};
	t = 1;
	while(t <= T) {
		int i = 0;
		while(true) {
			cin>>noskipws>>c;
			switch(c) {
				case '+':
					arr[i++] = true;
					break;
				case '-':
					arr[i++] = false;
					break;
			}
			if(c == ' ')
				break;
		}
		cin>>k;

		int j = 0, n= 0;
		for(j = 0; j<i; j++) {
			if(arr[j])
				continue;
			else {
				if(j+k <= i){
					for(int u =0; u<k; u++){
						arr[j+u] = !arr[j+u];
					}
					n++;
				} else
					break;
			}
		}
		if(j==i)
			cout<<"Case #"<<t<<": "<<n<<endl;
		else
			cout<<"Case #"<<t<<": IMPOSSIBLE"<<endl;
		t++;
	}
	return 0;
}

