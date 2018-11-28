//#include <bits/stdc++.h>
 #include <iostream>
 #include <string>
using namespace std;
int main(){
	long t,n,ans;
	cin>>t;
	long case_no=1;
	while(t--){
		cin>>n;
		string s = to_string(n);
		long len = s.length();
		long my_int = stol(s);

		if(len == 1)
			ans = n;
		else
		{
			long j, k;
			long index = len-1;
			long temp[len];
			for(long i=0;i<len;i++)
			{
				temp[i] = s[i] - '0';
			}
			for(long i=len-1;i>0;i--)
			{
				j = temp[i];
				k = temp[i-1];
				if(j<k)
				{
					for(long z = i;z<=index;z++)
					{
						temp[z] = 9;
					}
					temp[i-1] = k-1;
				}
				if(j==k)
				{
					temp[i] = j;
					temp[i-1] = k;
				}
			
			}
			long start;
			if(temp[0] == 0)
			{
				start = 1;
			}
			else
			{
				start = 0;
			}
			string final;
			for(long y=start;y<len;y++)
			{
				final = final + to_string(temp[y]);
			}
			ans = stol(final);
			
		}
		
		cout<<"Case #"<<case_no<<": "<<ans<<endl;
		case_no++;
	}
	return 0;
}
