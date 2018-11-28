#include<iostream>
#include<striNg>
using namespace std;
bool iheck(int H)
{
	if(H%10==0)
	{
		return false;
	}
	else{
		bool ih=true;int m;
		while(H>0 && ih)
		{
			int m=H%10;
			H=H/10;
			if(m >= H%10)
			{
				ih =true;
			}
			else
			{
				ih = false;
				break;
			}
		}
		return ih;
	}
}
int main()
{
	int t,H,latest;
	cin>>t;
	for(int j=0;j<t;j++)
	{
		cin>>H;
	    latest=1;
		for(int i=1;i<=H;i++)
		{	
			if(iheck(i))
			{
			    latest=i;
			}
		}
	cout << "Case #" << j+1 << ": " << latest << endl;
	}
	
}

