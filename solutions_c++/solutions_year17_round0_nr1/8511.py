#include<iostream>
using namespace std;

class Oversized
{
	private:
	int t;
	string s;
	int k;
	int flips;
	
	public:
	Oversized(int x)
	{
		flips = 0;
		t = x;
		
		cin>>s>>k;
		
		int* arr = new int[s.length()];
		for(int i=0; i<s.length(); ++i)
		{
			if(s[i] == '+')
				arr[i] = 1;
			else arr[i] = 0;
		}
		
		bool flag = false;
		while(!flag)
		{
			flag = true;
			int c = 0;
			
			//bool flagInternal = false;
			
			//flagInternal = true;
			while(c<s.length()-k+1)
			{
				if(arr[c] == 0)
				{
					//flagInternal = false;
					++flips;
					for(int i=c; i<c+k; ++i)
						arr[i] = -1*arr[i] + 1;
				}
				++c;
			}
		}
			
			/*for(int i=0; i<s.length(); ++i)
			{
				cout<<arr[i];
				if(arr[i] != 1)
					flag = false;
			}*/
			flag = false;
			for(int i=s.length()-k; i<s.length(); ++i)
			{
				if(arr[i] == 0)
					flag = true;
			}
			
			if(!flag)
				cout<<"Case #"<<t<<": "<<flips<<"\n";
			else cout<<"Case #"<<t<<": "<<"IMPOSSIBLE\n";
	}
};

int main()
{
	int t;
	cin>>t;
	
	Oversized** obj = new Oversized*[t];
	for(int i=0; i<t; ++i)
		obj[i] = new Oversized(i+1);
}