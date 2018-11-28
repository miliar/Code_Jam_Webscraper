/*harry potter dynamic programming
input:There will be a number of test cases in the input.
The first line of each test case will contain n, the number of mixtures, 1 <= n <= 100.
The second line will contain n integers between 0 and 99 - the initial colors of the mixtures.

when mixing two mixtures, new colour = (a+b) mod 100 and amount of smoke produced is a*b

find minimum amount of smoke produced
*/
#include <bits/stdc++.h>

#define MAX 1000000
#define ll long long
using namespace std;







int main(){
	freopen("A-large.in","r",stdin);
	freopen("output_file","w",stdout);
	int t;
	cin>>t;
	for(int d=0;d<t;d++){
		int flag=0;
		char a[10000];
		int k;
		cin>>a;
		cin>>k;
		long long int n =strlen(a);
		long long int i = 0;
		long long int count=0,minus=0;


		while(a[i]=='+')
			i++;
		if(i==n){//all +
			cout<<"Case #"<<d+1<<": "<<"0"<<endl;
			continue;
		}
		for(ll int j=i;j<=n-1;j++){
			if( (flag==0 || flag==1 || flag==3) && a[j]=='-'){
				minus++;
				flag=1;//count -'s
				if(minus==k){//flipped
					count++;
					minus=0;
					flag=3;//flipped
				}
			}
			else if( (flag==1 || flag==0 || flag==3) && a[j]=='+'){
				if(flag==1){//minus not flipped
					for(ll int l=j-minus;l<j-minus+k;l++){
						a[l]= (a[l]=='-')?'+':'-';
						// if(a[l]=='-') a[l]='+'; else{a[l]='-'; }
					}
					count++;
					minus=1	;
					flag=1;//count +'s
				}
				else if(flag==3)
					flag=3;	  
			}
		}
        if(minus==0)
        	cout<<"Case #"<<d+1<<": "<<count<<endl;
        else
        	cout<<"Case #"<<d+1<<": "<<"IMPOSSIBLE"<<endl;


	}

	return 0;
}
