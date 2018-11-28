#include<iostream>
#include<string>
using namespace std;
int main(){
	int TT;
	cin>>TT;
	string s;
	long long int n;
	int a[20];
	int l;
	for(int T=1;T<=TT;++T){
	    cin>>n;
	    long long int tmp = n;
	    l=0;
	    while(tmp>0){
	        a[l]=tmp%10;
	        ++l;
	        tmp/=10;
	    }
	    cout<<"Case #"<<T<<": ";
	    int j=0;
	    for(int i=1;i<l;++i){
	        if(a[i]>a[i-1]){
	            a[i]-=1;
	            j=i;
	        }
	    }
	    int i=l-1;
	    while(a[i]==0&&i>=j)
	        --i;
	    for(;i>=0;--i){
	        if(i>=j)
	            cout<<a[i];
	        else{
	            cout<<9;
	        }
	    }
	    cout<<"\n";
	}
	return 0;
}
