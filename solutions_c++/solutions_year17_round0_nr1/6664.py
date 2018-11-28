#include <iostream>
#include <vector>

using namespace std;

int main()
{
	int t;
	cin >> t;
	for(int r=1 ; r<=t;r++)
	{
		vector<char> v;
		string s;
		cin >> s;
		int k , count1=0 , count=0 , index=0;
		cin >> k;
		for(int i=0;i<s.length();i++)
		{
			bool flag1 = false;
			if(s[i]=='-' || count1>0) 
			{
		//		cout << " s if is " << s << endl;
				count1++;
			}
			
			if(count1 == k)
			{
				count1=0;
				count++;
				for(int j=i-k+1;j<i+1;j++)
				{
					if(s[j]=='+')
						s[j] = '-';
				 else
						s[j] = '+';
			 	}
			 	for(int j=i-k+1;j<i+1;j++)
			 	{
			 		if(s[j]=='-')
					{
						flag1=true;
						index = j;
						break;
					}	
				}
				if(flag1==true)
					i = index-1;
		//		cout << "j is" << index << endl;
		//	 	cout << "s is " << s << endl;
			}
			
		}
		bool flag = true;
		//cout << "s end  is " << s << endl;
		for(int i=0;i<s.length();i++)
		{
			if(s[i]=='-')
			{
				flag = false;
				break;
			}
		}
		if(flag == false)
			cout << "Case #" << r << ": " << "IMPOSSIBLE" << endl;
		else
			cout << "Case #" << r << ": " <<  count << endl;	
	}
	
	return 0;
}
