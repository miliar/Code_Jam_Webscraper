#include<iostream>
#include<sstream>
#include<fstream>
#include<string>
using namespace std;

int main()
{
	ifstream fin("Q2.in");
	ofstream fout("Q2_out.txt");
	int t;
	stringstream ss;
			string n_string;
	fin>>t;

	for(int i=0;i<t;i++)
	{
			int flag=0;
	long long	 n;
		fin>>n;
			ss<<n;
			ss>>n_string;
		//	cout<<n_string;
			ss.clear();
			while(true)
			{
			
	   if(n_string[n_string.size()-1]-48==0)     
	   {
	   	n=n-1;
	   		ss.clear();
	   		ss<<n;
			ss>>n_string;
		   	ss.clear();
			
	   }
	   else{
	   	for(int j=0;j<n_string.size()-1;j++)
	   	{
	   	//	cout<<"in for"<<endl;
	   		if((n_string[j]-48)>(n_string[j+1]-48))
	   		{
	   			flag = 1;
	   			break;
			   }
		   }
		 //  cout<<n_string<<"->"<<flag<<endl;
		   
		 if(flag==1)
		   {
		   	n=n-1;
		   		ss.clear();
		   		ss<<n;
			ss>>n_string;	ss.clear();
			flag=0;
		   }
		   else
		   {
		   //	cout<<n_string;
		   	break;
		   }   
		   if(n==1)
		   {break;
		   }
		  
	   	
	   }
	   
}
	  fout<<"Case #"<<i+1<<":"<<" "<<n<<endl;
		
		
	}
	
	
}
