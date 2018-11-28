
#include<fstream>
#include<conio.h>
using namespace std;
int main()
{

	ifstream f("B-small-attempt0.in");
	ofstream s("cj1.out",ios::app);
	int t;
	f>>t;
	long long int a;
	int b;
	int i;
	long long int j;s
	char c[]="Case #";
	for(i=0;i<t;i++)
	{
	
		long long int n;
		f>>n;
		s<<c;
		s<<(i+1);
		s<<": ";
		for(j=n;j>=0;j--)
		{
				int flag=1;
			a=j;
			b=a%10;
			a/=10;
			while(a>0)
			{
				int temp=a%10;
				if(temp>b)
				{
					flag=0;
					break;
					}	
					b=temp;
					a/=10;
			}
			if(flag==1)
			break;
		}
		s<<j;
			s<<'\n';
	}
f.close();
s.close();
return 0;
}
