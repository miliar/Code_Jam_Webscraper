#include<iostream>
#include<string>
#include<fstream>
using namespace std;
int main ()
{
	int t1;
	cin>>t1;
	int t=0;
	ofstream ofs("output.txt");
	while(t<t1)
	{
		string a;
		string s="";
		cin>>a;
		if (a.size()==1){
		cout<<"Case #"<<t+1<<": "<<a<<endl;
	    ofs<<"Case #"<<t+1<<": "<<a<<endl;}
		else{
		bool tt=false;
		for (int i=0; i<a.size()-1;i++)
		{
			int b=1;
			if (a[i]-'0'<a[i+1]-'0')
			{
				if(s.empty())
				s+=a[i];
				s+=a[i+1];
			}
			else if (a[i]==a[i+1])
			{
				while (a[i]==a[i+b])	
				b++;
				if (a[i+b]<'0' || a[i+b]>'9'){
				a[i+b]=a[i];}
				if (a[i]-'0'>a[i+b]-'0')
				{
					int test=a[i]-'0';
					test--;
					//cout<<a[i]-'0'<<" "<<a[i+b]<<" "<<b;
					if (test!=0 && s.empty()){
					s+=test+'0';
				    }
					i++;
					while (i<a.size()) 
					{
						i++;
						s+='9';
					}
					tt=true;
					cout<<"Case #"<<t+1<<": "<<s<<endl;
					ofs<<"Case #"<<t+1<<": "<<s<<endl;
				    break;
				}
				else if (a[i]-'0'<=a[i+b]-'0') 
				{
					int test=a[i]-'0';
					int j=1; 
					if(s.empty())
					j--;
					while(j<b)
					{
					s+=test+'0';
					j++; i++;
					}
					i--;
					if(a[i]<a[i+1])
					s+=a[i+1];
				}
				if(tt)
				break;	
			}    
			else 
			{
			   int test=a[i]-'0';
			   test--;
			   if (s.empty() && test==0)
			   {i++;
			   }
			   else if (!s.empty()){
			   s[s.size()-1]=test+'0';
			   i++;}
			   else
			   {
			    s+=test+'0'; i++;
			   	while(i<a.size())
			    {
			   	   i++;
			   	   s+='9';
			   	}
			   }
			   while (i<a.size())
			   {
			   	i++;
			   	s+='9';
			   }
			ofs<<"Case #"<<t+1<<": "<<s<<endl;
			cout<<"Case #"<<t+1<<": "<<s<<endl;
			tt=true;
			break;
			}
		}
		if(tt==false){
		cout<<"Case #"<<t+1<<": "<<s<<endl;	
		ofs<<"Case #"<<t+1<<": "<<s<<endl;
}
		}
		t++;
	}
}
