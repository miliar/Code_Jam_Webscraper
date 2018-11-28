#include<iostream>
using namespace std;
int main()
{
	int t;
	string inp,out;
	string::iterator s,e;
	char temp;
	unsigned long long int j,k,l;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		cin>>inp;
		l=inp.length();
		for(j=l-1;j>0;j--){
			if(inp[j-1]>inp[j]){
				for(k=j;k<l&&inp[k]!='9';k++)
					inp[k]='9';
				inp[j-1]=inp[j-1]-1;
			}
		}
		s=inp.begin();
		while((*s)=='0')
			s++;
		e=inp.end();
		out.assign(s,e);
		cout<<"Case #"<<i+1<<": "<<out<<endl;

	}

	return 0;
}
