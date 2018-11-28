#include <iostream>
#include <stdio.h>
#include <math.h>
using namespace std;
class TidyTest
{
	private:
		long double N;
	public:
		TidyTest()
		{
			cin>>N;
		}
		int isTidy(unsigned long long n)
		{
			unsigned int result=0, t=n%10, flag=0;
			if(t!=0)
			{
				while(n>0)
				{
					//cout<< t<<" "
					result++;
					n=(n/10)-(t/10);
					if(t>=n%10)
						flag=flag+1;
					t=n%10;
				}
				result=result==flag;
			}
			return result;
		}
		unsigned long long getLastTidyNumber()
		{
			unsigned long long i;
			for(i=N; i>9; i=i-1)
				if(isTidy(i))
					break;
			return i;
		}
};


int main(){
	int T;
	cin>>T;
	TidyTest N[T];

	for(int i=0; i<T; i++)
		cout<<"Case #"<<i+1<<": "<<N[i].getLastTidyNumber()<<endl;

	return 0;
}