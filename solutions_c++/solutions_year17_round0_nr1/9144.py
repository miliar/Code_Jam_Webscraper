#include <iostream>
#include <stdio.h>
#include <conio.h>
#include <string.h>
using namespace std;
char a[1000];
int k;
int main(){
	int T,sum;
	cin>>T;
	int out[T];
	for (int c = 0; c < T; c++)
	{
		int k;
		out[c]=0;
		cin>>a>>k;
	for (int i = 0; i < strlen(a)-k+1; i++)
	{
		if(a[i]=='-'){
			for(int l=0; l<k; l++){
				if(a[i+l]=='-')
					a[i+l]='+';
				else
					a[i+l]='-';
			}
			out[c]++;
		}
	}
	sum=0;
	for (int i = 0; i < strlen(a); i++)
	{
		if(a[i]=='+')
			sum++;
	}
	if (sum!=strlen(a))
		out[c]=-1;
	}
	for (int i = 0; i < T; i++)
	{
		if(out[i]==-1)
			cout<<"CASE #"<<i+1<<": IMPOSSIBLE \n";
        else
            cout<<"CASE #"<<i+1<<": "<<out[i]<<"\n";
	}
	return 0;
}
