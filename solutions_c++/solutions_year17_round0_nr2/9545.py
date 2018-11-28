#include<bits/stdc++.h>
#define ll long long
using namespace std;
#define INF 1000000000000

int main()
{
    //ifstream cin; cin.open("file.txt"); ofstream cout; cout.open("fileout.txt"); //comment while testing.
    ll t;
    cin>>t;
    for(int testcase=1;testcase<=t;testcase++)
    {
        ll n;
        cin >> n;
        int ar[19];
        int i=0;
        ll temp;
        temp=n;
        while(temp!=0){
        	ar[i]=temp%10;
        	temp=temp/10;
        	i++;

        }
        int count=0;
        int count1=0;
        for(int j=0; j<i-1; j++){
        	if(ar[j]==-1 )
        		count++;
        
        	if(count==1 || ar[j]<ar[j+1]){
        		for(int k=0; k<j; k++)
        			ar[k]=9;
        	}
        	if(ar[j]<ar[j+1] || ar[j+1]==0){
        		ar[j]=9;
        		ar[j+1]=ar[j+1]-1;

        }
    }
        ll mul=1,num=0;
        for(int j=0; j<i; j++){
        	num += (ll)ar[j]*mul;
        	mul *= 10;


        }
        cout<<"Case #"<<testcase<<": "<<num<<endl; // answer
        	
    }
    return 0;
}