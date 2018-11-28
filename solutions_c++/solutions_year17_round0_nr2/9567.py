#include<iostream> 
#include<vector>
#include <fstream>
using namespace std;
bool issorted(long int n)
{
    // Note that digits are traversed from last to first
    
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
main()
{
FILE *fp=freopen("B-small-attempt2.in","r",stdin);
   freopen("output_file_name.txt","w",stdout);
long long int x;

while(!feof(fp))
{
long long int n;
cin>>x;
for(int i=0;i<x;i++)
{
	cin>>n;
	while(n>0)
	{
		if(issorted(n))
		{
			cout<<"Case #"<<i+1<<":"<<" "<<n<<endl;
			break;
		}
		n--;
		
	
	}
//	cout<<endl;
}
cin>>x;
	
}
//myfile.close();
	//return 0;
}
