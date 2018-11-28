#include <bits/stdc++.h>
using namespace std;


bool check(long long n){
	vector <int> digits;
	while(n>0){
		digits.push_back(n%10);
		n=n/10;
	}
	for (int i=0; i<digits.size()-1; i++)
		if(digits[i]<digits[i+1]) return false;
	return true;
}

int main(int argc, char const *argv[])
{
	long long tc,n,i=0;
	string temp;
	fstream fin;
	fstream fout;
	fin.open("input.in",ios::in);
	fout.open("output.txt",ios::out);
	fin>>temp;

	stringstream convert(temp);//object from the class stringstream
	convert>>tc; 

	cout<<tc<<endl;
	while(i<tc){
		fin>>temp;
		cout<<temp<<endl;
		stringstream convert(temp);//object from the class stringstream
		convert>>n;
		//cin>>n; 
		while(check(n)==false)
			n--;
		fout<<"Case #"<<i+1<<": "<<n<<endl;
		i++;
	}
	return 0;
}