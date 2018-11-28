#include<iostream>
#include<stdio.h>
#include<conio.h>
using namespace std;
int main(){
	int T;
    int c=0,j=0,g=0;
	cin>>T;
	int num[T],a[T][10],out[T];
	for (int i = 0; i < T; i++)
	{
		cin>>num[i];
		int k=num[i];
		if(num[i]<10){
                        out[i]=num[i];
                        goto RESULT;

                }
		for (k = num[i]; k > 0; k--)
		{
			c=0,j=0,g=k;
			while(g>0){
				a[i][c]=g%10;
				g=g/10;
				c++;
			}
		while(j<c-1){

				if(a[i][j]<a[i][j+1]){
					out[i]=0;
					break;
				}else{
					out[i]=k;
				}
			j++;
			}
RESULT:
			if(out[i]==k)
                break;
		}
	}

	for (int i = 0; i < T; i++)
	{
		cout<<"CASE #"<<i+1<<": "<<out[i]<<"\n";
	}
	return 0;
}
