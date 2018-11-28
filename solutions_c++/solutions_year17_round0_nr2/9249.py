
#include<iostream>
#include<string>

using namespace std;

bool nondecreasing(int n){
int next_digit = n%10;
	n = n/10;
	while (n)
	{
		int digit = n%10;
		if (digit > next_digit)
			return false;
		next_digit = digit;
		n = n/10;
	}

	return true;

}

int main(){
int t;
int n,p;
cin>>t;
for(int j=1;j<=t;j++){
    cin>>n;
     while(n!=0){
     if (nondecreasing(n)){
        cout<<"Case #"<<j<<": "<<n<<endl;
        break;
     }
     else{
        n--;
     }}

    }
return 0;
}

