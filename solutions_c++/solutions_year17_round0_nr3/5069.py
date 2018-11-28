#include <algorithm>
#include <iostream>
#include <cmath>
#include <bitset>
#include <sstream>
#include <string>
#include <vector>

typedef   long long int bigint;

using namespace std;

int main(){

	int a;
	bigint n,k;
	cin>>a;
	int all=a;
	while(a){
		cin>>n>>k;


		bigint *v=new bigint[k]();
		bigint ls=0,rs=0;

		v[0]=n;
		bigint i=0;
		bigint j=0;
		bigint store=1;
		while(i<k){
			bigint large=v[i];
			if(large%2==1){
				ls=(large-1)/2;
				rs=ls;
			}else{
				rs=large/2;
				ls=max((bigint)0,(large)/2-1);
			}
			
			if(j==k) j--;
			if(j==-1) j++;
			while(j>=0 && rs>v[j]) j--;
			while(j<k && rs<=v[j]) j++;
			
			if(store<k){
				v[store]=rs;
			 	if(j<store){		
					swap(v[store],v[j]);
				}
				store++;//rs>=ls
			}else if(j<k){
				v[j]=rs;
			}
				
			if(store<k){
				v[store]=ls;
				store++;
			}
			
			i++;	
		}
		cout << "Case #" << all-a+1 << ": " << max(ls,rs)<<" "<<min(ls,rs)<< endl;
		a--;
		
	}
	return 0;
}
