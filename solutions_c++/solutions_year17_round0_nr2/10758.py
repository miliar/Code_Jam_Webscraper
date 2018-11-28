#include <iostream>
using namespace std;
bool areSorted(long int n)
{
   long long int next_digit = n%10;
    n = n/10;
    while (n)
    {
        long long int digit = n%10;
        if (digit > next_digit)
            return false;
        next_digit = digit;
        n = n/10;
    }
 
    return true;
}
int main(){
	int T,a=1;
	long long int N;
	cin>>T;
	while(T>0){
		cin>>N;
	    while(!areSorted(N))
	    	N--;
	    cout<<"Case #"<<a++<<": "<<N<<endl;	
		T--;
	}
	return 0;
}
