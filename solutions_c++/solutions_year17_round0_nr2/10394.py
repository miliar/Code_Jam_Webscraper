#include <bits/stdc++.h>
#include <algorithm>
using namespace std;
bool test(vector<int> v) {
    for(int i = 0; i < v.size()-1; i++)
        if(v[i] > v[i+1])
            return false;
    return true;
}
int main(){
	int t,k,n,choice;
	vector<int> digits;
	cin>>t;
	for(int i=1;i<=t;++i){
		cin>>n;
		k=n;
		while(k>0){
			digits.push_back(k%10);
			k/=10;
		}
		reverse(digits.begin(),digits.end());
		if(test(digits))
			choice=1;
		else
			choice=2;
		if(choice==1)
			cout<<"Case #"<<i<<": "<<n<<endl;
		else{
			cout<<"Case #"<<i<<": ";
			if(n==1000)
				cout<<"999"<<endl;
			else if(n==10)
				cout<<"9"<<endl;
			else if(digits.size()==2)
				cout<<digits[0]-1<<"9"<<endl;
			else{
				if(digits[1]<digits[0]){
					if(n<110)
						cout<<"99"<<endl;
					else
						cout<<digits[0]-1<<"99"<<endl;
				}
				else if(digits[2]<digits[1]){
					if(digits[1]-digits[0]>=1)
						cout<<digits[0]<<digits[1]-1<<"9"<<endl;
					else
						cout<<digits[0]-1<<"99"<<endl;
				}
			}
		}
		digits.clear();	
	}
	return 0;
}