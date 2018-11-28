#include<iostream>
#include<fstream>
using namespace std;
int main()
{
	unsigned int t,cas=1,ans;
	ofstream outfile("output.txt");
	cin>>t;
	while(t--)
	{
		unsigned long long int n,num,i=10,nd,pd;
		cin>>n;
		if(n<10)
		{
			outfile<<"Case #"<<cas++<<": "<<n<<endl;
			continue;
		}
		num=n;
		while(num)
		{
			pd=(num%10);
			num=num/10;
			nd=num%10;
			if(nd>pd)
			{
				num--;
				n=num*i+(i-1);
			}
			//cout<<num<<" "<<nd<<" "<<pd<<endl;
			i=i*10;
		}
		//cout<<n;
		outfile<<"Case #"<<cas++<<": "<<n<<endl;
	}
	return 0;
}
