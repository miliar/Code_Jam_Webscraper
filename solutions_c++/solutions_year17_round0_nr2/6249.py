#include<fstream>
#include<iostream>
#define ll long long
using namespace std;

ll int fn(ll int temp){
	int d[30];
	for(int j=0;j<30;j++)d[j] = -1;
	int i;
	for(i=0;temp;i++){
		d[i] = temp%10;
		temp /= 10;
	}i--;
	for(int j=0;i>j;j++){
		if(d[j] < d[j+1]){
			for(int k=0;k<=j;k++)
				d[k] = 9;
			d[j+1]--;
		}
	}
	for(;i>=0;i--){
		temp *= 10;
		temp += d[i];
	}
	return temp;
}

int main(){
	int T;
	ll int n;
	ifstream fin("in.txt");
	ofstream fout("out.txt");
	fin>>T;
	for(int i=0;i<T;i++){
		fin>>n;
		fout<<"Case #"<<i+1;
		fout<<": "<<fn(n)<<endl;
	}
}
