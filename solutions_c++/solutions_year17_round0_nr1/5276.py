#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <cstdlib>
#include <stdio.h>
#include <string>
#include <list>
#include <vector>
#include <queue>
#include <utility>
#include <math.h>
#include <float.h>
#include <bitset>
#define for0(i,n) for(int i=0; i<n; i++)
#define for1(i,n) for(int i=1; i<n; i++)
#define FOR(i,o,n,s) for(int i=o; i<n; i+=s)
#define refor0(i,n) for(int i=n-1; i>=0; i--)
#define pb push_back

using namespace std;  // since cin and cout are both in namespace std, this saves some text

bool isAllHappy;
int ttlTimes;

bool isHappy(int arr[], int len) {
	int sum=0;
	int i;
	FOR(i, 0, len, 1)
		sum+=arr[i];
	return sum==len;
}

void output(int arr[], int arrLen) {
	for(int i=0; i<arrLen; i++)
		cout<<arr[i];
	cout<<endl;
}

void flip(int arr[], int arrLen, int flipIdx, int flipNum, int times) {
	if((flipIdx+flipNum) > arrLen) return;
	
	int tmpArr[arrLen];
	for(int i=0; i<arrLen; i++) tmpArr[i]=arr[i];
	
	times++;
	for(int i=flipIdx; i<flipIdx+flipNum; i++) {
		if(tmpArr[i]==1) tmpArr[i]=0;
		else tmpArr[i]=1;
	}

	if(isHappy(tmpArr, arrLen)) {
		isAllHappy=true;
		ttlTimes=times;
		return;
	}

	for(int i=flipIdx+1; i<arrLen; i++) {
		flip(tmpArr, arrLen, i, flipNum, times);
	}
}

int main() {
	int dataNum;
	cin >> dataNum;

	int i, j, k;
	FOR(i, 0, dataNum, 1) {
		isAllHappy=false;
		string pencake;
		int flipNum;
		cin>>pencake;
		int pencakeArr[pencake.length()];
		FOR(j, 0, pencake.length(), 1) {
			if(pencake[j]=='+') pencakeArr[j]=1;
			else pencakeArr[j]=0;
		}
		cin>>flipNum;
		if(isHappy(pencakeArr, pencake.length())) {
			isAllHappy=true;
			cout<<"Case #"<<i+1<<": 0"<<endl;
		} else {
			FOR(k, 0, pencake.length(), 1) {
				flip(pencakeArr, pencake.length(), k, flipNum, 0);
				if(isAllHappy) {
					cout<<"case #"<<i+1<<": "<<ttlTimes<<endl;
					break;
				}
			}
		}
		if(!isAllHappy) cout<<"Case #"<<i+1<<": IMPOSSIBLE\n";

	}

}