# include <iostream>
bool sort(unsigned long long  n){
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
	std::cin>>t;
	int c=1;
	while(t--){
		unsigned long long  n;
		std::cin>>n;
		for(unsigned long long  i=n;i>0;i--){
			if(sort(i)){
				std::cout<<"Case #"<<c<<": "<<i;
				c++;
				break;
			}
		}
		std::cout<<"\n";
	}
	return 0;
}