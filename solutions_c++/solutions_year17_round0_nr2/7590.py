#include<iostream>
#include<vector>
#include<stdlib.h>

using namespace std;


bool isAValidNum(int n) {

 int temp=n;
 vector<int> a;

 while(temp>0) {
     	a.push_back(temp%10);
     	temp=temp/10;
 }

 for(int i=a.size()-1-1;i>=0;i--) {
 	if(! (a[i] >= a[i+1]) )
	    	return false;
 }
 return true;

}


int main(){

    int loopsLeft=0;
    int n,k=1;
    cin>>loopsLeft;
    while(loopsLeft--) {
    
    cin>>n;

    while(!isAValidNum(n--));

    cout<<"Case #"<<k<<": "<<n+1<<endl;
    k++;
    }
    return 0;
}
