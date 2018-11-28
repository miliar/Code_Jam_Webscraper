#include <bits/stdc++.h>
#define ulli unsigned long long int
using namespace std;

int main(){
    fstream fin,fout;
    fin.open("inputm.in");
    fout.open("output.txt");
	int t;
	fin>>t;
	for (int cs=1; cs<=t; cs++){
		fout<<"Case #"<<cs<<": ";

		ulli n, k;
		fin>>n>>k;
		priority_queue<ulli> arr;
		arr.push(n);
		ulli temp;
		temp = n;
		for (int i=0; i<k-1; i++){
			temp = arr.top();
			arr.pop();
			if (temp%2){
				arr.push(temp/2);
				arr.push(temp/2);
			} else {
				arr.push(temp/2);
				arr.push((temp/2)-1);
			}
		}
		temp = arr.top();
		if (temp%2){
			fout<<temp/2<<" "<<temp/2;
		} else {
			fout<<temp/2<<" "<<((temp/2)-1);
		}

		fout<<endl;
	}
	return 0;
}
