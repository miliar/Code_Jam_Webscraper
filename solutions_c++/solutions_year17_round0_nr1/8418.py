#include <bits/stdc++.h>
using namespace std;

int f(string str, int k){
	int i=0,count=0,len=str.size(),j;
	for(i=0;i<len;i++){
		cout<<i<<" "<<count<<endl;
		if(str[i]=='-'){
			if(i+k>len){
				return -1;
			}
			else{
				for(j=i;j<i+k;j++){
					str[j]=(str[j]=='-' ?'+':'-');

				}
				count++;
			}
		}

	}
	return count;
}
int main(int argc, char const *argv[]){
	int tc, m, i=0;
	string temp, temp1, temp2;

	fstream fin;
	fstream fout;

	fin.open("input1.in",ios::in);
	fout.open("output.txt",ios::out);
	fin>>temp;

	stringstream convert(temp);
	convert>>tc;
	//cin>>tc;
	while(i<tc){
		int k;
		fin>>temp1>>temp2;
		string str=temp1;
		stringstream convert(temp2);
		convert>>k; 
		cout<<str<<endl<<k<<endl;
		int ans=f(str, k);
		if(ans<0) fout<<"Case #"<<i+1<<": IMPOSSIBLE\n";
		else fout<<"Case #"<<i+1<<": "<<ans<<endl;
		i++;
	} 
	return 0;
}