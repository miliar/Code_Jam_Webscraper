#include<bits/stdc++.h>
using namespace std;
#define pi 3.14159265358979323846
#define ull unsigned long long
#define ll long long
#define MOD 1000000007
int main(){
	#ifndef ONLINE_JUDGE
		freopen("inp.txt","r",stdin);
		freopen("out.txt","w",stdout);
	#endif
	int t,q=1;
	cin>>t;
	string arr,arr1;
	while(t--){
	cin>>arr;
	int f=0;
	int len=arr.length();
     for(int i=0;i<len-1;i++)
     {
		if(arr[i]>arr[i+1])
		{
		f=1;break;}
		
	 }
	 
	 if(f==0)
	 {
	 	cout<<"Case #"<<q<<": "<<arr<<endl;
	 }
	
	 else
	 {
	 if(arr.length()==1)
	 cout<<"Case #"<<q<<": "<<arr<<endl;
	 else
	  {
	  
	 
	 int j=len-1;
	 char s[21];
	 strcpy(s,arr.c_str());
	 ll num=atoll(s);
	 
	 do{
	 
	 f=0;
	 
	 string arr2;
	 arr2=arr.substr(j);
	 char s2[21];
	 strcpy(s2,arr2.c_str());
	 ll  val=atoll(s2);	
	 
	 ll num1=(ll)(num-(val+1));
	 
	 char s1[21];
	 sprintf(s1,"%lld",num1);
	 
	 
	 arr1=s1;
	 if(arr1.length()==1)
	 break;
	 for(int i=0;i<arr1.length()-1;i++)
     {
		if(arr1[i]>arr1[i+1])
		{
		f=1;break;}
		
	 }
	 if(f==0)
	 break;
	 j--;
	 }while(j>=0);
	 	
	 	cout<<"Case #"<<q<<": "<<arr1<<endl;
	 }
	 
     }
	 q++;
	 
	}
	return 0;
}

