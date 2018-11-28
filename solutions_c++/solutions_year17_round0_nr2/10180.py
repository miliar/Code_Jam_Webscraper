#include <iostream> 
#include <cstdlib> 
#include <string> 

using namespace std; 

// Given an integer n, returns the largest integer x <= n that is tidy 
// namely its representation in digits is increasing (123 is, 132 is not) 


bool check_digits(int n)
{
	string s = to_string(n);
	bool flag = true; 
	for(int i=0;i< s.length()-1; i++)
	{
        int d1 =s[i+1]-'0';
        int d2 = s[i]-'0';
		if(d1 < d2 )
			flag = false;
	}
	return flag; 
}

int lazy_tidy(int n)
{
    int sol = n;
    bool flag = false;
    while( !flag){
        if( check_digits(n) )
            return n;
        n--;
    }
    return 1;
}


int main()
{
	int T; 
	cin>>T;
    int input;
    for(int i=0; i < T ; i++){
        cin>>input;
        cout<<"Case #"<<(i+1)<<": "<<lazy_tidy(input)<<endl;
    }
}
