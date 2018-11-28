#include<iostream>
using namespace std;

class TidyNumbers
{
	private:
	int t;
	string n;
	int len;
	
	public:
	
	TidyNumbers(int i)
	{
		t = i;
		cin>>n;
		len = n.length();
		int flag = -1;
		
		while(flag<0)
		{
			flag = 1;
			for(int i=0; i<len-1; ++i)
			{
				if(n[i]>n[i+1])
				{
					flag = -1;
					break;
				}
			}
			
			if(flag>0)
				display();
			else changeNumber();
		}
		
	}
	
	void display()
	{
		n = n.substr(0, len);
		//cout<<len<<"\n";
		/*for(int i=0; i<len; ++i)
			s.at(i) = n[i];
		*/
		//n = s;
		
		cout<<"Case #"<<t<<": "<<n<<endl;
	}
	
	void changeNumber()
	{
		switch(n[len-1])
		{
			case '1':
			n.at(len-1) = '0';
			break;
			
			case '2':
			n.at(len-1) = '1';
			break;
			
			case '3':
			n.at(len-1) = '2';
			break;
			
			case '4':
			n.at(len-1) = '3';
			break;
			
			case '5':
			n.at(len-1) = '4';
			break;
			
			case '6':
			n.at(len-1) = '5';
			break;
			
			case '7':
			n.at(len-1) = '6';
			break;
			
			case '8':
			n.at(len-1) = '7';
			break;
			
			case '9':
			n.at(len-1) = '8';
			break;
			
			default:
			int i = len-1;
			while(n[i] == '0')
			{
				n.at(i) = '9';
				--i;
			}
			switch(n[i])
			{
				case '1':
				n.at(i) = '0';
				break;
			
				case '2':
				n.at(i) = '1';
				break;
			
				case '3':
				n.at(i) = '2';
				break;
			
				case '4':
				n.at(i) = '3';
				break;
			
				case '5':
				n.at(i) = '4';
				break;
			
				case '6':
				n.at(i) = '5';
				break;
			
				case '7':
				n.at(i) = '6';
				break;
			
				case '8':
				n.at(i) = '7';
				break;
			
				case '9':
				n.at(i) = '8';
				break;
			}
			break;
		}
		
		if(n[0] == '0')
		{
			//cout<<n.length();
			for(int i=0; i<len-1; ++i)
				n[i] = n[i+1];
			
			n[len-1] = '\0';
			//cout<<n.length();
			--len;
		}
		//display();
	}
};

int main()
{
	int t;
	cin>>t;
	TidyNumbers** obj = new TidyNumbers*[t];
	
	for(int i=0; i<t; ++i)
		obj[i] = new TidyNumbers(i+1);
}