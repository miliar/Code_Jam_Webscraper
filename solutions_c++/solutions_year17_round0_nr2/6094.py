#include<iostream>
#include<math.h>
/*


Input

Output

4
132
1000
7
111111111111111110

Case #1: 129
Case #2: 999
Case #3: 7
Case #4: 99999999999999999

*/
using namespace std;
long long int powten(int coun)
{
    if(coun==0)
        return 1;
    return 10*powten(coun-1);
}
int main()
{
	int t;
	cin>>t;
	for(int f=1;f<=t;f++){
		long long int n,ans;
		int prev;
		cin>>n;
		//cout<<n;
		ans = n;
		prev = n%10;
		n= n/10;
		long long int coun = 1 ;
		while(n>0)
		{
			long long int val = n%10;

			if(val>prev)
			{
				ans = ans- ans%(long long int)ceil(pow(10,coun)) - 1;
			}
			long long int temp = ans/powten(coun);
			prev = temp%10;
			n = n/10;
			coun++;
		}
		cout<<"Case #"<<f<<": "<<ans<<endl;
	}
}
