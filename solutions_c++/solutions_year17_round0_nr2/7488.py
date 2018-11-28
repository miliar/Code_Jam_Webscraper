#include<iostream>
#include<algorithm>
#include<vector>
#include<set>
#include<stdlib.h>
#include<queue>
#include<math.h>

using namespace std;


bool isValid(int n) {

 int temp=0;
 vector<int> vec;
 temp=n;

 while(temp>0) {
     	vec.push_back(temp%10);
     	temp/=10;
 }
 for(int i=vec.size()-2;i>=0;i--) {
 	if(vec[i]<vec[i+1])
	    	return false;
 }
 return true;

}
int main(){

    int tests=0;
    int n,k=1;
    cin>>tests;
    while(tests--) {
    
    cin>>n;
    while(n) {
    	if(isValid(n))
		break;

    	n--;

    }

    cout<<"Case #"<<k<<": "<<n<<endl;
    k++;
    }
    return 0;
}
