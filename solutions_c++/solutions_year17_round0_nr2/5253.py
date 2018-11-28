#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <cstdlib>
#include <stdio.h>
#include <string>
#include <list>
#include <vector>
#include <queue>
#include <utility>
#define for0(i,n) for(int i=0; i<n; i++)
#define for1(i,n) for(int i=1; i<n; i++)
#define FOR(i,o,n,s) for(int i=o; i<n; i+=s)
#define refor0(i,n) for(int i=n-1; i>=0; i--)
#define pb push_back

using namespace std;  // since cin and cout are both in namespace std, this saves some text

int main() {
	int dataNum;
	cin >> dataNum;

	int i, j, k;
	string num;
	FOR(i, 0, dataNum, 1) {
		cin>>num;
		int numArr[num.length()];
		FOR(j, 0, num.length(), 1) {
			numArr[j]=num[j]-'0';
		}

		for(j=num.length()-1; j>=1; j--) {
			if(numArr[j-1]>numArr[j]) {
				if(numArr[j-1]==0) {
					for(k=0; k<=j-1; k++)
						numArr[k]=0;
				} else {
					numArr[j-1]--;
				}

				for(k=j; k<num.length(); k++)
					numArr[k]=9;
			}
		}

		bool head=true;
		cout<<"Case #"<<i+1<<": ";
		FOR(j, 0, num.length(), 1) {
			if(head && numArr[j]==0) continue;
			cout<<numArr[j];
		}
		cout<<endl;
	}
}