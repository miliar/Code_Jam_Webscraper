#include<bits/stdc++.h>
using namespace std;
int arr[20];
int start=0;
bool check_tidy(long long int n){
memset(arr,0,sizeof(arr));
int i=19;
while(n){
arr[i--] = n%10;
n=n/10;
}
start = i+1;
i= start;
while(i<=18 && arr[i]<=arr[i+1])
	i++;
if(i!=19)
	return false;
else
	return true;
}

long long int cal_tidy_num(long long int n){
if(check_tidy(n))
	return n;
int i;
for(i=19; i>start; i--){
	if(arr[i] < arr[i-1]){
		arr[i] = 9;
		arr[i-1] = arr[i-1]-1;
		if(i!=19){
			int j=i;
			while(j<=18 && arr[j+1]<arr[j]){
				arr[j+1] = arr[j];
				j++;
			}
		}

	}
}
n=0;
for(int i= start; i<=19; i++){
 //cout<<arr[i]<<" ";
 n = n*10 + arr[i];
}
return n;
}
int main(){
//freopen("input.in","r",stdin);
//freopen("output.in","w",stdout);
long long int n;
int test,t;
cin>>test;
t= test;
while(test--){
	cin>>n;
	cout<<"Case #"<<t-test<<": "<<cal_tidy_num(n)<<endl;
}
}
