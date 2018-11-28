#include <iostream>
#include <bits/stdc++.h>

#include <cstring>
using namespace std;

void printTidy(long long n, int test)
{
    cout<<"Case #"<<test<<": ";
    int count=0;
    int flag=1;
	int i=0;
	int j;
	int a[20]={0};
	while(n)
	{
		int rem=n%10;
//		cout<< "rem: "<<rem<<endl;
		a[i]=rem;
		n/=10;
		i++;
	}

	for(int k=0; k<i/2; k++)
        swap(a[k],a[i-k-1]);

    for(int k=0; k<i-1; k++){
        if(a[k]<a[k+1]){
            count=0;}
        else if(a[k]==a[k+1])
        {
           count++;
        }
        else if(a[k]>a[k+1] && a[k]!=1)
        {
            a[k-count]--;
            for(int s=k-count+1; s<i; s++)
                a[s]=9;
            break;
        }
        else// if (a[k]>a[k+1] && a[k]==1)
        {
            for(int s=0; s<i-1; s++)
                cout<<9;
                flag=0;
        }
                }


    if(flag)
	for(int t=0; t<i; t++)
        cout<<a[t];

	cout<<'\n';
	return;
}


int main() {
    freopen("B-large.in","r",stdin);
    freopen("output1.out","w",stdout);
	int t;
	cin>>t;
	for(int i = 1; i<=t; i++)
	{
		long long n;
		cin>>n;
		printTidy(n, i);
	}
	return 0;
}
