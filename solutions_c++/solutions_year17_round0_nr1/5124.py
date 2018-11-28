#include<bits/stdc++.h>
using namespace std;
string s ;
void revers(int end , int k ){
for(int i = end-k ;  i<=end ; i++){
	if(s[i]=='+')
		{s[i] = '-';
}
	else
		s[i]= '+';

}
}
int main(){
    fstream fin,fout;
    fin.open("inputl.in");
    fout.open("output.txt");
	int t;
	int m=1 , k ;
	fin>>t ;
	t++;
	while(m!=t){
		int count=0, flag = 0;
		fin>>s;
		fin>>k;
		int ss = s.size();
		for(int i = ss-1; i>=(k-1);i--){
			if(s[i]=='-')
			{	//s[i]='+';
				count++;
				revers(i, k-1);
			}

		}
		for(int i = 0 ; i <ss-1 ;i++){
			if(s[i]=='-'){
				flag=1;
			}
		}
		if(flag==1){
				fout<<"Case #"<<m<<": "<<"IMPOSSIBLE"<<endl;


		}
		else
		fout<<"Case #"<<m<<": "<<count<<endl;
		m++;
	}

	return 0;
}
