#include<iostream>
#include <string> 


using namespace std;

bool check(int number)
{
	string s = to_string(number);
	 int len = s.length();
	 
	for(int j =0;j<len-1;j++)
	{
		if(s[j] > s[j+1])
			return false;
	}
	return true;
}

int main(void){
int T ;

cin>>T;

for(int i=0;i<T ; i++)
{	
	int n;
	cin>>n;
	while(!check(n))
	{
		n--;
	}
	
	cout<<"Case #"<<i+1<<": "<<n<<endl;
	
}


return 0;
}

